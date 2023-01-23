from argparse import ArgumentParser

parser = ArgumentParser(
    prog = "stellartube",
    description = "a media downloader from YouTube.",
    epilog = "and then, stellar-tube and their friends lived happily ever after. THE END."
)

parser.add_argument("url", help="URL to download")
parser.add_argument("-p", "--playlist", help="download all videos from a playlist instead", action="store_true")
parser.add_argument("-d", "--destination-folder", help="specify destination download folder.", default="./files/")
parser.add_argument("-f", "--format", help="output file format", default="mp3", choices=["mp2", "mp3", "m4a", "ogg", "flac", "wav", "webm", "mp4", "mkv", "avi", "ogv"])
parser.add_argument("-t", "--type", help="type of media to download", default="audio", choices=["audio", "audio_and_video", "video"])
parser.add_argument("-v", "--verbose", help="display more downloading information", action="store_true", default=False)
parser.add_argument("-q", "--quiet", help="display no downloading information", action="store_true", default=False)
parser.add_argument("-i", "--id-in-filename", help="save file with the video ID in its name", action="store_true", default=False)