#!/usr/bin/env python3
#-*- coding: utf-8 -*- # Setup characters encode to "UTF-8"
from bs4 import BeautifulSoup
import requests
import time
import random


def get_kanji(level, start, end):
    while(start <= end):
        url = (f'https://jisho.org/search/%23kanji%20%23jlpt-n{level}?page={start}')
        source_page = requests.get(url).text
        start += 1
        print(f'Scrapping page: {str(start)}')
        delay = random.randint(1, 15)
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
            yield {'character': character,
                   'meaning': meaning,
                   'kun': kun_reading,
                   'on': on_reading}


if __name__ == '__main__':
    for test_kanji in get_kanji(5, 0, 1):
        print(test_kanji['character'])
