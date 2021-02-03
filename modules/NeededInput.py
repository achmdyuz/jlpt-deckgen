#!/usr/bin/env python3
#-*- coding: utf-8 -*- # Setup characters encode to "UTF-8"

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
