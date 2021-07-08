import dash
import dash_core_components as dcc 
import dash_html_components as html

# object Dash app
app = dash.Dash() 

app.layout = html.Div([
	# Div untuk Dropdown
	html.Div([
			html.Label(["Length Unit"]),
			dcc.Dropdown(id='my-dropdown',
					options=[{'label':'cm', 'value': 'centimeter'},
							{'label':'m', 'value': 'meter'},
							{'label':'km', 'value': 'kilometer'},
							{'label':'ft', 'value': 'feet'}
					],
					value='feet'
				)
		], style={'width': '100px'}),
	# Div untuk Input
	html.Div([
			html.Label(["Length Value"]),
			dcc.Input(id='my-input',
					placeholder='Masukkan Nilai',
					type='number', # tipe bisa "text", "number", "password", "email"
					value=0 # default value yang menyesuaikan tipe 
				)
		], style={'width': '100px'}),
	# Div untuk RadioItems
	html.Div([
			html.Label(["Type of Unit"]),
			dcc.RadioItems(id='my-radio',
					options=[{'label':'Length', 'value': 'length'},
							{'label':'Temperature', 'temperature': ''},
							{'label':'Pressure', 'value': 'pressure'},
							{'label':'Angle', 'value': 'angle'}
					],
					value='length'
				)
		], style={'width': '100%'}),

	# Div untuk Button
	html.Div([
			html.Label(["Push the button !"]),
			html.Button(["Click Me"],id='my-button')
		], style={'width': '200px'}),

	])
	

if __name__ == '__main__':
	app.run_server()