import dash 
import dash_core_components as dcc 
import dash_html_components as html 
from dash.dependencies import Input, Output

app = dash.Dash()

app.layout = html.Div([
			html.Label(["Masukan Nama :"]),
			dcc.Input(id='input-nama',
					placeholder='Nama Anda',
					type='text',
					value='',
				),
			html.Div(children=["Anda belum memasukkan Nama"],id='output-nama')
		])

@app.callback(Output('output-nama','children'),
		[Input('input-nama','value')]
	)
def update_nama(nama):
	if nama:
		return 'Nama saya adalah {} '.format(nama)
	return 'Anda belum memasukkan Nama'

if __name__ == '__main__':
	app.run_server()