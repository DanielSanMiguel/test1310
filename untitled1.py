# -*- coding: utf-8 -*-
"""
Created on Fri Oct 13 13:34:43 2023

@author: dsanm
"""
import streamlit as st
from seleniumbase import Driver
from seleniumbase import BaseCase
from selenium import webdriver

b_1 = st.button('arranca')
if b_1:
    driver = Driver(browser="chrome")
    
    driver.get("https://drones.enaire.es/")


b_2 = st.button('apàga')
if b_2:
    driver.quit()