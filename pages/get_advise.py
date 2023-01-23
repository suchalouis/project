import streamlit as st
import pandas as pd 
import streamlit_pandas as sp

# Use local CSS
def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)


local_css("style/style.css")


df=pd.read_csv("data/dfApp.csv")
dfGK_Indices=pd.read_csv("data/dfApp_GK.csv")
dfGK_Indices=dfGK_Indices.set_index('id')
dfRest_Indices=pd.read_csv("data/dfApp_Rest.csv")
dfRest_Indices=dfRest_Indices.set_index('id')



### FUNCTIONS
def value_player(x):
    return df[df['id']==x]['value'].iloc[0]

def value_player_1(x):
    return df[df['id']==x]['Dribbling'].iloc[0]

def value_player_2(x):
    return df[df['id']==x]['xGChain'].iloc[0]

def value_player_3(x):
    return df[df['id']==x]['Finishing'].iloc[0]

def value_player_4(x):
    return df[df['id']==x]['Interceptions'].iloc[0]

def value_player_5(x):
    return df[df['id']==x]['xG'].iloc[0]

def value_player_6(x):
    return df[df['id']==x]['player_name'].iloc[0]


def get_suggestion_v2(name):
    ind=df[df["player_name"]==name]['id'].iloc[0]
    if df[df["player_name"]==name]["Poste"].iloc[0]!="Gardien de but":
        #work with Rest dataset
        nbrs_list=dfRest_Indices.loc[ind]
        dff=pd.DataFrame(nbrs_list)
        dff.columns=["nbrs"]
        dff["player_name"]=dff['nbrs'].apply(value_player_6)
        dff["value"]=dff['nbrs'].apply(value_player)
        dff["Dribbling"]=dff['nbrs'].apply(value_player_1)
        dff["xGChain"]=dff['nbrs'].apply(value_player_2)
        dff["Finishing"]=dff['nbrs'].apply(value_player_3)
        dff["Interceptions"]=dff['nbrs'].apply(value_player_4)
        dff["xG"]=dff['nbrs'].apply(value_player_5)
        
    
    else:
        nbrs_list=dfGK_Indices.loc[1670]
        dff=pd.DataFrame(nbrs_list)
        dff.columns=["nbrs"]
        dff["value"]=dff['nbrs'].apply(value_player)
        dff["player_name"]=dff['nbrs'].apply(value_player_6)

    output=df[df["player_name"]==name], dff.drop('nbrs', axis=1)
    return output

def test(x):
    return f"{x}fdff"

### END FUNCTIONS

create_data = { "player_Name": "text"}
ignore_cols=['Unnamed: 0', 'player_international', 'number', 'Nationalite',
       'mois_de_naissance', 'jour_de_naissance', 'anne_de_naissance',
       'age_actuel', 'taille_en_m', 'Poste', 'Pied_fort', 'id',
       'time', 'goals', 'xG', 'assists', 'xA', 'shots', 'key_passes',
       'yellow_cards', 'red_cards', 'position', 'team_title', 'npg', 'npxG',
       'xGChain', 'xGBuildup', 'Dribbling', 'Marking', 'Aggression',
       'Reactions', 'Interceptions', 'Vision', 'Composure', 'Crossing',
       'Acceleration', 'Strength', 'Agility', 'Penalties', 'Volleys', 'Power',
       'Jumping', 'Heading', 'Curve', 'Injury', 'Finishing', 'value',
       'dateDeNaissance', 'Pied_fort_cat', 'value_int', 'poste_cat',
       'power_cat', 'poste_group']

all_widgets = sp.create_widgets(df.astype(str), create_data, ignore_columns=ignore_cols)

res = sp.filter_df(df, all_widgets)

if(len(res)==1): # if a player is selected 
    name=res['player_name'].iloc[0]
    st.header(f"{name}")

    st.subheader("Etat Civil")
    st.write(f"Nationalité: {get_suggestion_v2(name)[0]['Nationalite'].iloc[0]}")
    st.write(f"Team: {get_suggestion_v2(name)[0]['team_title'].iloc[0]}")
    st.write(f"Number: {get_suggestion_v2(name)[0]['number'].iloc[0]}")
    st.write(f"Poste: {get_suggestion_v2(name)[0]['Poste'].iloc[0]}")
    st.write(f"Valeur sur le marché: {get_suggestion_v2(name)[0]['value'].iloc[0]}")

    st.subheader("Attribus")
    topVar=['Dribbling','xGChain','Finishing','Interceptions','xG']
    st.write(pd.DataFrame(get_suggestion_v2(name)[0], columns=topVar))



    st.header(f"Similar players:")
    st.write(get_suggestion_v2(name)[1])

else:
    st.header('Select a player') 

with st.container():
    st.write("---")
    st.header("Sent the result by mail ")
    st.write("##")

    # Documention: https://formsubmit.co/ !!! CHANGE EMAIL ADDRESS !!!
    contact_form = """
    <form action="https://formsubmit.co/foot.api.project.pleasenoanswer@gmail.com" method="POST">
        <input type="hidden" name="_captcha" value="false">
        <input type="text" name="name" placeholder="Your name" required>
        <input type="email" name="email" placeholder="Your email" required>
        <textarea name="message" placeholder="Your message here" required></textarea>
        <button type="submit">Send</button>
    </form>
    """
    left_column, right_column = st.columns(2)
    with left_column:
        st.markdown(contact_form, unsafe_allow_html=True)
    with right_column:
        st.empty()