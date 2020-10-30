import scrapy
import pandas as pd

class CovidSpider(scrapy.Spider):
    name = "covid_article"
    start_urls = [
        'https://news.google.com/search?q=covid19&hl=en-US&gl=US&ceid=US%3Aen',
    ]

    def parse(self, response):
        dic = {'headline':[],'company':[],'time':[],'url':[]}
        headline = response.css('.DY5T1d::text').getall()
        company = response.css('.wEwyrc::text').getall()
        time = response.css('.WW6dff::text').getall()
        urls = response.css('.DY5T1d::attr(href)').getall()
        dic['headline'] = headline
        dic['company'] = company
        dic['time'] = time
        dic['url'] = [ 'https://news.google.com%s' % url.split('.')[1] for url in urls]

        # dic.drop(columns='Unnamed: 0',inplace=True)

        pd.DataFrame(dic).to_csv('article.csv')