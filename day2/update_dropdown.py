import dash 
import dash_core_components as dcc 
import dash_html_components as html 
from dash.dependencies import Input, Output

unit_dict = {
	'angle' : ['degrees','radians'],
	'length': ['ft','m','km','cm']
}

app = dash.Dash()

app.layout = html.Div([
		html.Label(["Pilih Tipe Unit"]),
		dcc.Dropdown(id='unit-type',
				options=[{'label': key.capitalize(), 'value': key} for key in unit_dict.keys()],
				value='angle'
			),
		html.Label(["Pilih Unit"]),
		dcc.Dropdown(id='unit-selector',
				options=[{}],
				value=''
			)
	])

@app.callback(Output('unit-selector', 'options'),
		[Input('unit-type', 'value')]
	)
def update_dropdown(unit_type):
	return [{'label': val ,'value': val} for val in unit_dict[unit_type]]

if __name__ == '__main__':
	app.run_server()