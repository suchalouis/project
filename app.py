import streamlit as st

import requests
import streamlit as st
from streamlit_lottie import st_lottie
from PIL import Image


# Find more emojis here: https://www.webfx.com/tools/emoji-cheat-sheet/
st.set_page_config(page_title="My Webpage", page_icon=":tada:", layout="wide")


def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()


# Use local CSS
def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)


local_css("style/style.css")

# ---- LOAD ASSETS ----
lottie_coding = load_lottieurl("https://assets3.lottiefiles.com/packages/lf20_bvxz04bd.json")
transfermarkt_logo = Image.open("images/transfermarkt_logo.png")
Wikipedia_logo = Image.open("images/Wikipedia_logo.png")
FIFA_Logo = Image.open("images/FIFA_Logo.png")
understat_Logo = Image.open("images/logo_understat.png")

# ---- HEADER SECTION ----
with st.container():
    st.title("Welcome in the football recommendation api")
# ---- WHAT I DO ----
with st.container():
    st.write("---")
    left_column, right_column = st.columns(2)
    with left_column:
        st.header("Where the data comes from ?")
        st.write("##")
        st.write(
            """
           This api is based on data that we have collected from 4 different sites 
            """
        )
    with right_column:
        st_lottie(lottie_coding, height=300, key="coding")

# ---- PROJECTS ----
with st.container():
    st.write("---")
    st.header("Where the data comes from ?")
    st.write("This api is based on data that we have collected from 4 different sites ")
    image_column, text_column = st.columns((1, 2))
    with image_column:
        st.image(Wikipedia_logo)
    with text_column:
        st.subheader("Wikipedia")
        st.write(
            """
            for nationality and current number 
            """
        )
        st.markdown("[go to the web site...](https://fr.wikipedia.org/wiki/Wikip%C3%A9dia)")
with st.container():
    image_column, text_column = st.columns((1, 2))
    with image_column:
        st.image(transfermarkt_logo)
    with text_column:
        st.subheader("transfermarkt_logo")
        st.write(
            """
            for the value of the players
            """
        )
        st.markdown("[go to the web site...](https://www.transfermarkt.fr/)")


with st.container():
    image_column, text_column = st.columns((1, 2))
    with image_column:
        st.image(FIFA_Logo)
    with text_column:
        st.subheader("Fifa index ")
        st.write(
            """
            For the marks of the players 
            """
        )
        st.markdown("[go to the web site...](https://www.fifaindex.com/)")

with st.container():
    image_column, text_column = st.columns((1, 2))
    with image_column:
        st.image(understat_Logo)
    with text_column:
        st.subheader("understat")
        st.write(
            """
            To get all the player name of one season and their stats            
            """
        )
        st.markdown("[go to the web site...](https://understat.com)")