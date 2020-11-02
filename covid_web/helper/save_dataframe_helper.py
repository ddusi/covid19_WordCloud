import sqlite3
from django.conf import settings
import pandas as pd


def save_dataframe(df, table):
	conn = sqlite3.connect(settings.DATABASES['default']['NAME'])
	df.to_sql(name=table, con=conn, if_exists='append', index=True)

	conn.close()


def return_dataframe(table):
	conn = sqlite3.connect(settings.DATABASES['default']['NAME'])
	df = pd.read_sql_table(table, index_col='index', con=conn)
	return df
