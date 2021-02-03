#!/usr/bin/env python3
#-*- coding: utf-8 -*- # Setup characters encode to "UTF-8"
import csv
from pathlib import Path

def write_csv(character, meaning, kun, on, tags, filename):
    path0 = Path('output_file/')
    path0.mkdir(exist_ok=True)
    with open(f'output_file/{filename}', 'a') as csv_source:
        csv_writer = csv.writer(csv_source, delimiter=':', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        csv_writer.writerow([character, meaning, kun, on, tags])
if __name__=='__main__':
    main()
