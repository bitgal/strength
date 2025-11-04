#streamlit frontend
# flow: login->your plans->create plan|view plan|start|end->logout
# TODO register

import streamlit as st
import requests

BASE_URL = "http://localhost:8000"
#streamlit frontend at http://localhost:8502

def welcome():
    user = st.session_state.get('user')
    st.title(f"Welcome {user['username']}")


def logon():
    st.title("Logon, stranger")
    with st.form(key="login_form"):
        email = st.text_input("Email *")
        password = st.text_input("Password *", type="password")
        submit = st.form_submit_button("Logon")

        if submit:
            response = requests.post(BASE_URL + '/users/authenticate', json={
                "email": email,
                "password": password
            })
            if response.status_code==200:
                user_data = response.json()
                st.session_state["user"] = user_data
                st.session_state['logged_in'] = True
                st.session_state.page = "welcome"
                st.rerun()
            else:
                st.error("Something is missing :(")


    if st.button("Don't have an account yet? Register"):
        st.session_state.page = "register"
        st.rerun()

def register():
    st.title("Let's do great things together!")
    with st.form(key="register_form"):
        email = st.text_input("Email *")
        password = st.text_input("Password *", type="password")
        # TODO add repeat pw
        username = st.text_input("Username")
        submit = st.form_submit_button("Register")

        if submit:
            response = requests.post(BASE_URL + '/users/register', json={
                "email": email,
                "password": password,
                "username": username
            })
            if response.status_code==200:
                user_data = response.json()
                st.session_state["user"] = user_data
                # st.success(f"Welcome {user_data['username']}")
                st.session_state['logged_in'] = True
                st.session_state.page = "welcome"
                st.rerun()
            else:
                st.error("Something is missing :(")

def main():

    #init page
    if "page" not in st.session_state:
        st.session_state.page = "logon"

    if st.session_state.page == "logon":
        logon()
    elif st.session_state.page == "register":
        register()
    elif st.session_state.page == "welcome":
        welcome()

if __name__ == "__main__":
    main()
