#streamlit frontend
# flow: login->your plans->create plan|view plan|start|end->logout
# TODO register

import streamlit as st
import requests
import os


BASE_URL = os.getenv("API_URL", "http://localhost:8000")


def welcome(msg:str=""):
    user = st.session_state.get('user')
    st.title(f"Welcome {user['username']}")

    st.info(msg)

    st.write("Your Training Plans")
    response = requests.get(f"{BASE_URL}/users/{user['id']}/training_plans")
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

    st.subheader("All Exercises")

    response = requests.get(f"{BASE_URL}/exercises")
    if response.status_code==200:
        exercises=response.json()
        if exercises:
            import pandas as pd
            from PIL import Image
            import io

            df = pd.DataFrame(exercises)
            # df['gif_url'] = df.apply(lambda row: create_gif(row['image_path_1'], row['image_path_2']), axis=1)

            # initialize session state for exercise selection
            if 'exercise_selection' not in st.session_state:
                st.session_state.exercise_selection = {ex['id']: False for ex in exercises}

            # search box
            search = st.text_input("Search exercises:")
            if search:
                df = df[df['name'].str.contains(search, case=False, na=False)]

            # checkbox
            df.insert(0, "Select", df['id'].map(st.session_state.exercise_selection))
            
            # editable table with checkboxes
            editable_df = st.data_editor(
                df,
                use_container_width=True,
                hide_index=True,
                height=400,
                column_config={
                    "Select": st.column_config.CheckboxColumn(required=True),
                    "id": st.column_config.Column(disabled=True),
                    "name": st.column_config.Column(disabled=True),
                    "description": st.column_config.Column(disabled=True),
                    # "gif_url": st.column_config.ImageColumn(disabled=True, label="Exercise"),
                    "equipment": st.column_config.Column(disabled=True),
                }
            )

           # update session state with selection
            for idx, row in editable_df.iterrows():
                st.session_state.exercise_selection[row['id']] = row['Select']
            
            # get all selected exercises
            selected = [ex_id for ex_id, checked in st.session_state.exercise_selection.items() if checked]
        else:
            st.info("No Exercises in db")
    else:
        st.error(f"error: {response.status_code}")

    with st.form(key="new_tp_form"):
        tp_title = st.text_input("title")

        submit =  st.form_submit_button("Create Plan")

        if submit:
            st.write(f"Selected: {selected}")
            st.write(f"Title: {tp_title}")
            # TODO backend

def create_gif(image_path_1, image_path_2):
    """Create a GIF from two images and return as bytes"""
    try:
        from PIL import Image
        import io
        
        image_1_recon_path = IMAGES_DIR / image_path_1.split('/')[-2] / image_path_1.split('/')[-1]
        image_2_recon_path = IMAGES_DIR / image_path_2.split('/')[-2] / image_path_2.split('/')[-1]
        
        img1 = Image.open(image_1_recon_path)
        img2 = Image.open(image_2_recon_path)
        
        # Resize to same size if needed
        img1 = img1.resize((200, 200))
        img2 = img2.resize((200, 200))
        
        # Create GIF in memory
        gif_bytes = io.BytesIO()
        img1.save(
            gif_bytes,
            format='GIF',
            save_all=True,
            append_images=[img2],
            duration=500,  # 500ms per frame
            loop=0  # infinite loop
        )
        gif_bytes.seek(0)
        return gif_bytes
        
    except Exception as e:
        st.warning(f"Could not create GIF: {e}")
        return None

   

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
