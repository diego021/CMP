#!/usr/bin/env python3
from youtube.engine import YoutubeSong

if __name__ == '__main__':
    my_song = YoutubeSong('la triple nelson verde')
    my_song.search()
    my_song.download()

