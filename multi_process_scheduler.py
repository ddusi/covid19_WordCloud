from multiprocessing import Process

from covid_web.helper.make_cloud_helper import make_data
from covid_web.helper.covid19_world_confirmation_helper import covid_confirmation
# from get_covid19_article_data_helper import main_crawl
import argparse


def start_get_data():
	print("-------------------------------- Start get data --------------------------------")
	process_one = Process(target=make_data)
	process_two = Process(target=covid_confirmation)
	process_one.start()
	process_two.start()
	process_one.join()
	print("-------------------------------- Finish Get covid19 article & Make WordCloud  --------------------------------")
	process_two.join()
	print("-------------------------------- Finish covid19_confirmation --------------------------------")
	print("-------------------------------- End --------------------------------")

def main():
	parser = argparse.ArgumentParser()

	# name argument 추가
	parser.add_argument('start', action='store_true')
	# start_get_data()

	# parser.add_argument('make_article', action='store_true')
	# main_crawl()
	args = parser.parse_args()
	if args.start:
		print('start')
	elif args.make_article:
		print('make_article')

if __name__ == "__main__":
	main()
