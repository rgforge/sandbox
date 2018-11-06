#! /usr/bin/python3.7

import datetime

time_stamp = (datetime.datetime.now().strftime('%b_%d_%y'))
print(time_stamp)

file_name = 'testfile' + time_stamp + '.txt'

fil = open(file_name,'w+')


fil.close()
