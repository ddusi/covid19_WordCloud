from django.apps import AppConfig
from multiprocessing import Process
import sys
from .views.views import make_data
from .helper.covid19_world_confirmation_helper import covid_confirmation
import time


class CovidWebConfig(AppConfig):
	name = 'covid_web'

	def ready(self):
		if 'runserver' not in sys.argv:
			return True

		process_one = Process(target=make_data)
		process_two = Process(target=covid_confirmation)
		process_one.start()
		process_two.start()
