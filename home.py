import streamlit as st
from pymongo import MongoClient
from PIL import Image, UnidentifiedImageError
import io

# Function to connect to MongoDB
def connect_to_mongodb():
    client = MongoClient()  # Replace with your MongoDB connection string
    db = client["CookBookie"]  # Replace with your database name
    return db

# Function to search recipes in MongoDB based on query
def search_recipes(query):
    db = connect_to_mongodb()
    recipes_collection = db["recipes"]
    results = recipes_collection.find({
        "$or": [
            {"name": {"$regex": query, "$options": "i"}},
            {"ingredients": {"$regex": query, "$options": "i"}},
            {"cuisine": {"$regex": query, "$options": "i"}}
        ]
    })
    return results

def app():
    st.title('Home')

    # Search bar for user input
    search_query = st.text_input("Search for recipes by ingredients or cuisine:")

    # Perform search when user submits the query
    if st.button("Search"):
        search_results = search_recipes(search_query)

        # Display search results
        if search_results:
            st.write("Search Results:")
            for result in search_results:
                st.subheader(result['name'])
                st.write(f"Ingredients: {', '.join(result.get('ingredients', []))}")
                st.write(f"Cuisine: {result.get('cuisine', '')}")

                # Convert image data from MongoDB to displayable format
                if 'image' in result:
                    try:
                        image = Image.open(io.BytesIO(result['image']))
                        st.image(image, caption='Recipe Image', use_column_width=True)
                    except UnidentifiedImageError:
                        st.write("Error: Unable to load image.")
                else:
                    st.write("No image available")

                st.write(f"Preparation: {result.get('procedure', '')}")
                st.write(f"Serving Size: {result.get('serving_size', '')}")
                st.write(f"Owner: {result.get('owner', '')}")
                st.write("---")
        else:
            st.write("No recipes found matching the search criteria.")

if __name__ == "_main_":
    app()