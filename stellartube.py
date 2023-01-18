from sys import stderr
from os import listdir as lsdir
from os.path import exists
from os import remove

from pytube import YouTube, Playlist
from yt_dlp.YoutubeDL import YoutubeDL

def configure():
    global options

    options = {
        "quiet": True,
        "format": "bestaudio/best",
        "force_title": True,
        "external_downloader": "native",
        "postprocessors": [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'flac',
            'preferredquality': '192',
        }],

    }

configure()
ps = Playlist("https://youtube.com/playlist?list=PLPUc0Mgs4Cs4D8BGffxUag083ek_mhZw2")

a = YoutubeDL(options)
a.download(ps)