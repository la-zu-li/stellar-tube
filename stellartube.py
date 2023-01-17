from sys import stderr
from os import listdir as lsdir
from os.path import exists
from os import remove

from pytube import YouTube
from pytube import Playlist
from pytube.exceptions import RegexMatchError
from pytube.exceptions import MaxRetriesExceeded

from ffmpy import FFmpeg

def getVideoFromYoutube(url):
    try:
        video = YouTube(url)
    except RegexMatchError:
        print(f"Invalid video URL. The URL '{url}' is not an URL to an Youtube video.", file=stderr)
        return None
    return video

def getPlaylistFromYoutube(url):
    try:
        playlist = Playlist(url)
    except RegexMatchError:
        print(f"Invalid playlist URL. The URL '{url}' is not an URL to an Youtube playlist.", file=stderr)
        return None
    return playlist

def downloadFileFromYoutube(url, file_name=None, folder_path=None, media_type="audio", prefix=None):
    video = getVideoFromYoutube(url)
    if not video:
        return None

    print(f"collecting streams for '{video.title}'...")
    streams = video.streams

    if media_type == "audio":
        stream = streams.filter(only_audio=True, audio_codec='opus').order_by('abr').last()

        print(f"downloading audio file from video '{video.title}...'")
        try:
            a = stream.download(filename=file_name, output_path=folder_path, filename_prefix=prefix)
        except MaxRetriesExceeded:
            print(f"'{video.title}' download failed. Try again later.")
            return None
        return 1

    elif media_type == "video":
        # nothing here yet
        pass

    else:
        return None

def downloadPlaylistFromYouTube(url, folder_path, media_type, set_track_numbers=False):
    pls = getPlaylistFromYoutube(url)
    if not pls:
        return None
    
    if set_track_numbers:
        n_chars_track_number = len(str(len(pls)))

        for i in range(len(pls)):
            track_number = str(i+1)
            track_number_str = "0" * (n_chars_track_number-len(track_number)) + track_number
            downloadFileFromYoutube(pls[i], folder_path=folder_path, media_type=media_type, prefix=f"{track_number_str} - ")
    else:
        for x in pls:
            downloadFileFromYoutube(x, folder_path=folder_path, media_type=media_type)

def convertFiles(folder_path, extension, delete_old=True):
    if not exists(folder_path):
        print(f"Invalid path. The folder '{folder_path}' does not exist.", file=stderr)
        return None

    if folder_path[-1] != "/":
        folder_path += "/"

    old_files = lsdir(folder_path)
    new_files = [x.split('.') for x in old_files]
    new_files = ['.'.join(x[:-1] + [extension]) if len(x) > 1 else '.'.join(x + extension) for x in new_files]
    old_files = [folder_path + x for x in old_files]
    new_files = [folder_path + x for x in new_files]
    old_files.sort()
    new_files.sort()

    [print(x) for x in old_files]
    [print(x) for x in new_files]

    for i in range(len(old_files)):
        FFmpeg(
            inputs={old_files[i]: None},
            outputs={new_files[i]: None}
        ).run()
    
    if delete_old:
        for x in old_files:
            remove(x)