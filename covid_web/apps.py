from django.apps import AppConfig
import sys



class CovidWebConfig(AppConfig):
	name = 'covid_web'

	def ready(self):
		if 'runserver' not in sys.argv:
			return True

