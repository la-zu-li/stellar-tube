from sys import stderr
from os import listdir as lsdir
from os.path import exists
from os import remove

from pytube import YouTube
from pytube import Playlist
from pytube.exceptions import RegexMatchError

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

def downloadFileFromYoutube(url, file_name=None, folder_path=None, media_type="audio"):
    video = getVideoFromYoutube(url)
    if not video:
        return None

    streams = video.streams
    
    if media_type == "audio":
        stream = streams.filter(only_audio=True, audio_codec='opus').order_by('abr').last()

        a = stream.download(filename=file_name, output_path=folder_path)
        return a
    elif media_type == "video":
        # nothing here yet
        pass

    else:
        return None

def downloadPlaylistFromYouTube(url, folder_path, media_type):
    pls = getPlaylistFromYoutube(url)
    if not pls:
        return None
    
    for x in pls:
        downloadFileFromYoutube(x, folder_path=folder_path, media_type=media_type)

def convertFiles(folder_path, extension, delete_old=True):

    if not exists(folder_path):
        print(f"Invalid path. The folder '{folder_path}' does not exist.", file=stderr)
        return None

    old_files = lsdir(folder_path)
    new_files = [x.split('.') for x in old_files]
    new_files = ['.'.join(x[:-1] + [extension]) if len(x) > 1 else '.'.join(x + extension) for x in new_files]

    FFmpeg(
        inputs=dict([(folder_path+x, None) for x in old_files]),
        outputs=dict([(folder_path+x, None) for x in new_files])
    ).run()
    
    if delete_old:
        for x in old_files:
            remove(folder_path + x)