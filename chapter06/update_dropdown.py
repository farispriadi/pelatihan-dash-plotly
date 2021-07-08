import dash
import dash_core_components as dcc 
import dash_html_components as html 
from dash.dependencies import Input, Output

app = dash.Dash()

unit_dict = {
	'angle': ['degrees','radians'],
	'length': ['ft','m','km','cm']
}

app.layout = html.Div([
		html.Div([
				html.Label("Pilih tipe unit! "),
				dcc.Dropdown(id='unit-type',
					options=[{'label':'Length', 'value': 'length'},
						{'label':'Angle', 'value': 'angle'}],
					value='angle')

			]),
		html.Div([
				html.Label("Pilih unit! "),
				dcc.Dropdown(id='unit-selector',
					options=[{}],
					value='')
			])
	])

@app.callback(Output('unit-selector', 'options'),
		[Input('unit-type', 'value')]
	)
def update_units(unit_type):
	return [{'label':unit, 'value':unit} for unit in unit_dict[unit_type]]


if __name__ == '__main__':
	app.run_server()
