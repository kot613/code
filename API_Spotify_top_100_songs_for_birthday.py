from bs4 import BeautifulSoup
import requests
import spotipy

SPOTIPY_CLIENT_ID = 'Your client ID'
SPOTIPY_CLIENT_SECRET = 'Your client secret'
SPOTIPY_REDIRECT_URI = 'http://127.0.0.1:9090'
SCOPE = "playlist-modify-private"


def charts_hot_100(url: str):
    # =============== Top 100 Billboard Web scraping =========
    list_song, list_group, all_dct = [], [], {}
    html = requests.get(url=url)
    if not html.raise_for_status():
        soup = BeautifulSoup(html.text, 'html.parser')
        find = soup.find_all('li', class_='o-chart-results-list__item')
        for block in find:
            if block.find('span', class_='a-no-trucate'):
                list_group.append(block.find('span', class_='a-no-trucate').text.strip())
            if block.find('h3', id='title-of-a-story', class_='a-no-trucate'):
                list_song.append(block.find('h3', id='title-of-a-story', class_='a-no-trucate').text.strip())

    song_names = [name.replace("'", "").replace("!", "") for name in list_song]
    # all_dct = {k: v for k, v in zip(song_names, list_group)}

    return song_names, list_group


def create_playlist(song_names: list, artist_names: list, input_data: str):
    # # ==================== Spotify API =======================
    spotify_auth = spotipy.oauth2.SpotifyOAuth(client_id=SPOTIPY_CLIENT_ID,
                                               client_secret=SPOTIPY_CLIENT_SECRET,
                                               redirect_uri=SPOTIPY_REDIRECT_URI,
                                               scope=SCOPE)
    sp = spotipy.Spotify(oauth_manager=spotify_auth)

    user_id = sp.current_user()["id"]
    song_urls = []

    for song, artist in zip(song_names, artist_names):
        items = sp.search(q=f"track: {song} artist: {artist}", type="track")["tracks"]["items"]
        if len(items) > 0:
            song_urls.append(items[0]["uri"])

    playlist_id = sp.user_playlist_create(user=user_id, name=f"{input_data} Billboard HoT 100", public=False)["id"]

    sp.playlist_add_items(playlist_id=playlist_id, items=song_urls)


def main():
    input_data = input('What year you would like to travel to in YYYY-MM-DD format?:')
    url = 'https://www.billboard.com/charts/hot-100/' + input_data
    song_names, artist_names = charts_hot_100(url=url)
    create_playlist(song_names, artist_names, input_data)


if __name__ == '__main__':
    main()
