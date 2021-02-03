#!/usr/bin/env python3
#-*- coding: utf-8 -*- # Setup characters encode to "UTF-8"
from modules.NeededInput import get_input
from modules.Kanji import get_kanji
from modules.Writeit import write_csv

def main():
    for user_input in get_input():
        level = user_input['jlpt_level']
        start = user_input['start']
        end = user_input['end']
        tags = user_input['tags']
        filename = user_input['filename']
        for kanji in get_kanji(level, start, end):
            write_csv(kanji['character'], kanji['meaning'], kanji['kun'], kanji['on'], tags, filename)

if __name__=='__main__':
    main()
