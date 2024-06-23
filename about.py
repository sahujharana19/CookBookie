import streamlit as st
def app():
    st.title('About')

    # Motto of the website
    st.header('Motto:')
    st.write("Bringing Flavor to Your Fingertips: Explore, Create, and Share Delicious Recipes!")

    # Information about the creators
    st.header('Creators Information:')
    st.write("Here is some information about the creators:")

    # Creator 1
    st.subheader('Developer 1')
    st.write("Name:jharana sahu")
    st.write("Role: Developer")

    # Displaying image alongside text
    col1, col2 = st.columns([4, 1])  # Adjust the column width ratio as needed

    # Resize image and display it in column 1
    with col2:
        st.image("jharana.jpg", caption="Jharana sahu", use_column_width=True)

    # Display text in column 2
    with col1:
        st.write("Additional information about jharana sahu goes here.")

    # Creator 2
    st.subheader('Developer 2')
    st.write("Name: jami manasa")
    st.write("Role: Developer")

    # Displaying image alongside text
    col1, col2 = st.columns([4, 1])  # Adjust the column width ratio as needed

    # Resize image and display it in column 1
    with col2:
        st.image("manasa.jpg", caption="Jami manasa", use_column_width=True)

    # Display text in column 2
    with col1:
        st.write("Additional information about Jami manasa goes here.")


if __name__ == "_main_":
    app()