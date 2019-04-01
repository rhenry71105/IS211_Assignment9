#!usr/bin/env python
# -*- coding: utf-8 -*-
"""
	Part I ­ CBS Football Stats
	Author: Rickardo Henry
"""
import urllib2
from bs4 import BeautifulSoup

url = "https://www.cbssports.com/nfl/stats/playersort/nfl/year-2019-season-regular-category-touchdowns"
page = urllib2.urlopen(url)
soup = BeautifulSoup(page.read(), 'lxml')

trs = soup.find_all('tr')
top20Counter = 0

for tr in trs:
    for link in tr.find_all('a'):
        fulllink = link.get ('href')


    tds = tr.find_all("td")

    try:
        names = str(tds[0].get_text())
        position = str(tds[1].get_text())
        team = str(tds[2].get_text())
        touchdowns = tds[6].get_text()

    except:
        continue
    top20Counter += 1
    if top20Counter > 20:
        break

    print "Name: {} | Position: {} | Team: {} | Touchdowns {}.".format(names, position, team, touchdowns)
