# -*- coding: utf-8 -*-
"""
Created on Fri Oct 13 13:34:43 2023

@author: dsanm
"""
import streamlit as st
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

# Create a new Chrome driver instance
driver = webdriver.Chrome(ChromeDriverManager().install())

# Use the driver to interact with web pages
driver.get('https://drones.enaire.es/')





