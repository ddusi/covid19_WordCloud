from django.shortcuts import render
import pandas as pd
from covid_web.helper.covid19_world_confirmation_helper import remove_comma
from covid_web.helper.save_dataframe_helper import return_data_frame
import plotly.express as px
import plotly.graph_objects as go
import plotly.io as pio


# from plotly.offline import plot
# import plotly.offline.offline as plot

def status(request):
	df_world_data = return_data_frame('world_confirmation')

	df_world_data.drop([0], inplace=True)  # delete would data
	df_world_data['Total Rank'] = df_world_data['Total'].apply(remove_comma).astype(int)
	df_world_data['Total Rank'] = df_world_data['Total Rank'] / df_world_data['Total Rank'].sum() * 100

	fig = px.pie(df_world_data, values='Total Rank', names='Area', hover_name='Total')
	fig.update_traces(hole=.4, hoverinfo="label+percent+name")
	fig.update_layout(
		title_text="World Covid19 confirmation",
		# Add annotations in the center of the donut pies.
		annotations=[dict(text='Covid19', x=0.5, y=0.5, font_size=20, showarrow=False)])
	# confirmation_graph = fig.to_html(full_html=False)
	confirmation_graph = fig.to_html(full_html=False, include_plotlyjs='cdn')
	pio.write_image(fig, "covid_web/static/confirmation_graph.png")
	# fig.to_image(format='png', engine='orca')

	## Cumulative COVID-19 deaths on Jan 11, and first day of following months
	data = {'month': ['jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct'],
	        'case': [1, 259, 2977, 40598, 224172, 371166, 508055, 675060, 848445, 1010639]}
	df = pd.DataFrame(data)

	fig = go.Figure(go.Scatter(
		x=df['month'],
		y=df['case'],
	))

	fig.update_layout(
		title='Cumulative COVID-19 deaths on Jan 11, and first day of following months',
	)
	cumulative_deaths = fig.to_html(full_html=False, include_plotlyjs='cdn')
	pio.write_image(fig, "covid_web/static/cumulative_deaths.png")

	context = {'world_data': df_world_data.to_dict(),
	           'confirmation_graph': confirmation_graph,
	           'cumulative_deaths': cumulative_deaths}

	return render(request, 'covid_web/status.html', context)
