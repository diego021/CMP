#!/usr/bin/env python3
import youtube_dl

def download_mp3(url):
    ydl_opts = { 'format': 'bestaudio/best',
                 'download_archive': '/tmp/cmpindex',
                 'outtmpl': '/home/diego021/Music/%(title)s.%(ext)s',
                 'postprocessors': [{ 'key': 'FFmpegExtractAudio',
                                      'preferredcodec': 'mp3',
                                      'preferredquality': '192' }] }
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])

if __name__ == '__main__':
    download_mp3('https://music.youtube.com/watch?v=-72BiJv09Is')
