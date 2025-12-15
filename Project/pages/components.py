from typing import Literal

import streamlit as st
from streamlit_product_card import product_card

import Project.proj_backend as backend

# This includes General components for the site
if "open_action_dialog" not in st.session_state:
    st.session_state.open_action_dialog = False

def song_container(song,onclick = "none", large = True, act = True, playlist = None):
    id,img,name = song["id"], song["art"], song["name"]
    c = st.container(border=True)
    cover,title,action = c.columns((1.5 if large else 1,10,1.5 if large else 1), vertical_alignment="center")
    cover.image(img, width="stretch")
    title.write(f"####{"#" if not large else ""} {name}")
    
    if act:
        if action.button("", width=100, key=id, icon=":material/add:" if onclick == "add" else ":material/delete:" if onclick == "remove" else None, type="primary" if onclick == "remove" else "secondary"):
            st.session_state.open_action_dialog = True
            if st.session_state.open_action_dialog:
                if onclick == "add":
                    add(song=song)
                    pass
                elif onclick == "remove":
                    remove(song=song, playlist=playlist)
                    pass
                else:
                    pass

@st.dialog("Add to playlist")
def add(song):
    l_playlist = backend.get_playlists(uid = st.session_state.uid)
    playlist_data = st.selectbox(label="Playlists", options=l_playlist, format_func=lambda song: song["name"])
    st.space(2)
    c= st.container(horizontal=True, horizontal_alignment="distribute") 
    with c:
        if st.button("Add to playlist"):
            playlist_data["songs"].append(song)
            print(playlist_data["songs"])
            backend.edit_playlist(uid=st.session_state.uid, pid=playlist_data["pid"], songs=playlist_data["songs"])
            st.session_state.open_action_dialog = False
            st.rerun()

            # backend.create_playlist(uid=st.session_state.uid, )

def dialogFormat(song):
    return str(song)+"A"

def remove(song, playlist):
    playlist["songs"].remove(song)
    backend.edit_playlist(uid = st.session_state.uid, pid=playlist["pid"], songs=playlist["songs"])
    st.rerun()

