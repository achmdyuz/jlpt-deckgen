#!/usr/bin/env python3
#-*- coding: utf-8 -*- # Setup characters encode to "UTF-8"
from deckgen import get_kanji, get_input, write_csv
import time
import random
from tkinter import *
from tkinter import ttk

# Deckgen graphic interface start here
class Window(Tk):
    def __init__(self):
        super(Window, self).__init__()
        self.title("Graphic CSV generator")
        self.minsize(500, 400)

        # Initialize combobox
        self.level_choice()

# Create combobox as input choice for users
    def level_choice(self): 
        self.JLPT = StringVar()
        self.combobox = ttk.Combobox(self, width = 20, textvariable = self.JLPT)
        self.combobox['values'] = ("JLPT-N1", "JLPT-N2", "JLPT-N3", "JLPT-N4", "JLPT-N5")
        self.combobox.grid(column = 1, row = 0)

# Combobox label
        self.label = ttk.Label(self, text = "Select the JLPT level")
        self.label.grid(column = 0, row = 0)

# Combobbox button
        self.button = ttk.Button(self, text = "Scrapping it!", command = self.scrapping_it)
        self.button.grid(column = 2, row = 0)

# Combobox action
    def scrapping_it(self):
        self.label.configure(text = "Test success!")
        self.label.configure(text = self.JLPT.get()+" Scrapped")

# Main loop 
window = Window()
window.mainloop()
