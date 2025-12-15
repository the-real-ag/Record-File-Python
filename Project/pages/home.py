import time

import streamlit as st
from pages.components import song_container

from Project.proj_backend import search_tracks

st.title("Search Songs")

if "login" not in st.session_state:
    st.switch_page("pages/account.py")
if "last_search" not in st.session_state:
    st.session_state.last_search = ""

q = st.text_input("Song Name", key="qsong", label_visibility="hidden")
songs = ""
if q!="":
    if st.session_state.last_search != q:
        with st.spinner(show_time=True):
            time.sleep(2)
    st.session_state.last_search = q
    songs = search_tracks(q)
if songs:
    with st.container() :
        for x in songs:
            song_container(song = x, onclick="add")