from django.shortcuts import render
import pandas as pd
from ..helper.covid19_world_confirmation_helper import remove_comma, covid_confirmation
from ..helper.save_dataframe_helper import return_data_frame

def status(request):
	df = return_data_frame('world_confirmation')

	df['Total Rank'] = df['Total'].apply(remove_comma).astype(int)
	df['Total Rank'] = df['Total Rank'] / df['Total Rank'].sum() * 100

	import plotly.express as px
	import plotly.offline as plot

	fig = px.pie(df, values='Total Rank', names='Area', hover_name='Total')
	fig.update_traces(hole=.4, hoverinfo="label+percent+name")
	fig.update_layout(
		title_text="World Covid19 confirmation",
		# Add annotations in the center of the donut pies.
		annotations=[dict(text='Covid19', x=0.5, y=0.5, font_size=20, showarrow=False)])
	fig.show()

	confirmation_graph = plot(fig, include_plotlyjs=False, output_type='div')

	return render(request, 'covid_web/status.html', {'df' : df, 'html_data' : confirmation_graph})