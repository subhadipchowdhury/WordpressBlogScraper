# -*- coding: utf-8 -*-
"""
Created on Fri Jan 19 14:50:39 2018

@author: Subhadip Chowdhury
"""
##Script to scrape WebSerials from Wordpress Blogs

import requests
from bs4 import BeautifulSoup
from time import sleep

##Put the URL of TOC here
toc_url="??"
###

counter=0

toc_page=requests.get(toc_url)
toc_soup = BeautifulSoup(toc_page.content, 'html.parser')

toc=toc_soup.find('div', class_="entry-content")

for link in toc.findChildren('a'):
#    print(link)
    counter+=1
    url=link.get('href')
    page=requests.get(url)
    soup=BeautifulSoup(page.content, 'html.parser')
    
    entry_title=soup.find(class_="entry-title")
    
    chapter_heading = str(entry_title)
    
    entry=soup.find(class_="entry-content")
    
    ##Get rid of extra stuff, depends on Webserial
    
    chapter=(str(entry)).split("<hr")[0]
    
    with open(str(counter) + ".html", "w", encoding='utf8') as outputfile:
        print("Starting Chapter " + entry_title.get_text())
        outputfile.write(chapter_heading + "\n" + chapter)
        print("Press CTRL-C to stop")
        
    sleep(1) ##So that you don't get banned
