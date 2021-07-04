import justpy as jp
import pandas as pd
from datetime import datetime
from pytz import utc
import matplotlib.pyplot as plt

data = pd.read_csv("reviews.csv", parse_dates=["Timestamp"])
data["Day"] = data["Timestamp"].dt.date
day_average = data.groupby("Day").mean()

splice_def = """
{
	chart: {
		type: 'spline',
		inverted: false
	},
	title: {
		text: 'Atmosphere Temperature by Altitude'
	},
	subtitle: {
		text: 'According to the Standard Atmosphere Model'
	},
	xAxis: {
		reversed: false,
		title: {
			enabled: true,
			text: 'Date'
		},
		labels: {
			format: '{value}'
		},
		accessibility: {
			rangeDescription: 'Range: 0 to 80 km.'
		},
		maxPadding: 0.05,
		showLastLabel: true
	},
	yAxis: {
		title: {
			text: 'Average Rating'
		},
		labels: {
			format: '{value}'
		},
		accessibility: {
			rangeDescription: 'Range: -90°C to 20°C.'
		},
		lineWidth: 2
	},
	legend: {
		enabled: false
	},
	tooltip: {
		headerFormat: '<b>{series.name}</b><br/>',
		pointFormat: '{point.y}'
	},
	plotOptions: {
		spline: {
			marker: {
				enable: false
			}
		}
	},
	series: [{
		name: 'Average Rating',
		data: [[0, 15], [10, -50], [20, -56.5], [30, -46.5], [40, -22.1],
			[50, -2.5], [60, -27.7], [70, -55.7], [80, -76.5]]
	}]
}
"""

def app():
	web_page = jp.QuasarPage()
	h2 = jp.QDiv(a=web_page, text="Analysis of Course Reviews", classes="text-h3 text-center q-pa-md")
	p = jp.QDiv(a=web_page, text="These graphs represent course review analysis")
	hc = jp.HighCharts(a=web_page, options=splice_def)
	hc.options.title.text = "Average Rating by Day"
	x = day_average.index
	y = day_average["Rating"]
	hc.options.series[0].data = list(y)
	hc.options.xAxis.categories = list(x)
	return web_page

jp.justpy(app)