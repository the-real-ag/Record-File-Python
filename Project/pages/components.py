import streamlit as st
from streamlit_product_card import product_card

#* This includes General components for the site

def song_container(id,img,name,onclick =None, large = True, act = True, ):
    c = st.container(border=True)
    cover,title,action = c.columns((1.5 if large else 1,10,1.5 if large else 1), vertical_alignment="center")
    cover.image(img, use_container_width=True)
    title.write(f"####{"#" if not large else ""} {name}")
    if act:
        action.button("...", width=100, key=id, on_click=onclick)

def playlist(playlist_data):
    playlist_con = st.expander(label="Playlist 1")
    with playlist_con:
        for x in playlist_data:
            song_container(x["id"],x["cover"], x["name"], large = False)