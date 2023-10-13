# -*- coding: utf-8 -*-
"""
Created on Fri Oct 13 13:34:43 2023

@author: dsanm
"""
import streamlit as st
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService
import pandas as pd

#chrome_options = webdriver.ChromeOptions()
#chrome_options.add_argument('--headless')
#chrome_options.add_argument('--window-size=1920x1080')
#chrome_options.add_argument('--disable-gpu')

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

url = 'https://drones.enaire.es/'
driver.get(url)