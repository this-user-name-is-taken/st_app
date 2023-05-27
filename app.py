import streamlit as st
import numpy as np
import pandas as pd
from html2image import Html2Image
import folium
from selenium import webdriver
from streamlit_folium import st_folium
st.markdown("""# This is a header
## This is a sub header
This is text""")
# center on Liberty Bell, add marker
map = folium.Map(location=[39.949610, -75.150282], zoom_start=16)
folium.Marker([39.949610, -75.150282], popup="Liberty Bell", tooltip="Liberty Bell").add_to(map)
st_data = st_folium(map, width=725)

hti = Html2Image()
html = map.get_root().render()
hti.screenshot(html_str=html, save_as='page.png)
