#!/usr/bin/env python3
#-*- coding: utf-8 -*- # Setup characters encode to "UTF-8"
from bs4 import BeautifulSoup
import requests
import time
import random
import csv

# Scrapping start from here

def kanji_scrapper():
    # Get some data starter from user
    jlpt_level= int(input("Enter the JLPT level do you studying (1: Hardest, 2, 3, 4, 5: Easiest): "))
    start_page = 0
    end_page = int(input("How many page do you want to scrapping? "))
    tags = "JLPT-N"+str(jlpt_level)
    # Let's do it
    while(start_page <= end_page):
    
        source_page = requests.get(f'https://jisho.org/search/%23kanji%20%23jlpt-n{jlpt_level}?page={start_page}').text # Mix url source with data from user
        start_page += 1
        print("Scrapping page : "+str(start_page))
        delay = random.randint(1, 30)
        time.sleep(delay)
        soup = BeautifulSoup(source_page, 'lxml')
    
        #kanji = soup.find("a", attrs={"href":"jisho.org/search/%E6%B0%8F%20%23kanji"}) # This is how to find tag with attributes
    
        kanjis = soup.find_all('div', class_='entry kanji_light clearfix')
        for kanji in kanjis:
    
            character = kanji.find('span', class_='character literal japanese_gothic').text.replace('\n', '').strip()
            meaning = kanji.find('div', class_='meanings english sense').text.replace('\n', '').strip()
            get_kun_reading = kanji.find('div', class_='kun readings')
            if get_kun_reading is None:
                kun_reading = "Kun"
            else:
                kun_reading = kanji.find('div', class_='kun readings').text.replace('\n', '').strip()
            get_on_reading = kanji.find('div', class_='on readings')
            if get_on_reading is None:
                on_reading = "On"
            else:
                on_reading = kanji.find('div', class_='on readings').text.replace('\n', '').strip()
    
    #Everything done, let's start putting all into CSV file
            with open('file_output/JLPTN'+str(jlpt_level)+'.csv', 'a') as csv_source:
                csv_writer = csv.writer(csv_source, delimiter=':', quotechar='"', quoting=csv.QUOTE_MINIMAL)
                csv_writer.writerow([character, meaning, kun_reading, on_reading, "Compound 0", "Compound 1", "Compound 2", "Compound 3", "Compound 4", "Sentences example : ", tags])

if __name__=='__main__':
    kanji_scrapper()
    print("All pages scrapped")
