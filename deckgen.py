#!/usr/bin/env python3
#-*- coding: utf-8 -*- # Setup characters encode to "UTF-8"
from bs4 import BeautifulSoup
import requests
import time
import random

jlpt_level= int(input("Enter the JLPT level do you studying : "))
source_page = requests.get(f'https://jisho.org/search/%23kanji%20%23jlpt-n{jlpt_level}?page=3').text
