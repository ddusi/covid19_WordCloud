from ..helper.get_info import basic,precaution, Covid_confirmed, Make_Cloud
from ..helper.make_cloud_helper import make_cloud_helper
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
        make_cloud_helper('covid_WordCloud.png')
        flag = False
    else:
        make_cloud_helper('covid_WordCloud1.png')
        flag = True
    article_pd = pd.read_csv('article.csv')
    article = article_pd.to_dict()
    cont = basic()
    pre = precaution()
    Korea, World = Covid_confirmed()
    timer.start()
make()