import justpy as jp

def app():
	web_page = jp.QuasarPage()
	h2 = jp.QDiv(a=web_page, text="Analysis of Course Reviews", classes="text-h3 text-center q-pa-md")
	p = jp.QDiv(a=web_page, text="These graphs represent course review analysis")
	return web_page

jp.justpy(app)