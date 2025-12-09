import time

import streamlit as st
from pages.components import song_container

from Project.proj_backend import search_tracks

st.title("Search Songs")

if "login" not in st.session_state:
    st.switch_page("pages/account.py")

q = st.text_input("Song Name", key="qsong", label_visibility="hidden")
songs = ""
if q!="":
    with st.spinner(show_time=True):
        time.sleep(2)
    songs = search_tracks(q)
    print(songs)
if songs:
    with st.container() :
        for x in songs:
            song_container(id=x["id"], img=x["art"], name=x["name"])