import requests
from bs4 import BeautifulSoup


def scrape_songs(url):
    billboard_site = requests.get(url)
    billboard_site = billboard_site.text
    soup_obj = BeautifulSoup(billboard_site, 'html.parser')
    song_list_returned = soup_obj.find_all(name='span',
                                           class_='chart-element__information__song text--truncate color--primary')
    artist_list_returned = soup_obj.find_all(name='span',
                                             class_='chart-element__information__artist text--truncate color--secondary')
    song_list = []
    artist_list = []
    for song, artist in zip(song_list_returned, artist_list_returned):
        song_list.append(str(song.getText()))
        artist_list.append(str(artist.getText()))

    return song_list, artist_list
