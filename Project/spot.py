import spotipy
from spotipy.oauth2 import SpotifyOAuth

sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id="76673bbf062648368df5b6dfa9c5837e",
                                               client_secret="5a4059bafd6b4189b67dfeee8030d71f",
                                               redirect_uri="http://127.0.0.1:8000/callback",
                                               scope="user-library-read"))

taylor_uri = 'spotify:artist:06HL4z0CvFAxyc27GXpf02'
try:
    results = sp.search("star", limit=10, offset=1, type = "track", market=any)
except Exception as e:
    print(e.message)
tracks = results["tracks"]["items"]
for x in tracks:
    print(x["name"], x["id"])