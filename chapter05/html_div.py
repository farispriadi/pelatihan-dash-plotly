import dash
import dash_html_components as html 

# Dash app object
app = dash.Dash()

# membuat komponen Div
app.layout = html.Div(["Ini Div bagian luar",
						html.Div(
							["Ini Div bagian Dalam"], 
							style={'color':'red', 'border':'2px red solid'}
						),
						html.Div(
							["Ini Div bagian Dalam Kedua"], 
							style={'color':'purple', 
									'border':'2px purple solid',
									'margin': '2px 2px 2px 2px'}
						),
					],
					style={'color':'green', 
							'border':'4px green solid', 
							'padding': '2px 2px 2px 2px'}
				)



if __name__ == '__main__':
	app.run_server()