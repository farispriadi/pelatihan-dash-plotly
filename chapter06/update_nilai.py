import dash
import dash_core_components as dcc 
import dash_html_components as html 
from dash.dependencies import Input, Output


app = dash.Dash() 

app.layout = html.Div([
		html.Label(["Nama Lengkap : "]),
		dcc.Input(id='input-nama',
				placeholder='Masukan Nama Lengkap',
				type='text',
				value=''
			),
		html.Div(id='output-nama',children='')
	])

@app.callback(Output('output-nama','children'),
			[Input('input-nama', 'value')])
def update_nama(nama):
	if nama:
		return 'Nama Saya {}'.format(nama)
	return ''

if __name__ == '__main__':
	app.run_server()