import dash
import dash_core_components as dcc 
import dash_html_components as html

colors = {'text': '#e6e8eb', 'background': 'rgb(230, 2, 112)'}

# object dash

app = dash.Dash()

#layout
app.layout = html.Div(children=[
					html.H1(children=["BTS Meal!"],style={'color': colors['text'], 'textAlign':'center'}),
					dcc.Graph(
							id='plot',
							figure={'data':[
									{
										'x': [1,2,3],
										'y': [1,4,9],
										# 'type': 'bar',
										'name': 'pangkat 2'
									},
									{
										'x': [1,2,3],
										'y': [1,8,27],
										# 'type': 'bar',
										'name': 'pangkat 3'
									},
								],
								'layout': {
									'title': 'Plot Viral',
									'plot_bgcolor': colors['background'],
									'paper_bgcolor': colors['background'],
									'font': {'color': colors['text']},
								}		
							}
						)
			], style={'background': colors['background']})

# main
if __name__ == '__main__':
	app.run_server()