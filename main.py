import streamlit as st
from streamlit_option_menu import option_menu

import about, account, home, trending, your_receipes

st.set_page_config(
    page_title="CookBookie"
)

class MultiApp:

    def __init__(self):
        self.apps = []

    def add_app(self, title, function):
        self.apps.append({
            "title": title,
            "function": function
        })

    def run(self):
        with st.sidebar:
            app = option_menu(
                menu_title='CookBookie',
                options=['Home', 'Account', 'Trending', 'Your Recipes', 'About'],
                icons=['house-fill', 'person-circle', 'trophy-fill', 'chat-fill', 'info-circle-fill'],
                menu_icon='chat-text-fill',
                default_index=1,
                styles={
                    "container": {"padding": "5!important", "background": "grey"},
                    "icon": {"color": "white", "font-size": "23px"},
                    "nav-link": {"color": "white", "font-size": "20px", "text-align": "left", "margin": "0px"},
                    "nav-link-selected": {"background-color": "#02ab21"},
                }
            )

        if app == 'Home':
            home.app()
        elif app == 'Account':
            account.app()
        elif app == 'About':
            about.app()
        elif app == 'Trending':
            trending.app()
        elif app == 'Your Recipes':
            your_receipes.app()

# Create an instance of MultiApp and run it
app = MultiApp()
app.run()