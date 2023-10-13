# -*- coding: utf-8 -*-
"""
Created on Fri Oct 13 13:34:43 2023

@author: dsanm
"""
import streamlit as st

from seleniumbase import BaseCase
from selenium import webdriver

class MyTest(BaseCase):
    def test_open_browser(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://drones.enaire.es/")



if __name__ == "__main__":
    MyTest().main()


