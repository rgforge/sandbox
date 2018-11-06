#! /usr/bin/python3

import re

my_string = 'For more than 80 years, Southwestern Energy Company has thrived because of a deep commitment to providing the energy that powers our world. Our success continues to be dependent upon the dedication of our employees to the company and to the communities in which we operate.'
#result = re.findall(r'([A-Z][a-z].*)', my_string)
result = re.split(r'\s+', my_string)

for x in result:
	test = re.findall(r'^[A-Z][a-z].*', x)
	if test:
		print(test)


