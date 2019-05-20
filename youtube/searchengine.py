#!/usr/bin/env python3
import youtube_dl

def search_youtube(string: 'text to search', max_duration: 'max duration allowed in seconds'=420) -> list:
    search_result = youtube_dl.YoutubeDL({}).extract_info('ytsearch10: {}'.format(string), download=False)
    data = []
    for entry in search_result['entries']:
        if len(data) == 5: break
        if entry['duration'] > max_duration: continue
        track = { 'id'      : entry['id'],
                  'artist'  : entry['artist'],
                  'title'   : entry['title'],
                  'duration': entry['duration'],
                  'url'     : entry['webpage_url'] }
        data.append(track)
    return data

if __name__ == '__main__':
    for song in search_youtube('buitres'):
        print(song)

