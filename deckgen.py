#!/usr/bin/env python3
#-*- coding: utf-8 -*- # Setup characters encode to "UTF-8"
from bs4 import BeautifulSoup
import requests
import time
import random
import csv

# Declare the main function and call other function from here 
def main():
    get_input()

# Scrapping start from here
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

        get_kanji(jlpt_level = get_input.jlpt_level, start_page = get_input.start_page, end_page = get_input.end_page) 
def get_kanji(jlpt_level, start_page, end_page):
    # Get kanji, meaning, and reading from jisho with user input as parameter
    while(start_page <= end_page):
    
        source_page = requests.get(f'https://jisho.org/search/%23kanji%20%23jlpt-n{jlpt_level}?page={start_page}').text # Mix url source with data from user
        start_page += 1
        print("Scrapping page : "+str(start_page))
        delay = random.randint(1, 5)
        time.sleep(delay)
        soup = BeautifulSoup(source_page, 'lxml')
    
        #kanji = soup.find("a", attrs={"href":"jisho.org/search/%E6%B0%8F%20%23kanji"}) # This is how to find tag with attributes

        # Output filename will be have name from variable below
        nametag = "JLPT-N"+str(jlpt_level)
        
    
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
            write_csv(character, meaning, kun_reading, on_reading, tags = nametag, this_file = nametag)

# Put everything into CSV file
def write_csv(character, meaning, kun_reading, on_reading, tags, this_file):
    ''' This function used by script for writing csv file after receive all the data needed from get_kanji function'''
    ''' To using this functon, call this function with parameter like this : write_dev(character, meaning, kun_reading, on_reading, tags, this_file) '''
    with open(f'file_output/{this_file+".csv"}', 'a') as csv_source:
        csv_writer = csv.writer(csv_source, delimiter=':', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        csv_writer.writerow([character, meaning, kun_reading, on_reading, "Compound 0", "Compound 1", "Compound 2", "Compound 3", "Compound 4", "Sentences example : ", tags])
if __name__=='__main__':
    main()
