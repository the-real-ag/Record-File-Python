import json

import pymysql as sql
import spotipy
from spotipy.oauth2 import SpotifyOAuth

scon = sql.connect(user="root", host='localhost', password="mvn123", database="music", autocommit=True)
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id="76673bbf062648368df5b6dfa9c5837e",
                                               client_secret="5a4059bafd6b4189b67dfeee8030d71f",
                                               redirect_uri="http://127.0.0.1:8000/callback",
                                               scope="user-library-read"))

def mood_genre(mood):
    with scon.cursor() as con:
        
        con.execute(f"select * from gen_mood where mood='{mood}'")
        a = [x[0] for x in con]
        return a
def search_by_mood(mood):
    gens = mood_genre(mood)
    print(gens)
    res = sp.search(f"genre:{gens}", type="track", limit=12)['tracks']["items"]
    a = [{"name": x["name"],"id": x["id"], "art": x["album"]["images"][-2]['url']} for x in res]
    return a
def search_tracks(q):
    res = sp.search(f"{q}", type="track", limit=12)['tracks']["items"]
    a = [{"name": x["name"],"id": x["id"], "art": x["album"]["images"][-2]['url']} for x in res]
    return a
def retrieve_music(ids):
    a = [{"name": x["name"],"id": x["id"], "art": x["album"]["images"][-2]['url']} for x in sp.tracks(tracks=ids)["tracks"]]
    return a
def auth(username, password, mode="login"):
    if mode == "login":
        with scon.cursor() as con:
            try:
                con.execute(f"select id from auth where Username = '{username}' and Password  = '{password}'")
                values = con.fetchall()
                if len(values) == 0:
                    raise ValueError("Incorrect email or password")
                else:
                    return values[0][0]
            except Exception as e:
                print(e)
    elif mode == "signup":
        with scon.cursor() as con:
            try:
                con.execute(f"insert into auth (Username,Password) values('{username}','{password}') ")
                return auth(username, password)
            except Exception as e:
                if e[0] == 1062:
                    print("Username Already Exists")
                    raise ValueError("Email Already exists")

def create_playlist(uid, name, songs):
    with scon.cursor() as con:
        song_json = json.dumps(songs)
        try:
            con.execute(f"insert into playlist(name, playlist_data, uid) values('{name}', '{song_json}', {uid})")
        except Exception as e:
            print(e)
def edit_playlist(uid, pid, songs):
    with scon.cursor() as con:
        con.execute(f"update playlist set playlist_data='{json.dumps(songs)}' where uid={uid} and pid={pid}")
def get_playlists(uid,):
    with scon.cursor() as con:
        con.execute(f"select playlist.pid,playlist.playlist_data from auth inner join playlist on auth.id=playlist.uid where playlist.uid = {uid};")
        return [{ "pid": x[0], "songs": json.loads(x[1])} for x in con.fetchall()]
#__main__

# id = input("enter id")
# password = input("Password")
# a = auth(id,password, mode="login")
# songs = [1,2,3]
'''
Song Data format:
[{"name": '', "id": '', "art": ''}]
'''
print(search_tracks("Hi"))