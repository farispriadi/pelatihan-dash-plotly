import dash
import dash_html_components as html
import dash_core_components as dcc


colors = {'text': '#ffffff', 'background': '#000033'}

# membuat dash object
app = dash.Dash()

# membuat layout
app.layout = html.Div(children=[
						html.H1("Aplikasi Web Sederhana Oppinet", style={'textAlign': 'center',
														'color': colors['text'],
							}),
						dcc.Graph(id='plot', 
								figure={'data': [ 
									{'x':[1,2,3], # menggunakan low level interface (list & dict)
									'y':[1,4,9], 
									# 'type':'bar', 
									'marker':{
                    							'color':'rgb(235, 232, 52)'
                    						},
									'name':'pangkat 2'},
									{'x':[1,2,3], 
									'y':[1,8,27],
									'marker':{
                    							'color':'rgb(255, 0, 0)'
                							},
									# 'type':'bar',
									'name':'pangkat 3'},					

								],
								'layout': {
									'title' : 'Line Plots',
									'plot_bgcolor': colors['background'],
									'paper_bgcolor': colors['background'],
									'font': {'color': colors['text']}
								}
								})
					], style={'background': colors['background']})

if __name__ == '__main__':
	# menjalankan aplikasi dash
	app.run_server()