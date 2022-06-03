import streamlit as st
import requests
import pandas as pd
import numpy as np
from streamlit_folium import folium_static
import folium
from folium.plugins import MousePosition
from streamlit_folium import folium_static
import joblib



st.set_page_config(
    page_title="Real Estate Tracker", # => Quick reference - Streamlit
    page_icon="🗺",
    layout="centered", # wide
    initial_sidebar_state="auto")

CSS = """
h1 {
    color: white;
    text-align: center;
}

h2 {color: white;
    text-align: center;}
h3 {color: white;
    text-align: center;}
p {color: white;
    text-align: center;}


.stApp {
    background-image: linear-gradient(to bottom, rgba(153, 153, 153, 0.52), rgba(153, 153, 153, 0.52)), url(https://images.unsplash.com/photo-1516156008625-3a9d6067fab5?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=2070&q=80);
    background-size: cover;

}
"""


st.write(f'<style>{CSS}</style>', unsafe_allow_html=True)


'''
# Real Estate Tracker
'''

st.markdown('''
Remember that there are several ways to output content into your web page...
''')

'''
## Your dream house is waiting for you...

Enter your preference and look for opportunities
'''

'''## Select a neighborhood ##'''

df = ['Chamberí', 'Retiro', 'Carabanchel', 'Villa de Vallecas', 'Centro',
       'Tetuán', 'Puente de Vallecas', 'Barrio de Salamanca', 'Chamartín',
       'Usera', 'Moncloa - Aravaca', 'Ciudad Lineal', 'Arganzuela',
       'Fuencarral - El Pardo', 'Villaverde', 'Latina', 'Moratalaz',
       'Vicálvaro', 'Barajas', 'Hortaleza', 'Madrid Capital', 'San Blas']

neighborhood = st.selectbox('', df)

# st.write(neighborhood)

"""## Enter rooms number ##"""

pick_rooms = st.slider('', 0, 6, 1)

ColorMinMax = st.markdown(''' <style> div.stSlider > div[data-baseweb = "slider"] > div[data-testid="stTickBar"] > div {
    background: rgb(0 0 0 / 0%); } </style>''', unsafe_allow_html = True)


Slider_Cursor = st.markdown(''' <style> div.stSlider > div[data-baseweb="slider"] > div > div > div[role="slider"]{
    background-color: rgb(255, 250, 250); box-shadow: rgb(14 38 74 / 20%) 0px 0px 0px 0.2rem;} </style>''', unsafe_allow_html = True)


Slider_Number = st.markdown(''' <style> div.stSlider > div[data-baseweb="slider"] > div > div > div > div
                                { color: rgb(255, 250, 250); } </style>''', unsafe_allow_html = True)


col = f''' <style> div.stSlider > div[data-baseweb = "slider"] > div > div {{
    background: linear-gradient(to right, rgb(255, 250, 250) 100%,
                                rgb(1, 183, 158) {pick_rooms}%,
                                rgba(151, 166, 195, 0.25) {pick_rooms}%,
                                rgba(151, 166, 195, 0.25) 100%); }} </style>'''

ColorSlider = st.markdown(col, unsafe_allow_html = True)

# st.write(pick_rooms)

"""## Enter the surface ##"""

surface = st.number_input("", min_value=20, max_value=None, value=50, step=1)

# st.write('The current number is ', surface)

'''## Select the type of property ##'''

df1 = ['Piso', 'Dúplex', 'Apartamento', 'Ático', 'Loft', 'Planta baja',
       'Finca rústica', 'Estudio', 'Casa adosada', 'Casa o chalet']

df1_eng = {'Piso':'Flat',
           'Dúplex':'Duplex',
           'Apartamento':'Apartment',
           'Ático':'Attic',
           'Loft':'Loft',
           'Planta baja':'Ground floor',
           'Finca rústica':'Rural property',
           'Estudio':'Study',
           'Casa adosada':'Single-family semi-detached',
           'Casa o chalet':'House or chalet'}

df1_trans = {"Flat": "Piso",
            "Duplex": "Dúplex",
            "Apartment": "Apartamento",
            "Attic": "Ático",
            "Loft": "Loft",
            "Ground floor": "Planta baja",
            "Rural property": "Finca rústica",
            "Study": "Estudio",
            "Single-family semi-detached": "Casa adosada",
            "House or chalet": "Casa o chalet"}

type = st.selectbox("", df1_eng.values())

"""
"""
col1, col2, col3 , col4, col5 = st.columns(5)


param = {"pick_rooms": pick_rooms,
         "surface": surface,
         "neighborhood": neighborhood,
         'type': df1_trans[type]}

param = pd.DataFrame(param, index=[0]).rename(columns={"pick_rooms":"rooms",
                                                "surface": "surface",
                                                "neighborhood": "neighborhood",
                                                "type": "nhousetype"})

potato = joblib.load("model.joblib")
pred = round(potato.predict(param)[0], 0)

final_pred = f"With the given characteristics, the market price is between {pred * 0.95} and {pred * 1.05}"

if col3.button("Click me"):
    st.balloons()
    #st.write(final_pred)
    new_title = f'<p style="font-family:; color:White; font-size: 32px;">{final_pred}</p>'
    st.markdown(new_title, unsafe_allow_html=True)
# [[param["pick_rooms"], param["surface"], param["neighborhood"], param["type"]]]
