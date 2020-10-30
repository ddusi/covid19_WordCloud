from bs4 import BeautifulSoup
from urllib.request import urlopen,Request
import ssl
import re
import nltk
import os
import pandas as pd
from nltk.tokenize import RegexpTokenizer
from nltk.tag import pos_tag
from nltk.tokenize import word_tokenize
from nltk import Text
import matplotlib.pyplot as plt
from nltk import FreqDist
from wordcloud import WordCloud
from nltk.corpus import stopwords


def Covid_confirmed():
    Korea = {
        'Area':[],
        'Total':[],
        'Cases':[],
        'Recovered':[],
        'Deaths':[],
    }
    World = {
        'Area':[],
        'Total':[],
        'Cases':[],
        'Recovered':[],
        'Deaths':[],
    }
    headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.135 Safari/537.36'}
    # Korea cases
    Korea_URL = 'https://news.google.com/covid19/map?hl=en-US&gl=US&ceid=US%3Aen&mid=%2Fm%2F06qd3'
    req = Request(url=Korea_URL, headers=headers) 
    context = ssl._create_unverified_context()

    html = urlopen(req,context=context)

    Korea_bs = BeautifulSoup(html, 'html.parser')

    Korea_Num = [ n.text.strip() for n in Korea_bs.find('tbody',{'class':'ppcUXd'},).findAll('td',{'class':'l3HOY'}) if n.text != ''][4:] 
    Korea_Area = [ a.text.strip() for a in Korea_bs.find('tbody',{'class':'ppcUXd'},).findAll('th',{'class':'l3HOY'}) if a.text != ''][1:]

    Korea['Area'] = Korea_Area
    for n in range(len(Korea_Num)):
        if n%4==0:
            Korea['Total'].append(Korea_Num[n])
        elif n%2==0:
            Korea['Recovered'].append(Korea_Num[n])
        elif (n-1)%4==0:
            Korea['Cases'].append(Korea_Num[n])
        else:
            Korea['Deaths'].append(Korea_Num[n])

    # world
    World_URL = 'https://news.google.com/covid19/map?hl=en-US&gl=US&ceid=US%3Aen'
    req = Request(url=World_URL, headers=headers) 

    html = urlopen(req,context=context)

    World_bs = BeautifulSoup(html, 'html.parser')

    World_Num = [ n.text.strip() for n in World_bs.find('tbody',{'class':'ppcUXd'}).findAll('td',{'class':'l3HOY'}) if n.text != ''][:64]
    World_Area = [ a.text.strip() for a in World_bs.find('tbody',{'class':'ppcUXd'},).findAll('th',{'class':'l3HOY'}) if a.text != ''][:16]

    World['Area'] = World_Area
    for n in range(len(World_Num)):
        if n%4==0:
            World['Total'].append(World_Num[n])
        elif n%2==0:
            World['Recovered'].append(World_Num[n])
        elif (n-1)%4==0:
            World['Cases'].append(World_Num[n])
        else:
            World['Deaths'].append(World_Num[n])

    return (Korea,World)