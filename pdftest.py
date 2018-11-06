#! /usr/bin/env python

import subprocess
import re
from tabula import read_pdf
import pandas

df = read_pdf('USRS - DistrictFW37.pdf', 'multiple_tables = True')
df






'''
output = subprocess.check_output(["less","USRS - DistrictFW37.pdf"])
print(output)


re_data_prefix = re.compile("^[0-9]+[.].*$")
re_data_fields = re.compile("(([^ ]+[ ]?)+)")

for line in output.splitlines():
    print(line)

    if re_data_prefix.match(line):
        print [l[0].strip() for l in re_data_fields.findall(line)]
'''