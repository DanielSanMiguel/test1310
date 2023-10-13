# -*- coding: utf-8 -*-
"""
Created on Fri Oct 13 13:34:43 2023

@author: dsanm
"""

import streamlit as st
from selenium import webdriver

# Inicializa el navegador web
driver = webdriver.Chrome()  # Cambia a webdriver.Firefox() si estás usando Firefox
st.title("Automatizando un navegador con Selenium en Streamlit")
driver.get("https://drones.enaire.es/")
