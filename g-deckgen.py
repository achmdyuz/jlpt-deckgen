#!/usr/bin/env python3
#-*- coding: utf-8 -*- # Setup characters encode to "UTF-8"
import tkinter
from tkinter import ttk
from modules.Kanji import get_kanji
from modules.Writeit import write_csv

def scrapping():
    level = jlptchoosen.get()[6]
    if level == '1':
        level = int(level) 
        start = int('0')
        end = int('64')
        tags = 'JLPT-N'+str(level)
        filename = 'JLPT-N'+str(level)+'.csv'
        for kanji in get_kanji(level, start, end):
            write_csv(kanji['character'], kanji['meaning'], kanji['kun'], kanji['on'], tags, filename)
    elif level == '2':
        level = int(level) 
        start = int('0')
        end = int('21')
        tags = 'JLPT-N'+str(level)
        filename = 'JLPT-N'+str(level)+'.csv'
        for kanji in get_kanji(level, start, end):
            write_csv(kanji['character'], kanji['meaning'], kanji['kun'], kanji['on'], tags, filename)
    elif level == '3':
        level = int(level) 
        start = int('0')
        end = int('21')
        tags = 'JLPT-N'+str(level)
        filename = 'JLPT-N'+str(level)+'.csv'
        for kanji in get_kanji(level, start, end):
            write_csv(kanji['character'], kanji['meaning'], kanji['kun'], kanji['on'], tags, filename)
    elif level == '4':
        level = int(level) 
        start = int('0')
        end = int('12')
        tags = 'JLPT-N'+str(level)
        filename = 'JLPT-N'+str(level)+'.csv'
        for kanji in get_kanji(level, start, end):
            write_csv(kanji['character'], kanji['meaning'], kanji['kun'], kanji['on'], tags, filename)
    elif level == '5':
        level = int(level) 
        start = int('0')
        end = int('7')
        tags = 'JLPT-N'+str(level)
        filename = 'JLPT-N'+str(level)+'.csv'
        for kanji in get_kanji(level, start, end):
            write_csv(kanji['character'], kanji['meaning'], kanji['kun'], kanji['on'], tags, filename)
    else:
        print("Invalid choice")
# Main window
window = tkinter.Tk()
window.title("Anki CSV Deck Generator")

# Widgets

# Combobox
ttk.Label(window, text = "Select the JLPT level :")
select = tkinter.StringVar()
jlptchoosen = ttk.Combobox(window, width = 35, textvariable = select)
jlptchoosen['values'] = ('JLPT-N1',
                         'JLPT-N2',
                         'JLPT-N3',
                         'JLPT-N4',
                         'JLPT-N5')
jlptchoosen.pack()

# JLPT-N5 as a default value
jlptchoosen.current(4)

# Button
clickthis = tkinter.Button(text = "Scrap it", width = 7, height = 2, command = scrapping)
clickthis.pack()

# Main window loop
window.mainloop()
