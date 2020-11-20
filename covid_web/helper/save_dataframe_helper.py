import sqlite3

from Covid.settings import DATABASES
from django.conf import settings
import pandas as pd
from datetime import date


def save_data_frame(df: 'DataFrame', table: str) -> 'Success Message':
	conn = sqlite3.connect(DATABASES['default']['NAME'])
	c = conn.cursor()
	sql = 'SELECT COUNT(created_at) FROM ' + table + ' WHERE created_at LIKE ' + '\'' + str(date.today()) + '%\''
	# sql = 'SELECT COUNT(created_at) FROM ' + table + ' WHERE created_at LIKE ' + '\'' + '2020-11-0' + '%\''
	try:
		data = c.execute(sql).fetchall()
	except sqlite3.OperationalError:
		return print('-------------------------------- Error Not exist ' + table + ' --------------------------------')

	if data[0][0] == 0:
		df.to_sql(name=table, con=conn, if_exists='append', index=True)
		conn.close()
		return print('-------------------------------- ' + str(
			date.today()) + ' success save ' + table + ' --------------------------------')
	else:
		conn.close()
		return print('-------------------------------- ' + str(
			date.today()) + ' Already existing data ' + table + ' --------------------------------')


def return_data_frame(table: str) -> 'DataFrame':
	conn = sqlite3.connect(settings.DATABASES['default']['NAME'])
	# sql = 'SELECT * FROM ' + table + ' WHERE created_at LIKE ' + '\'' + str(date.today()) + '%\''
	sql = 'SELECT * FROM ' + table + ' WHERE created_at LIKE ' + '\'' + '2020-11-05' + '%\''
	df = pd.read_sql(sql, index_col='index', con=conn)
	conn.close()
	return df
