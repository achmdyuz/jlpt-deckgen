#!/usr/bin/env python3
#-*- coding: utf-8 -*- # Setup characters encode to "UTF-8"
from bs4 import BeautifulSoup
import requests
import time
import random
import csv

def main():
    for user_input in get_input():
        level = user_input['jlpt_level']
        start = user_input['start']
        end = user_input['end']
        tags = user_input['tags']
        filename = user_input['filename']
        for kanji in get_kanji(level, start, end):
            write_csv(kanji['character'], kanji['meaning'], kanji['kun'], kanji['on'], tags, filename)


def get_input():
    jlpt_level = int(input("Choose your JLPT level between 1 and 5 (E.g : enter 1 for JLPT-N1) "))
    start_page = int(input("Enter first page you want to scrapping "))
    end_page = int(input("Enter last page you want to scrapping "))
    temp_filename = str(input("Please enter the output filename "))
    if temp_filename == '':
        filename = "JLPT-N"+str(jlpt_level)+".csv"
    else:
        filename = temp_filename+".csv"
    temp_tags = str(input("Please enter the tag label of the Anki decks "))
    if temp_tags == '':
        tags = "JLPT-N"+str(jlpt_level)
    else:
        tags = temp_tags

    dict_input = {'jlpt_level':jlpt_level, 'start':start_page, 'end':end_page, 'tags':tags,'filename':filename}
    yield dict_input

def get_kanji(level, start, end):
    while(start <= end):
        source_page = requests.get(f'https://jisho.org/search/%23kanji%20%23jlpt-n{level}?page={start}').text
        start += 1
        print(f'Scrapping page: {str(start)}')
        delay = random.randint(1, 5)
        time.sleep(delay)
        soup = BeautifulSoup(source_page, 'lxml')

        get_kanji = soup.find_all('div', class_='entry kanji_light clearfix')
        for kanji in get_kanji:
            character = kanji.find('span', class_='character literal japanese_gothic').text.replace('\n', '').strip()
            meaning = kanji.find('div', class_='meanings english sense').text.replace('\n', '').strip()
            get_kun_reading = kanji.find('div', class_='kun readings')
            if get_kun_reading is None:
                kun_reading = ''
            else:
                kun_reading = kanji.find('div', class_='kun readings').text.replace('\n', '').strip()
            get_on_reading = kanji.find('div', class_='on readings')
            if get_on_reading is None:
                on_reading = ''
            else:
                on_reading = kanji.find('div', class_='on readings').text.replace('\n', '').strip()
            yield {'character':character, 'meaning':meaning,'kun':kun_reading, 'on':on_reading}

def write_csv(character, meaning, kun, on, tags, filename):
    with open(f'output_file/{filename}', 'a') as csv_source:
        csv_writer = csv.writer(csv_source, delimiter=':', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        csv_writer.writerow([character, meaning, kun, on, tags])
if __name__=='__main__':
    main()
