import dash 
import dash_html_components as html 


app = dash.Dash() 

app.layout = 
			html.Div(["Ini adalah Div terluar!",
						html.Div(["Ini Div bagian dalam!!"], style={'border':'4px red solid', 'margin': '0px 0px 10px 0px'}),
						html.Div(["Ini Div bagian dalam kedua!!"], style={'border':'4px blue solid'})

					],
					style={'border':"4px green solid", 'padding':'10px 10px 10px 10px'}
				)


if __name__ == "__main__":
	app.run_server()