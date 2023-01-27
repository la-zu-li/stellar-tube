from argparse import ArgumentParser, RawTextHelpFormatter

logo = """
           ⢠        ⣄ ⢠⡀
      ⢀⣤⠾⢋⣡⣼⣧⠤ ⢀⣤⣤⡀ ⣿ ⢸⡇   ⢀⣾⣆   ⢸⣆⣤⠤
     ⠐⠛⠷⢦⡤ ⢸⡇⠠⣾⣿⠥⠼⠇ ⢸⡇ ⣿ ⠙⠿⣿⣥⣽⡿⠟⠁⢸⡏
    ⢀⣀⣴⠟⠋  ⠘⣿ ⠈⠻⠶⠶⠖⠂⠈⣷ ⢹⡆ ⣼⠿⠁⠹⢿⡄ ⠘⣷
            ⠻        ⠙⠆⠈⠳         ⠙
        ⢠⣶⣶⣶⣶⡄⢠⣶⡄⢠⣶⡄⢠⣶⡄   ⢀⣴⣶⣶⣦⡀
         ⠉⣿⣿⠉ ⢸⣿⡇⢸⣿⡇⢸⣿⣷⣶⣶⡄⢸⣿⡿⠿⠿⠃
          ⢿⡿  ⠘⢿⣿⣿⡿⠃⠸⣿⣿⣿⣿⠇⠘⢿⣿⣿⣿⠆ 
    """

parser = ArgumentParser(
    prog = "stellartube",
    description = "a media downloader from YouTube.",
    epilog = logo + "\n" + "developed by Lazuli, a non-binary who cares",
    formatter_class=RawTextHelpFormatter
)
parser.add_argument(
    "url",
    help="URL to download"
)
parser.add_argument(
    "-p", "--playlist",
    help="put playlist indexing on filename when downloading videos from a playlist\n\n",
    action="store_true"
)
parser.add_argument(
    "-d", "--destination-folder",
    help="specify destination download folder.\n\n",
    default="./files/"
)
parser.add_argument(
    "-f", "--format",
    help="final media-file format (post-download)\n\n",
    default=None,
    choices=["mp2", "mp3", "m4a", "ogg", "flac", "wav", "mp4", "mkv", "avi", "ogv"]
)
parser.add_argument(
    "-t", "--type",
    help="type of media-file that will be downloaded\n\n",
    default="audio_only",
    choices=["audio_only", "audio_and_video", "video_only"]
)
verbose_or_quiet = parser.add_mutually_exclusive_group()

verbose_or_quiet.add_argument(
    "-v", "--verbose",
    help="display more downloading information\n\n",
    action="store_true",
    default=False
)
verbose_or_quiet.add_argument(
    "-q", "--quiet",
    help="display no downloading information\n\n",
    action="store_true",
    default=False
)
parser.add_argument(
    "-i", "--id-in-filename",
    help="save file with the video ID in its name\n\n",
    action="store_true",
    default=False
)
parser.add_argument(
    "--do-not-convert",
    help="keep the media-file with original format from downloading\n\n",
    action="store_true",
    default=False    
)