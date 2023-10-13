# -*- coding: utf-8 -*-
"""
Created on Fri Oct 13 13:34:43 2023

@author: dsanm
"""
import streamlit as st
from seleniumbase import DriverContext
from seleniumbase import BaseCase
from selenium import webdriver
with DriverContext(browser="chrome", incognito=True) as driver:
    driver.open("drones.enaire.es/")
