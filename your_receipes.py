import os

import streamlit as st
from pymongo import MongoClient
import uuid  # For generating unique IDs


# Function to connect to MongoDB
def connect_to_mongodb():
    client = MongoClient()
    db = client["CookBookie"]
    return db


# Function to insert recipe into MongoDB
def insert_recipe(recipe):
    db = connect_to_mongodb()
    recipes_collection = db["recipes"]

    # Generate a unique ID for the recipe
    recipe_id = str(uuid.uuid4())

    # # Store image URL if uploaded
    # if recipe["image"]:
    #     image_url = f"https://yourdomain.com/images/{recipe_id}.jpg"  # Change to your domain
    # else:
    #     image_url = None

    # Update recipe dictionary with image URL and ID
    recipe.update({"_id": recipe_id})

    # Insert recipe into MongoDB
    recipes_collection.insert_one(recipe)


def app():
    st.title('Your Recipes')

    # Input fields for recipe details
    recipe_name = st.text_input('Recipe Name')
    ingredients = st.text_area('Ingredients (separate with commas)')
    procedure = st.text_area('Procedure')
    serving_size = st.number_input('Serving Size', min_value=1, step=1)
    cuisine_options = ['Italian', 'Mexican', 'Indian', 'Chinese', 'French', 'Other']
    cuisine = st.selectbox('Cuisine', cuisine_options)

    # If "Other" is selected, allow user to input custom cuisine
    if cuisine == 'Other':
        custom_cuisine = st.text_input('Enter Cuisine')
    else:
        custom_cuisine = None

    owner = st.text_input('Your Name')

    # File uploader for recipe image
    uploaded_file = st.file_uploader("Upload Image", type=["jpg", "jpeg", "png"])

    if uploaded_file is not None:
        os.makedirs("uploaded_images",exist_ok=True)
        with open(os.path.join("uploaded_images",uploaded_file.name),"wb") as f:
            f.write(uploaded_file.getbuffer())
    # Submit button
    if st.button('Add Recipe'):
        # Determine cuisine value based on selection
        if cuisine == 'Other':
            cuisine_value = custom_cuisine
        else:
            cuisine_value = cuisine

        # Create recipe dictionary
        recipe = {
            "name": recipe_name,
            "ingredients": [ingredient.strip() for ingredient in ingredients.split(',')],
            "procedure": procedure,
            "serving_size": serving_size,
            "cuisine": cuisine_value,
            "owner": owner,
            "image": uploaded_file.read() if uploaded_file else None  # Read image bytes if uploaded
        }

        # Insert recipe into MongoDB
        insert_recipe(recipe)
        st.success("Recipe added successfully!")


if __name__ == "_main_":
    app()