#!/usr/bin/env python3
import datetime
import youtube_dl

def download_mp3(url, track_info=True):
    ydl_opts = { 'format': 'bestaudio/best',
                 'download_archive': '/tmp/cmpindex',
                 'outtmpl': '/home/diego021/Music/%(title)s.%(ext)s',
                 'noplaylist': True,
                 'postprocessors': [{ 'key': 'FFmpegExtractAudio',
                                      'preferredcodec': 'mp3',
                                      'preferredquality': '192' }] }
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        if track_info:
            track = ydl.extract_info(url, download=True)
            track = { 'id'      : track['id'],
                      'artist'  : track['artist'],
                      'title'   : track['title'],
                      'duration': track['duration'],
                      'url'     : track['webpage_url'],
                      'filename': ydl_opts['outtmpl'] % {'title':track['title'], 'ext':'mp3'},
                      'created' : datetime.datetime.utcnow() }
            return track
        else:
            ydl.download([url])

if __name__ == '__main__':
    download_mp3('https://www.youtube.com/watch?v=MnxU4ZxUh2k')

