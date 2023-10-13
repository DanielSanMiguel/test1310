# -*- coding: utf-8 -*-
"""
Created on Fri Oct 13 13:34:43 2023

@author: dsanm
"""
import streamlit as st

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

@st.cache_data
def get_driver():
    return webdriver.Chrome(service=Service(ChromeDriverManager().install()))


driver = get_driver()
driver.get('https://drones.enaire.es/')

st.code(driver.page_source)


# Use the driver to interact with web pages


