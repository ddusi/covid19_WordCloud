from django.shortcuts import render
import pandas as pd
from covid_web.helper.covid19_world_confirmation_helper import remove_comma
from covid_web.helper.save_dataframe_helper import return_data_frame
import plotly.express as px


# from plotly.offline import plot
# import plotly.offline.offline as plot

def status(request):
	df = return_data_frame('world_confirmation')

	df.drop([0], inplace=True)  # delete would data
	df['Total Rank'] = df['Total'].apply(remove_comma).astype(int)
	df['Total Rank'] = df['Total Rank'] / df['Total Rank'].sum() * 100

	fig = px.pie(df, values='Total Rank', names='Area', hover_name='Total')
	fig.update_traces(hole=.4, hoverinfo="label+percent+name")
	fig.update_layout(
		title_text="World Covid19 confirmation",
		# Add annotations in the center of the donut pies.
		annotations=[dict(text='Covid19', x=0.5, y=0.5, font_size=20, showarrow=False)])
	# confirmation_graph = fig.to_html(full_html=False)
	confirmation_graph = fig.to_html(full_html=False, default_height=500, default_width=700)
	context = {'confirmation_graph': confirmation_graph}

	return render(request, 'covid_web/status.html', context)
