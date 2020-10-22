from ..helper.get_info import basic,precaution, Covid_confirmed, Make_Cloud
import threading
import pandas as pd

flag = True
article = {}
cont = []
pre = []
Korea = {}
World = {}


def make():
    global flag, cont, article, pre, Korea, World
    timer = threading.Timer(600,make)

    if flag:
        Make_Cloud('covid_WordCloud.jpg')
        flag = False
    else:
        Make_Cloud('covid_WordCloud1.jpg')
        flag = True
    article_pd = pd.read_csv('article.csv')
    article = article_pd.to_dict()
    cont = basic()
    pre = precaution()
    Korea, World = Covid_confirmed()
    timer.start()
# make()