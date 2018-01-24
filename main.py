# -*- coding: utf-8 -*-
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import json


class Credential(object):
    client_id = '2e9c8dc340894985a5e09302dbf5cc0d'
    client_secret = 'e80fcc9fee984c34b230f5892050c2a9'

    def __init__(self):
        client_credentials_manager = \
            spotipy.oauth2.SpotifyClientCredentials(client_id=self.client_id, client_secret=self.client_secret)
        self.spotify = spotipy.Spotify(client_credentials_manager=client_credentials_manager)


class SpotifySpider(Credential):
    def search_artist(self, name):
        result = self.spotify.search(q='artist:' + name, type='artist')
        for i in result['artists']['items']:
            print("{0} - popularity: {1}, id: {2}".format(i['name'], i['popularity'], i['id']))

    def search_relate(self, artist_id):
        result = self.spotify.artist_related_artists(artist_id)
        for artist in result['artists']:
            artist_name = artist['name']
            popularity = artist['popularity']
            unique_id = artist['id']
            print("{0} - popularity: {1}, id: {2}".format(artist_name, popularity, unique_id))

        data = json.dumps(result, indent=3)
        with open(r'related_artist.json', 'w') as f:
            f.write(data)


if __name__ == "__main__":
    s = SpotifySpider()
    # s.search_artist("rihanna")
    s.search_relate('5pKCCKE2ajJHZ9KAiaK11H')
