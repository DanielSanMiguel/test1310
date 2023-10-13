# -*- coding: utf-8 -*-
"""
Created on Fri Oct 13 13:34:43 2023

@author: dsanm
"""
import streamlit as st
from selenium import webdriver

options = webdriver.ChromeOptions()
st.write(options.to_capabilities())





