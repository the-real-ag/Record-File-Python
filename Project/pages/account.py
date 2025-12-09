import streamlit as st


def logout(): 
    for x in st.session_state:
        del st.session_state[x]
    print([x for x in st.session_state])


if "login" not in st.session_state or "uid" not in st.session_state:
    st.session_state.login = True
@st.dialog("Login" if st.session_state.login else "Signup", dismissible=False)
def auth_dialog():
    username = st.text_input("**Username**")
    password = st.text_input("**Password**")
    with st.container(horizontal=True, horizontal_alignment="distribute"):
        if st.button("Submit"):
            pass
        if st.button(f"###### {"Login" if st.session_state.login else "Signup"}", type="tertiary",):
            st.session_state.login = not st.session_state.login
            st.rerun()
# auth_dialog()
st.write("## Account options")

#TODO: Logout option
st.button("**Logout**",type="primary", on_click=logout)
