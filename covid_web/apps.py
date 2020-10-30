from django.apps import AppConfig
from multiprocessing import Process
import sys
from .views.views import make_data
import time


class CovidWebConfig(AppConfig):
	name = 'covid_web'

	def ready(self):
		if 'runserver' not in sys.argv:
			return True

		process_one = Process(target=make_data)
		process_one.start()
