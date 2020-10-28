from bs4 import BeautifulSoup
from urllib.request import urlopen, Request
import ssl


def basic():
	reg_url = 'https://www.health.harvard.edu/diseases-and-conditions/covid-19-basics'
	headers = {
		'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.3'}
	req = Request(url=reg_url, headers=headers)

	context = ssl._create_unverified_context()

	html = urlopen(req, context=context)

	be = BeautifulSoup(html, 'html.parser')

	article = be.article

	cont = [a.get_text() for a in article.find_all(re.compile('[h,p][0-9]?$'))]
	return cont


def precaution():
	reg_url = 'https://www.google.com/search?newwindow=1&rlz=1C5CHFA_enKR906KR906&sxsrf=ALeKk03U3erUtcELyHKYrkqygAJC44yd3w%3A1598434292483&ei=9CtGX6OJHYWkmAXptZKABQ&q=covid-19+Precautions&oq=covid-19+Precautions&gs_lcp=CgZwc3ktYWIQAzICCAAyAggAMgIIADICCAAyAggAMgIIADICCAAyAggAMgIIADICCAA6BwgjELADECc6BwgAELADEENQ3WBY3WBg3mVoAXAAeACAAZIBiAGSAZIBAzAuMZgBAKABAqABAaoBB2d3cy13aXrAAQE&sclient=psy-ab&ved=0ahUKEwij08zhx7jrAhUFEqYKHemaBFAQ4dUDCA0&uact=5'
	headers = {
		'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.3'}
	req = Request(url=reg_url, headers=headers)
	precautions = []

	context = ssl._create_unverified_context()

	html = urlopen(req, context=context)

	be = BeautifulSoup(html, 'html.parser')

	pre = be.find('div', {'class': 'bVNaN'}).findAll('span')

	precautions = [p.text for p in pre]
	return precautions
