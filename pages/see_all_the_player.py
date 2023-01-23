import requests
import streamlit as st
from streamlit_lottie import st_lottie
from PIL import Image
import streamlit_pandas as sp
import pandas as pd 

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



df=pd.read_csv("data/dfApp.csv")
df=df.drop('Unnamed: 0', axis=1)


create_data = { "team_title": "multiselect",
                "Poste": "multiselect",
                'Nationalite' : 'multiselect'
                }

ignore_cols=['player_international', 'number',
       'mois_de_naissance', 'jour_de_naissance', 'anne_de_naissance',
       'age_actuel', 'taille_en_m', 'Pied_fort', 'id',
       'time', 'goals', 'xG', 'assists', 'xA', 'shots', 'key_passes',
       'yellow_cards', 'red_cards', 'position', 'npg', 'npxG',
       'xGChain', 'xGBuildup', 'Dribbling', 'Marking', 'Aggression',
       'Reactions', 'Interceptions', 'Vision', 'Composure', 'Crossing',
       'Acceleration', 'Strength', 'Agility', 'Penalties', 'Volleys', 'Power',
       'Jumping', 'Heading', 'Curve', 'Injury', 'Finishing', 'value',
       'dateDeNaissance', 'Pied_fort_cat', 'value_int', 'poste_cat',
       'power_cat', 'poste_group']

all_widgets = sp.create_widgets(df.astype(str), create_data, ignore_columns=ignore_cols)

cols_fiche_joueur=['id','player_name','Nationalite','dateDeNaissance',"Poste",'team_title', 'number', "poste_group", "value"]

features=['player_name','player_international', 'age_actuel', 'taille_en_m', 'poste_cat', 'time', 'goals', 'xG',
       'assists', 'xA', 'shots', 'key_passes', 'yellow_cards', 'red_cards','npg', 'npxG', 'xGChain', 'xGBuildup',
       'Dribbling', 'Aggression', 'Reactions', 'Interceptions', 'Vision','Composure', 'Crossing', 'Acceleration', 'Strength', 'Agility',
       'Penalties', 'Volleys', 'Jumping', 'Heading', 'Curve','Finishing', 'power_cat', 'value_int']

res = sp.filter_df(pd.DataFrame(df,columns=cols_fiche_joueur), all_widgets)
st.title("All players")

#st.header("Result DataFrame")
st.write(res)




