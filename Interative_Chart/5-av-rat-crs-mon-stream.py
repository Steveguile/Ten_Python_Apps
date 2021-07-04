
import justpy as jp
import pandas
from datetime import datetime
from pytz import utc
 
data = pandas.read_csv("reviews.csv", parse_dates=["Timestamp"])

data["Month"] = data["Timestamp"].dt.strftime("%Y-%m")
month_average_course = data.groupby(["Month", "Course Name"])["Rating"].count().unstack()

print(month_average_course.index)

chart_def = """
{

    chart: {
        type: 'streamgraph',
        marginBottom: 30,
        zoomType: 'x'
    },
    title: {
        floating: true,
        align: 'left',
        text: 'Count of Ratings per Course'
    },
    subtitle: {
        floating: true,
        align: 'left',
        y: 30,
        text: 'Source: <a href="https://www.sports-reference.com/olympics/winter/1924/">sports-reference.com</a>'
    },

    xAxis: {
        maxPadding: 0,
        type: 'category',
        crosshair: true,
        categories: [],
        labels: {
            align: 'left',
            reserveSpace: false,
            rotation: 270
        },
        lineWidth: 0,
        margin: 20,
        tickWidth: 0
    },

    yAxis: {
        visible: false,
        startOnTick: false,
        endOnTick: false
    },

    legend: {
        enabled: false
    },

    plotOptions: {
        series: {
            label: {
                minFontSize: 5,
                maxFontSize: 15,
                style: {
                    color: 'rgba(255,255,255,0.75)'
                }
            }
        }
    },

    series: [],

    exporting: {
        sourceWidth: 800,
        sourceHeight: 600
    }
}
"""

def app():
	web_page = jp.QuasarPage()
	h2 = jp.QDiv(a=web_page, text="Analysis of Course Reviews", classes="text-h3 text-center q-pa-md")
	p = jp.QDiv(a=web_page, text="These graphs represent course review analysis")

	hc = jp.HighCharts(a=web_page, options=chart_def)

	hc_data = [{"name": v1, "data": [v2 for v2 in month_average_course[v1]]} for v1 in month_average_course.columns]
	hc.options.xAxis.categories = list(month_average_course.index)
	hc.options.series = hc_data

	return web_page

jp.justpy(app)