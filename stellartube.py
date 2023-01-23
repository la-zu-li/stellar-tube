from sys import stderr
from os.path import exists
from argparse import ArgumentParser

from yt_dlp.YoutubeDL import YoutubeDL

from lib.argument_parsing import parser

def configure(format='mp3', quiet=True, verbose=False, folder_path='./', video_code=False, track_numbers=False):
    options = {
        "quiet": quiet,
        "verbose": verbose,
        "format": "bestaudio/best",
        "force_title": True,
        "external_downloader": "native",
        "postprocessors": [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': format,
            'preferredquality': '192'
        }]
    }

    if video_code:
        options["outtmpl"] = "%(title)s [%(code)s] .%(ext)s"
    else:
        options["outtmpl"] = "%(title)s.%(ext)s"

    if track_numbers:
        options["outtmpl"] = "%(playlist_index)d - " + options["outtmpl"]

    options["outtmpl"] = folder_path + options["outtmpl"]

    return options

args = parser.parse_args()

url = args.
codec = 'flac'
quiet = True
verbose = True
path = './files/'
video_code = False
track_numbers = False

if args.playlist:
    track_numbers = True

options = configure(codec, quiet, verbose, path, video_code, track_numbers)
YoutubeDL(options).download()