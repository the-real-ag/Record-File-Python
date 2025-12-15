import streamlit as st

pages = {
    "Songs": [
        st.Page("./pages/home.py", title="Search new songs!"),
        st.Page("./pages/mood_songs.py", title = "Songs for your mood")
    ],
    "Profile": [
        st.Page("./pages/playlists.py", title= "Your playlists"),
        st.Page("./pages/account.py", title = "Manage your account"),
    ]

}

pg = st.navigation(pages)
pg.run()