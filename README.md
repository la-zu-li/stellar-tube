# stellar-tube

A command-line tool for downloading media from Youtube, written in Python programming language.

## what can it do?

Stellar-tube can download media from a youtube video by entering its URL.
It can:

- download a file containing only the audio of a specific youtube video (no video)
- download a file containing only the video of a specific youtube video (no audio)
- download a file containing both audio and video
- convert the downloaded file to an audio format (mp3, mp2, wav, flac, m4a, ogg) or a video format (mp4, mkv, avi, ogv) of your preference
- download all the videos from a specific playlist.

## prerequisites

You need a Python interpreter installed for running this project, as well as the **yt_dlp** module installed.
**Python 3.10.6** was used to test it, but it can probably run with older versions as well.
After installing Python, to install **yt_dlp**, run the following command:

```bash
pip install yt_dlp
```

## running it

Having Python and **yt_dlp** installed, To simply download the audio from an youtube video, run the following command, while in the root directory of this project.

```bash
python stellartube.py <VIDEO URL> -d <destination folder> 
```

If you don't specify a destination folder for the downloaded file, it will be downloaded to the **files** folder, in the directory of this project.

if you want to download only the video instead, you can specify it with the following:

```bash
python stellartube.py <VIDEO URL> -d <destination folder> -t video_only
```

Or, the following, for a file with audio and video:

```bash
python stellartube.py <VIDEO URL> -d <destination folder> -t audio_and_video
```

When downloading only audio, the file is converted by default to mp3, if audio-only, or to mp4, if it's video-only or both both audio and video. To specify another format, run with the following option:

```bash
python stellartube.py <VIDEO URL> -d <destination folder> -f <preferred format>
```

Or, if you don't want the file to be converted at all, run the following to keep the original format from download:

```bash
python stellartube.py <VIDEO URL> -d <destination folder> --do-not-convert
```

If you want to download all the videos from a playlist, you can provide the url to a playlist instead. Run with the **-p** option to provide playlist indexing on filenames.

```bash
python stellartube.py <PLAYLIST URL> -d <destination folder> -p
```

To get information about stellartune usage, run the following:

```bash
python stellartube.py -h
```

## trivia

- Stellar-tube would use **pytube** library at first, but I was not satisfied with the download speed, as it would first get all the streams from the file and that took very long time.
  - I then proceeded to use **youtube_dl**, but then switched to **yt_dlp**, which is an youtube_dl fork, since youtube_dl is an outdated project.
  - yt_dlp then showed to be much faster to download the files.
- The name "stellar-tube" is a reference to **stellar tune**, an item from **Terraria**, which is my favorite game.
  - This item is a magic star-shaped guitar, that shoots stars when played. It's a magic weapon, that has a small chance to drop from Empress of Light.
- The developing of stellar-tube took about one week.
- Stellar-tube was the result of the second of some programming challenges two friends of mine organized. The challenge was developing a program able to download audio from youtube videos and youtube playlists.
- Stellar-tube will also be very useful to me, because I like to download music from Youtube, and I think Youtube Premium is stupid. I did that before using a browser extension and some scripts I made that converted the files, but the download part was mostly manual. Not anymore. I can just run this baby now.
