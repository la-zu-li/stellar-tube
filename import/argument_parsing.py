from argparse import ArgumentParser

parser = ArgumentParser(
    prog = "stellar tube",
    description = "a media downloader from YouTube.",
    epilog = "Definitions for 'epilog': \n\t"
         + "1. Alternative spelling of epilogue\n\t"
         + "2. A short speech (often in verse) addressed directly to the audience by an actor at the end of a play\n\t"
         + "3. a short passage added at the end of a literary work"
)

parser.add_argument("-p", "--playlist")

options = parser.parse_args(["-p"])

print(options.playlist)