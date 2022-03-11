# This is a sample Python script.

import urllib.request
import xml.etree.ElementTree as ET
import csv

csv_file = open('facts_and_figures.csv', 'a+', encoding="utf-8", newline='')
csv_writer = csv.writer(csv_file)
f = urllib.request.urlopen('https://en.wikipedia.org/wiki/Road_safety_in_Europe')
x = f.read().decode('utf-8')
data = ET.fromstring(x)
first_list = []
for value in data.findall('.//*[@class="wikitable sortable"]//tr'):
    new_list = []
    for val in value.findall('.//'):
        try:
            new_list.append(val.text.strip())
        except AttributeError:
            pass
    csv_writer.writerow(new_list)