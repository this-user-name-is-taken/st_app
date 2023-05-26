import streamlit as st
import numpy as np
import pandas as pd
import time
import os
# import json
# import io
import folium
from selenium import webdriver
from streamlit_folium import st_folium
st.markdown("""# This is a header
## This is a sub header
This is text""")
# center on Liberty Bell, add marker
m = folium.Map(location=[39.949610, -75.150282], zoom_start=16)
folium.Marker(
[39.949610, -75.150282], popup="Liberty Bell", tooltip="Liberty Bell"
).add_to(m)
st_data = st_folium(m, width=725)
html = m.get_root().render()
fName='map.html'
m.save(fName)
mUrl= f'file:///map/{fName}'
driver = webdriver.Chrome()
driver.get(mUrl)
time.sleep(2)
driver.save_screenshot('output.png')
driver.quit()
