#!usr/bin/env python
# -*- coding: utf-8 -*-

import urllib2
from bs4 import BeautifulSoup
"""
	Part II ­ Stock Data
	Author: Rickardo Henry
"""
url = "http://finance.yahoo.com/q/hp?s=AAPL+Historical+Prices"
page = urllib2.urlopen(url)
soup = BeautifulSoup(page.read(), 'lxml')

#table = soup.findAll("table")
#print table[7]

trs = soup.find_all('tr')



for tr in trs:

    tds = tr.find_all("td")



    for link in tr.find_all('a'):
        fulllink = link.get ('href')




    try:
        date = str(tds[0].get_text())
        cPrice = tds[6].get_text()

    except:
        continue

    print "Date: {} | CLosing Price: {}.".format(date, cPrice)
