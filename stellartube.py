from sys import stderr
from os.path import exists
from argparse import ArgumentParser

from yt_dlp.YoutubeDL import YoutubeDL

from lib.argument_parsing import parser

def configure(media_type='audio', file_format='mp3', quiet=True, verbose=False, folder_path='./', video_id=False, track_numbers=False):
    options = {
        "quiet": quiet,
        "verbose": verbose,
        "force_title": not quiet,
        "external_downloader": "native",
        "postprocessors": [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': file_format,
            'preferredquality': '192'
        }]
    }

    if media_type == "audio":
        options["format"] = "bestaudio/best"

    elif media_type == "video":
        options["format"] = "bestvideo/best"

    if video_id:
        options["outtmpl"] = "%(title)s [%(code)s] .%(ext)s"
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
    track_numbers = False

    if not exists(path):
        print(f"unexistent folder {path}", file=stderr)
        return
    
    if path[-1] != '/':
        path += "/"

    if args.playlist:
        track_numbers = True

    options = configure(media_type, file_format, quiet, verbose, path, video_id, track_numbers)
    YoutubeDL(options).download(url)


main()