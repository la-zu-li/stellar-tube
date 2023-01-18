from sys import stderr
from os import listdir as lsdir
from os.path import exists
from os import remove

from yt_dlp.YoutubeDL import YoutubeDL

def configure(format='mp3', quiet=True, verbose=False, folder_path='./', video_code=False, track_numbers=False):
    global options

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

configure('flac', False, False, "/home/lazuli/Music/Musiquitas/Gris Soundtrack/", False, True)

downloader = YoutubeDL(options)
downloader.download("https://youtube.com/playlist?list=PLPUc0Mgs4Cs4D8BGffxUag083ek_mhZw2")