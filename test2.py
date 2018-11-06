#! /usr/bin/python3.7

import threading

def input_thread(a_list):
    input()
    a_list.append(True)

def do_stuff():
    a_list = []
    threading.start_new_thread(input_thread, (a_list,))
    while not a_list:
    	x = 0
    	while x >= 0:
        	print (x)
        	x += 1

do_stuff