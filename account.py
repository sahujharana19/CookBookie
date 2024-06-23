import streamlit as st
import pymongo
from pymongo import MongoClient
from bson.objectid import ObjectId
import hashlib  # For password hashing

# Function to connect to MongoDB
def connect_to_mongodb():
    client = MongoClient()
    db = client["CookBookie"]
    return db

# Function to authenticate user
def authenticate_user(email, password):
    db = connect_to_mongodb()
    users_collection = db["users"]

    # Hash the provided password
    hashed_password = hashlib.sha256(password.encode()).hexdigest()

    # Query the database for the user
    user = users_collection.find_one({"email": email, "password": hashed_password})

    return user

# Function to reset password
def reset_password(email, new_password):
    db = connect_to_mongodb()
    users_collection = db["users"]

    # Hash the new password
    hashed_new_password = hashlib.sha256(new_password.encode()).hexdigest()

    # Update the user's password with the new password
    users_collection.update_one({"email": email}, {"$set": {"password": hashed_new_password}})

def app():
    # # Custom CSS for background
    # background ="""
    # <style>
    # body {
    #     background-image: url('login.jpg');
    #     background-size: cover;
    # }
    # </style>"""

    # st.markdown(background, unsafe_allow_html=True)

    st.title('Welcome to :violet[CookBookie] 🍽 📜 🥗 ')

    choice = st.selectbox('Login/Signup/Forgot Password', ['Login', 'Sign Up', 'Forgot Password'])

    if choice == 'Forgot Password':
        email = st.text_input('Enter Your Email Address')
        new_password = st.text_input('Enter Your New Password', type='password')
        if st.button('Reset Password'):
            # Reset the password with the new password
            reset_password(email, new_password)
            st.success("Your password has been reset successfully.")

    elif choice == 'Login':
        email = st.text_input('Email Address')
        password = st.text_input('Password', type='password')

        if st.button('Login'):
            user = authenticate_user(email, password)
            if user:
                st.success("Login successful!")
                # Set session state to indicate successful login
                st.session_state.logged_in = True
            else:
                st.error("Invalid email or password. Please try again.")

    else:
        email = st.text_input('Email Address')
        password = st.text_input('Password', type='password')
        username = st.text_input('Enter Your Unique Username')

        if st.button('Create My Account'):
            db = connect_to_mongodb()
            users_collection = db["users"]

            # Hash the password before storing it
            hashed_password = hashlib.sha256(password.encode()).hexdigest()

            # Insert the user into the database
            users_collection.insert_one({"email": email, "password": hashed_password, "username": username})
            st.success("Account created successfully!")

    # # Display home page content if user is logged in
    # if st.session_state.get("logged_in"):
    #     st.write("Home page content goes here.")

if __name__ == "_main_":
    app()