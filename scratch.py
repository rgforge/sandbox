#! /usr/bin/python3

import re
import textwrap

text_file = open('testtextOct_19.txt', 'r')
file_text = text_file.read()
file_text = textwrap.fill(file_text, 50)#file_text = 'For more than 80 years, Southwestern Energy Company has thrived because of a deep commitment to providing the energy that powers our world. Our success continues to be dependent upon the dedication of our employees to the company and to the communities in which we operate.'
text_file.close()
#lines = re.split(r'\n+', file_text)
substitution = re.sub(r'Southwestern Energy Company has', 'We have', file_text)
take_tags = re.sub(r'<.*>', '', file_text)
output_file = open('out_put.txt', 'w+')
output_file.write(take_tags)
