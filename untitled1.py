# -*- coding: utf-8 -*-
"""
Created on Fri Oct 13 13:34:43 2023

@author: dsanm
"""
import streamlit as st
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import chromedriver_binary

# Set up Chrome options
chrome_options = Options()
#chrome_options.add_argument("--headless")  # Run Chrome in headless mode

# Create a new Chrome driver instance
driver = webdriver.Chrome(options=chrome_options)

# Use the driver to interact with web pages
driver.get('https://drones.enaire.es/')


