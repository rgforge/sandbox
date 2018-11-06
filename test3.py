#! /usr/bin/python

import cv2

while True:
    k = cv2.waitKey(1) & 0xFF
    # press 'q' to exit
    if k == ord('q'):
        break
    else:
    	x = 0
    	while x >= 0:
        	print (x)
        	x += 1