#!/usr/bin/env python3
#-*- coding: utf-8 -*- # Setup characters encode to "UTF-8"
from bs4 import BeautifulSoup
import requests
import time
import random
import csv

# Creating the main function and call any other needed function
def main():
    get_input()
    get_kanji()
# Scrapping start from here

# Change the function name into "def get_input():
#def kanji_scrapper():
def get_input():
    # Get some data from user
        get_input.jlpt_level = int(input("Enter the JLPT level do you studying (1: hardest, 2, 3, 4, 5: easiest): "))
        get_input.start_page = 0
        get_input.end_page = int(input("How many pages do you want to scrapping? "))
        get_input.tags = "JLPT-N"+str(get_input.jlpt_level)
        temp_filename = str(input("Please enter the CSV filename: "))
        if temp_filename == '':
            get_input.filename = "JLPTN"+str(get_input.jlpt_level)+".csv"
        else:
            get_input.filename = temp_filename


# Change the function name into "get_kanji():"
def get_kanji():
    # Let's do it
    while(get_input.start_page <= get_input.end_page):
    
        source_page = requests.get(f'https://jisho.org/search/%23kanji%20%23jlpt-n{get_input.jlpt_level}?page={get_input.start_page}').text # Mix url source with data from user
        get_input.start_page += 1
        print("Scrapping page : "+str(get_input.start_page))
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
                kun_reading = " "
            else:
                kun_reading = kanji.find('div', class_='kun readings').text.replace('\n', '').strip()
            get_on_reading = kanji.find('div', class_='on readings')
            if get_on_reading is None:
                on_reading = " "
            else:
                on_reading = kanji.find('div', class_='on readings').text.replace('\n', '').strip()
            write_csv(character, meaning, kun_reading, on_reading)   
# Change into "def write_csv():"

# Put everything into CSV file
def write_csv(character, meaning, kun_reading, on_reading):
    with open(f'file_output/{get_input.filename}', 'a') as csv_source:
        csv_writer = csv.writer(csv_source, delimiter=':', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        csv_writer.writerow([character, meaning, kun_reading, on_reading, "Compound 0", "Compound 1", "Compound 2", "Compound 3", "Compound 4", "Sentences example : ", get_input.tags])

if __name__=='__main__':
    main()
    print("All pages scrapped")
