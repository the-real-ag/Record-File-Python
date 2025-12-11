import time

import streamlit as st
from pages.components import song_container

import Project.proj_backend as bckend

st.title("Search by mood")

mood = st.selectbox("Mood",
             ("Sad", "Calm", "Angry", "Happy", "Romantic", "Energetic", "Varied"),
             label_visibility= "hidden"
             )


with st.spinner(show_time=True):
    time.sleep(2)
songs = bckend.search_by_mood(mood)
if songs:
    with st.container() :
        for x in songs:
            song_container(id=x["id"], img=x["art"], name=x["name"])
