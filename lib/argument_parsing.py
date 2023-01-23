from argparse import ArgumentParser

parser = ArgumentParser(
    prog = "stellartube",
    description = "a media downloader from YouTube.",
    epilog = "Definitions for 'epilog': \n\t"
         + "1. Alternative spelling of epilogue\n\t"
         + "2. A short speech (often in verse) addressed directly to the audience by an actor at the end of a play\n\t"
         + "3. a short passage added at the end of a literary work"
)

parser.add_argument("url", help="URL to download")
parser.add_argument("-p", "--playlist", help="download all videos from a playlist instead", action="store_true")

if __name__ == '__main__':
    args = parser.parse_args()
    print(args.url)