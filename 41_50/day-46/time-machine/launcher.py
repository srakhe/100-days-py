from datetime import datetime
import scraper
import spotify


def validate_date(date_text):
    try:
        datetime.strptime(date_text, '%Y-%m-%d')
    except ValueError:
        raise ValueError("Incorrect data format, should be YYYY-MM-DD")
    else:
        return True


date = input('Enter the date you\'d like to be taken back to! [YYYY-MM-DD]')
if date:
    if validate_date(date):
        url = 'https://www.billboard.com/charts/hot-100/' + date
        songs, artists = scraper.scrape_songs(url)
        playlist_id = spotify.create_playlist(date)
        done = spotify.add_songs_to_playlist(playlist_id, songs, artists)
        if done:
            print('Playlist was created successfully!')
