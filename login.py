import streamlit as st
from spell_Correction_fix import apps
from streamlit_option_menu import option_menu
import json


with open("data/data_user.json", "r") as json_file:
    data_user = json.load(json_file)
# @st.cache_data
def upadate_user():
    data_user.update(user)
    with open("data/data_user.json", "w") as json_file:
        json.dump(data_user, json_file)
# @st.cache_data
def cache_user():
    user_cache = {}
    with open(f"data/user_cache/{email_user_sign}.json", "w") as json_file:
        json.dump(user_cache, json_file)

user = {}
if 'email' not in st.session_state:
    st.session_state.email = ""

def login_user():
    email_user_log = st.text_input("Masukkan Email")
    password_user_log = st.text_input("Masukkan Password", type="password")
    if st.button("Login"):
        if email_user_log in data_user and data_user[email_user_log] == password_user_log:
            st.success("Anda berhasil login")
            st.session_state.email = email_user_log
            st.session_state.page = 2
            # password = (password_user_log)
            st.rerun()
        elif email_user_log in data_user and data_user[email_user_log] != password_user_log:
            st.error("Password Salah")
        elif email_user_log not in data_user:
            st.error("Email Belum Terdaftar")
        else:
            st.error("Email dan Password Salah")

if 'page' not in st.session_state:
    st.session_state.page = 1

# Halaman 1
if st.session_state.page == 1:
    st.title("Selamat Datang")
    pilihan = st.selectbox("Login/Sign Up", ["Login", "Sign Up"])
    if pilihan == "Login":
        login_user()
    if pilihan == "Sign Up":
        # st.write(data_user)
        email_user_sign = st.text_input("Masukkan Email")
        password_user_sign = st.text_input("Masukkan Password", type="password")
        confirm_password = st.text_input("Masukkan Kembali Password", type="password")
        if st.button("Sign Up"):
            if email_user_sign not in data_user and password_user_sign == confirm_password:
                st.success("Sign Up Success, Silahkan Login")
                user.update({email_user_sign:password_user_sign})
                upadate_user()
                cache_user()
                data_user.update({email_user_sign:password_user_sign})
            elif email_user_sign in data_user and password_user_sign == confirm_password:
                st.error("Email Sudah Ada")
            elif password_user_sign != confirm_password:
                st.error("Password Confirm Password Salah")
            
            # st.json(data_user)
        

# Halaman 2
elif st.session_state.page == 2:
    with open(f"data/user_cache/{st.session_state.email}.json", "r") as json_file:
        data_cache = json.load(json_file)
    apps()