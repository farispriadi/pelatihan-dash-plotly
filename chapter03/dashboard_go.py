import dash
import dash_html_components as html
import dash_core_components as dcc
import plotly.graph_objs as go

# membuat dash object
app = dash.Dash()

# membuat layout
app.layout = html.Div(children=[
						html.H1("Aplikasi Web Sederhana Oppinet", style={'textAlign': 'center',
							}),
						dcc.Graph(id='plot', 
								figure= {
										'data' : [go.Scatter(
												x=[1, 2, 3], 
												y=[4, 1, 2],
												mode='lines+markers',
												marker={'color':'rgb(252, 82, 3)'},
												line={'width':2 },
												showlegend=True,
												name='data 1'
											)
										],
										'layout': go.Layout(title="Judul Plot",
															xaxis={'title':"sumbu x"}
											)
									}
								)
					])

if __name__ == '__main__':
	# menjalankan aplikasi dash
	app.run_server()