import time

import streamlit as st
from pages.components import song_container

import Project.proj_backend as bckend


@st.dialog("Create Playlist")
def create_playlist_dialog(songs = []):
    name = st.text_input("Name of playlist")
    if st.button("Submit", type="primary"):
        if name!="":
            bckend.create_playlist(songs=songs, uid = st.session_state.uid, name = name)
            st.session_state.close_dialog = True
            print(st.session_state.close_dialog)
            st.rerun()
        else:
            st.warning("Empty name")
if "close_dialog" not in st.session_state:
    
    st.session_state.close_dialog = False

  

# __main__


st.title("Your Playlists")
st.space(2)

if st.button("Create Playlist",):
    st.session_state.close_dialog = False
    if not st.session_state.close_dialog:
        create_playlist_dialog()
# if st.session_state.close_popover:
#     st.spinner(text="Loading..", show_time=True)
#     time.sleep(2)
#     st.session_state.close_popover = False
#     print(st.session_state.close_popover)
#     st.rerun()
    
st.space(1)
for x in bckend.get_playlists(st.session_state.uid):
    playlist_con = st.expander(label=x["name"])
    with playlist_con:
        for x in x["songs"]:
            song_container(song = x, large = False, onclick="remove")