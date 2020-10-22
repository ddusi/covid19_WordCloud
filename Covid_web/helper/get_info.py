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


def basic():
    reg_url = 'https://www.health.harvard.edu/diseases-and-conditions/covid-19-basics'
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.3'}
    req = Request(url=reg_url, headers=headers) 

    context = ssl._create_unverified_context()

    html = urlopen(req,context=context)

    be = BeautifulSoup(html, 'html.parser')

    article = be.article

    cont = [ a.get_text() for a in article.find_all(re.compile('[h,p][0-9]?$')) ]
    return cont

def precaution():
    reg_url = 'https://www.google.com/search?newwindow=1&rlz=1C5CHFA_enKR906KR906&sxsrf=ALeKk03U3erUtcELyHKYrkqygAJC44yd3w%3A1598434292483&ei=9CtGX6OJHYWkmAXptZKABQ&q=covid-19+Precautions&oq=covid-19+Precautions&gs_lcp=CgZwc3ktYWIQAzICCAAyAggAMgIIADICCAAyAggAMgIIADICCAAyAggAMgIIADICCAA6BwgjELADECc6BwgAELADEENQ3WBY3WBg3mVoAXAAeACAAZIBiAGSAZIBAzAuMZgBAKABAqABAaoBB2d3cy13aXrAAQE&sclient=psy-ab&ved=0ahUKEwij08zhx7jrAhUFEqYKHemaBFAQ4dUDCA0&uact=5'
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.3'}
    req = Request(url=reg_url, headers=headers) 
    precautions = []

    context = ssl._create_unverified_context()

    html = urlopen(req,context=context)

    be = BeautifulSoup(html, 'html.parser')

    pre = be.find('div',{'class':'bVNaN'}).findAll('span')

    precautions = [ p.text for p in pre ]
    return precautions

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

def Make_Cloud(path):
    os.system('scrapy runspider Covid_web/scrapy/covid/spiders/covid_spider.py')
    file = 'article.csv'
    article_pd = pd.read_csv(file)
    
    headlines = list(article_pd['headline'])
    headlines = '.'.join(headlines)

    letters_only = re.sub('[^a-zA-Z]',' ',headlines)
    
    lower_case = letters_only.lower()

    words = lower_case.split()

    tagged = nltk.pos_tag(words)

    stop_words = ['daily','roundup','update','july','sunday','aug','list','line']
    name_list = [t[0] for t in tagged if t[1] != "VB" and t[0] not in stop_words and t[1] == "NN"]
    fd_names = FreqDist(name_list)

    wc = WordCloud(width=1200, height=800, background_color="white", random_state=0)
    plt.imshow(wc.generate_from_frequencies(fd_names))
    plt.axis('off')
    plt.savefig("Covid_web/static/"+path)