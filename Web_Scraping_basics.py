# -*- coding: utf-8 -*-
"""
Created on Sat Jan 21 17:05:55 2023

@author: shubh
"""

from bs4 import BeautifulSoup
import requests
import re

#1
url = 'https://www.tigerdirect.com/applications/SearchTools/item-details.asp?EdpNo=1501390'
user_agent = {'User-agent':'Mozilla/5.0'}
page = requests.get(url,headers = user_agent)
soup = BeautifulSoup(page.text, 'lxml')
list_price = soup.select("div.pdp-price p.list-price del")
#replacing first element of list which has the price using regex
list_price = re.sub(r'(.*)([0-9]),([0-9]{3})\.([0-9]{2})(.*)',r'\2\3.\4',str(list_price[0]))
print('list_price = ',list_price)
current_price = soup.select("div.pdp-price p.final-price span.sr-only")
current_price = [i.text for i in current_price]
#split the data as it has \r\n into different elements of the list as re.sub did not work directly
current_price = current_price[0].splitlines()
#used re.sub to replace the $ value and the cents part and concatenated
current_price[0] = re.sub(r'(.*)([0-9]),([0-9]{3})',r'\2\3',current_price[0])
current_price[1] = re.sub(r'(.*)([0-9]{2})(.*)',r'\2',current_price[1])
print('current price = ',current_price[0] + '.' + current_price[1])
#5
url = "https://www.usnews.com/"
user_agent = {'User-agent':'Mozilla/5.0'}
page = requests.get(url,headers = user_agent)
soup = BeautifulSoup(page.text, 'lxml')
#6
#top stories
headings = soup.select("div.Box-w0dun1-0.ArmRest__Container-z77ov1-0.hTnNtV.bZwypa.Cell-sc-1abjmm4-0-w.iRArip.Cell-sc-1abjmm4-0-w.iRArip h3.Heading-sc-1w5xk2o-0.ContentBox__StoryHeading-sc-1egb8dt-3.MRvpF.fqJuKa.story-headline")
#top stories stored in a list
headings_new = [i.text for i in headings]
headings_new
#urls of top stories
urls = [i.select('a')[0].get('href') for i in headings]
#7
#2nd url
urls[1]
user_agent = {'User-agent':'Mozilla/5.0'}
page = requests.get(urls[1],headers = user_agent)
#8
#2nd top story
soup = BeautifulSoup(page.text, 'lxml')
#9
#HTML for heading
heading_new_2 = soup.select("div.Villain__TitleContainer-sc-1y12ps5-6.knjdTo")
#Heading in text
heading = [i.text for i in heading_new_2]
#Selecting all paragraphs
paragraphs = soup.select("div.Raw-slyvem-0.bCYKCn")
#Paragraphs in text
all_paragraphs = [i.text for i in paragraphs]
#Removing empty values from list
all_paragraphs = list(filter(None,all_paragraphs))
#First 3 paragraphs and not the first three lines. The 2nd paragraph has 2 lines.
first_three_paragraphs = [all_paragraphs[i] for i in range(3)]
#first 3 lines
first_three_lines = [all_paragraphs[i] for i in range(2)]
print('The first three lines are: ' + first_three_lines[0] + ' '+ first_three_lines[1])
