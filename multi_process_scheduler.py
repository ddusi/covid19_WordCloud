from multiprocessing import Process

from covid_web.helper.make_cloud_helper import make_data
from covid_web.helper.covid19_world_confirmation_helper import covid_confirmation
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
	parser.add_argument('start')

	start_get_data()


if __name__ == "__main__":
	main()
