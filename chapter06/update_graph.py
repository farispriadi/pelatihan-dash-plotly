import dash
import dash_core_components as dcc 
import dash_html_components as html 
from dash.dependencies import Input, Output

app = dash.Dash()

data = {'pangkat2': [[1,2,3],[1,4,9]],
			'pangkat3': [[1,2,3],[1,8,27]]
		}

app.layout = html.Div(children=[
						html.H1("Aplikasi Web Sederhana Oppinet", style={'textAlign': 'center',
														'color': 'green',
							}),
						dcc.Dropdown(id='pangkat',
								options=[{'label':'Pangkat 2', 'value': 'pangkat2'},
									{'label':'Pangkat 3', 'value': 'pangkat3'}],
								value='pangkat2'),
						dcc.Graph(id='plot', 
								figure={})
					])

@app.callback(Output('plot','figure'),
		[Input('pangkat','value')]
	)
def update_plot(value):
	return {'data': [ 
					{'x':data[value][0],
					'y':data[value][1], 
					'marker':{'color':'rgb(235, 232, 52)'},
					'name':value},				
				],
				'layout': {'title' : 'Grafik {}'.format(value),}
			}

if __name__ == '__main__':
	# menjalankan aplikasi dash
	app.run_server()