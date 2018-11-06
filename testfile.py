#! /usr/bin/python3

import datetime
from bs4 import BeautifulSoup
from urllib.request import urlopen
import re

current_time = (datetime.datetime.now().strftime('%b_%d_%y'))
text_file = ('testtext' + current_time + '.txt')
url = 'https://www.swn.com/aboutswn/pages/ourprofile.aspx'
html = urlopen(url)
soup = BeautifulSoup(html, 'html.parser')
pattern = re.compile(r'^[A-Z][a-z].*')
span_tag = soup.find('span', class_ = 'swn-paragraph')
span_tag = (span_tag.prettify())
output_file = open('output.txt', 'w+')

with open(text_file, 'w+') as file:
	file.write(span_tag)
	
with open(text_file, 'r') as file:
	content = file.read()
	lines = re.split(r'\s+', content)
	for x in lines:
		word = pattern.search(x)
		if word:
			x = x + '\n'
			output_file.write(x)
			
