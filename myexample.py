#! /usr/bin/python3

fil = open('testfile.txt','r')
html_file = open('testhtml.html', 'w+')

if fil.mode == 'r':
	read_lines = fil.readlines()
	for x in read_lines:
		html_file.write('<pre>' + x + '</pre>')


fil.close()
html_file.close()
