from sys import stderr
from os.path import exists
from argparse import ArgumentParser

from yt_dlp.YoutubeDL import YoutubeDL

from lib.argument_parsing import parser

def configure(media_type='audio', convert=True, file_format='mp3', quiet=True, verbose=False, folder_path='./', video_id=False, track_numbers=False):
    options = {
        "quiet": quiet,
        "verbose": verbose,
        "force_title": not quiet,
        "external_downloader": "native",
    }

    if media_type == "audio_only":
        options["format"] = "bestaudio/best"

    elif media_type == "video_only":
        options["format"] = "bestvideo*"

    if convert:
        if file_format in ["mp3", "flac", "wav", "ogg", "m4a", "mp2"]:
            if media_type == "video_only":
                print("ERROR: cannot extract audio from a video-only file", file=stderr)
                return None

            options["postprocessors"] = [{
                'key': 'FFmpegExtractAudio',
                'preferredcodec': file_format,
                'preferredquality': '192'
            }]
        else:
            if media_type == "audio_only":
                print("ERROR: cannot extract video from a audio-only file", file=stderr)
                return None

            options["postprocessors"] = [{
                'key': 'FFmpegVideoConvertor',
                'preferedformat': file_format
            }]

    if video_id:
        options["outtmpl"] = "%(title)s [%(id)s] .%(ext)s"
    else:
        options["outtmpl"] = "%(title)s.%(ext)s"

    if track_numbers:
        options["outtmpl"] = "%(playlist_index)d - " + options["outtmpl"]

    options["outtmpl"] = folder_path + options["outtmpl"]

    return options

def main():
    args = parser.parse_args()

    url = args.url
    media_type = args.type
    file_format = args.format
    quiet = args.quiet
    verbose = args.verbose
    path = args.destination_folder
    video_id = args.id_in_filename

    convert = not args.do_not_convert
    track_numbers = False

    if not file_format:
        if media_type == "audio_only":
            file_format = "mp3"
        else:
            file_format = "mp4"

    if not exists(path):
        print(f"unexistent folder {path}", file=stderr)
        return
    
    if path[-1] != '/':
        path += "/"

    if args.playlist:
        track_numbers = True

    options = configure(media_type, convert, file_format, quiet, verbose, path, video_id, track_numbers)
    
    if(options):
        YoutubeDL(options).download(url)


main()
