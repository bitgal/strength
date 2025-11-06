#streamlit frontend
# flow: login->your plans->create plan|view plan|start|end->logout
# TODO register

import streamlit as st
import requests

BASE_URL = "http://localhost:8000"
#streamlit frontend at http://localhost:8502


def welcome(msg:str=""):
    user = st.session_state.get('user')
    st.title(f"Welcome {user['username']}")

    st.info(msg)

    st.write("Your Training Plans")
    response = requests.get(f"{BASE_URL}/users/{user["id"]}/training_plans")
    if response.status_code==200:
        tps = response.json()
        if tps:
            st.table(tps)
        else:
            st.info("No Training Plans yet")
            if st.button("Create your first plan"):
                st.session_state.page = "create_training_plan"
                st.rerun()
    else:
        st.info("smt went wrong fetching your plans")


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

def new_tp():
    st.title("A brand new Training Plan")

    st.divider()

    col1, col2 = st.columns(2)

    with col1:
        st.subheader("All Exercises")

        response = requests.get(f"{BASE_URL}/exercises")
        if response.status_code==200:
            exercises=response.json()
            if exercises:
                st.table(exercises)
            else:
                st.info("No Exercises in db")
        else:
            st.error(f"error: {response.status_code}")


    with st.form(key="new_tp_form"):
        st.text_input("title")

        submit =  st.form_submit_button("Create Plan")

        if submit:
            pass
    

   

def main():
    #init page
    #  if st.session_state.page == "logon":
    #     # Reset session state except for page
    #     keys_to_reset = [key for key in st.session_state.keys() if key != "page"]
    #     for key in keys_to_reset:
    #         del st.session_state[key]
    if "page" not in st.session_state: 
        st.session_state.page = "logon"

    if st.session_state.page == "logon":
        logon()
    elif st.session_state.page == "register":
        register()
    elif st.session_state.page == "welcome":
        welcome()
    elif st.session_state.page == "create_training_plan":
        new_tp()

if __name__ == "__main__":
    main()
