import streamlit as st

import Project.proj_backend as bckend


def logout(): 
    for x in st.session_state:
        del st.session_state[x]
    print([x for x in st.session_state])

if "login" not in st.session_state:
    st.session_state.login = True
@st.dialog("Login" if st.session_state.login else "Signup", dismissible=False)
def auth_dialog():
    username = st.text_input("**Username**")
    password = st.text_input("**Password**")
    if "login_err_text" in st.session_state:
        st.error(st.session_state.login_err_text)
    with st.container(horizontal=True, horizontal_alignment="distribute"):
        if st.button("Submit"):
            try:
                uid = bckend.auth(username=username, password=password, mode= "login" if st.session_state.login else "signup")
                st.session_state.uid = uid
                st.rerun()
            except ValueError as e:
                st.session_state.login_err_text = e
                st.rerun()
        if st.button(f"###### {"Signup" if st.session_state.login else "Login"}", type="tertiary",):
            st.session_state.login = False if st.session_state.login else True
            if "login_err_text" in st.session_state:
                del st.session_state.login_err_text
            st.rerun()
if "uid" not in st.session_state:
    auth_dialog()
st.write("## Account options")
if "uid" in st.session_state:
    st.write(f"**User id**: {st.session_state.uid}")
st.button("**Logout**",type="primary", on_click=logout, key="logout")
