import streamlit as st
import requests
import pandas as pd
import numpy as np
from streamlit_folium import folium_static
import folium
from folium.plugins import MousePosition
from streamlit_folium import folium_static
import os

CSS = """
h1 {
    color: white;
}

h2 {color: white;}
h3 {color: white;}

.stApp {
    background: transparent\0.1;
    background:rgba(0,0,0,0.4);
    background-image: url(https://images.unsplash.com/photo-1516156008625-3a9d6067fab5?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=2070&q=80);
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

neighborhood = st.selectbox('Select a line to filter', df)

st.write(neighborhood)

"""## Enter rooms number ##"""

pick_rooms = st.slider('Select a modulus', 0, 6, 1)

st.write(pick_rooms)

"""## Enter the surface ##"""
"""  We look around the value that you enter """

surface = st.number_input('Insert a number', min_value=20, max_value=None, value=50, step=1)

st.write('The current number is ', surface)

'''## Select the type of property ##'''

df = ['Piso', 'Dúplex', 'Apartamento', 'Ático', 'Loft', 'Planta baja',
       'Finca rústica', 'Estudio', 'Casa adosada', 'Casa o chalet']

type = st.selectbox('Select a line to filter', df)

st.write(type)

# """## drop longitude ##"""

# drop_long = st.slider('Select a modulus', -74.4, -72.91)

# st.write(drop_long)

# """## drop latitude ##"""

# drop_lat = st.slider('Select a modulus', 40.0, 42.1)

# st.write(drop_lat)

# '''## dropout adresse ##'''
# drop_addresse = st.text_input("drop_addresse")
# st.write(drop_addresse)

# '''## passager count ##'''

# pass_count = st.selectbox('Select a line to filter', list(range(1,9)))

# st.write(pass_count)

# '''## select point in map ##'''
# def get_coord(adresse):
#     url_map = 'https://nominatim.openstreetmap.org/search'

#     param_map = {"q": adresse,
#              "format": "json"}

#     response_map = requests.get(url_map, params=param_map).json()

#     return response_map[0]["lat"], response_map[0]["lon"]

# pick_lat, pick_long = get_coord(pick_addresse)
# drop_lat, drop_long = get_coord(drop_addresse)

# '''## Here is your pick and drop location ##'''


# def get_map_data():

#     return pd.DataFrame(
#             [[float(pick_lat), float(pick_long)], [float(drop_lat), float(drop_long)]],
#             columns=['lat', 'lon']
#         )

# df = get_map_data()

# st.map(df)


# '''

# 2. Let's build a dictionary containing the parameters for our API...
# '''



param = {"neighborhood": neighborhood,
         "pick_rooms": pick_rooms,
         "surface": surface,
         'type': type}

# '''

# 3. Let's call our API using the `requests` package... '''

# url = 'https://taxifare.lewagon.ai/predict'

# response = requests.get(url, params=param).json()

# price = round(response["fare"],2)

# st.write("# The price is: ", price)
