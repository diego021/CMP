#!/usr/bin/env python3
import database.driver as db
from .downloader import download_mp3
from .searchengine import search_youtube

class YoutubeSong:
    '''This class is the main flow of search and download functions from youtube'''
    def __init__(self, song):
        self.song = song
        self.search_info = None
        self.track = None

    @staticmethod
    def choice(my_options: list) -> dict:
        choices = len(my_options)
        while True:
            try:
                print('Please choose any of the following options:\n')
                for idx,value in enumerate(my_options):
                    print('[{idx}] Title: {track[title]} // Artist: {track[artist]} // Duration: {track[duration]}'.format(idx=idx+1, track=value))
                print()
                answer = int(input('I choose option: ')) - 1
                if my_options[answer] and answer != -1:
                    break
            except (IndexError, ValueError):
                continue
        return my_options[answer]

    def search(self):
        self.search_info = self.choice(search_youtube(self.song))

    def download(self):
        url = self.search_info['url']
        self.track = download_mp3(url)
        exists = db.find_local_track(self.track['filename'])
        if not exists:
            db.insert('library', self.track)

