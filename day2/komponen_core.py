import dash 
import dash_core_components as dcc 
import dash_html_components as html 

app = dash.Dash() 

app.layout = html.Div([
				html.Div([
					html.Label(["Length Unit"]), # label 
					dcc.Dropdown(id='my-dropdown', # dropdown
							options=[
								{'label':'km', 'value':'km'},
								{'label':'ft', 'value':'feet'},
								{'label': 'm', 'value':'meter'}
							],
							value='feet' # default value
						),
					html.Label(["Length Value"]), # input label
					dcc.Input(id='my-input', # input
							placeholder='Masukan Nilai',
							type='number',
						),
					html.Label(["Radio Items"]),
					dcc.RadioItems(id='my-radio',
						options=[
								{'label':'km', 'value':'km'},
								{'label':'ft', 'value':'feet'},
								{'label': 'm', 'value':'meter'}
							],
						value='feet'),
					html.Label("Button Example"),
					html.Button(["Submit"],style={'width':'200px'}),

				], style={'width': '200px'}),

				html.Div(["Div untuk Grafik",
						dcc.Graph(id='my-graph',
								figure={'data': [{'x': [1,2,3], 'y': [1,4,9]}],
									'layout': {'title': 'Grafik Pangkat 2'}
								}
							)
					])
			])

if __name__ == '__main__':
	app.run_server()