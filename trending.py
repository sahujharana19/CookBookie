import streamlit as st
from pymongo import MongoClient
from PIL import Image
from io import BytesIO

# Function to connect to MongoDB
def connect_to_mongodb():
    client = MongoClient()
    db = client["CookBookie"]
    return db

# Function to fetch most viewed recipes from MongoDB
def fetch_most_viewed_recipes(limit=5):
    db = connect_to_mongodb()
    recipes_collection = db["recipes"]
    results = recipes_collection.find().sort("views", -1).limit(limit)
    return results

def app():
    st.title('Trending')

    # Fetch most viewed recipes
    trending_recipes = fetch_most_viewed_recipes()

    # Display trending recipes
    if trending_recipes:
        for recipe in trending_recipes:
            st.subheader(recipe['name'])
            st.write(f"Ingredients: {', '.join(recipe.get('ingredients', []))}")
            st.write(f"Cuisine: {recipe.get('cuisine', '')}")

            # Check if image data is available
            if 'image_data' in recipe:
                # Convert binary image data to Image object
                image = Image.open(BytesIO(recipe['image_data']))
                st.image(image, caption='Recipe Image', use_column_width=True)
            else:
                st.write("Image not available")

            st.write(f"Preparation: {recipe.get('procedure', '')}")
            st.write(f"Serving Size: {recipe.get('serving_size', '')}")
            st.write(f"Owner: {recipe.get('owner', '')}")
            st.write("---")
    else:
        st.write("No trending recipes found.")

if __name__ == "_main_":
    app()