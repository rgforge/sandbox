#! /usr/bin/python3.7

'''
from bs4 import BeautifulSoup
from urllib.request import urlopen
import csv

url = 'http://www.data.jma.go.jp/obd/stats/etrn/view/monthly_s3_en.php?block_no=47401&view=1'
html = urlopen(url)
soup = BeautifulSoup(html, 'html.parser')
table = soup.select_one("table.data2_s")
# python3 just use th.text
headers = [th.text for th in table.select("tr th")]

with open("out.csv", "w") as f:
    wr = csv.writer(f)
    wr.writerow(headers)
    wr.writerows([[td.text for td in row.find_all("td")] for row in table.select("tr + tr")])

'''
#! /usr/bin/python3.7
from bs4 import BeautifulSoup
from urllib.request import urlopen
import csv

url = 'https://en.wikipedia.org/wiki/List_of_counties_in_Texas'
html = urlopen(url)
soup = BeautifulSoup(html, 'html.parser')
all_table = soup.find_all('table')
table = soup.find('table', class_ = 'wikitable sortable')
headers = [th.text for th in table.select('tr th')]



with open('outtest.csv', 'w') as f:
	wr = csv.writer(f)
	wr.writerow(headers)
	wr.writerows([[td.text for td in row.find_all('td')] for row in table.select('tr + tr')])

