import dash
from dash import dcc, html
from dash.dependencies import Input, Output
import pandas as pd
import plotly.express as px



# data
data = {
    'Fruit': ['Apples', 'Oranges', 'Bananas', 'Grapes', 'Strawberries'],
    'Amount': [4, 1, 2, 5, 3]
}

# start app
app = dash.Dash(__name__)

# grabbing the data for dash and setting it into data framework
  # this is data source
  # this more likely than not will be data pull from an SQL server in the real world
df = pd.DataFrame(data)





# layout
# where you set html and graph components
app.layout = html.Div(
  [
    dcc.Dropdown(
     id="slct_fruit",
     options=[
     {"label": "Apples", "value": "Apples"},
     {"label": "Oranges", "value": "Oranges"},
     {"label": "Bananas", "value": "Bananas"},
     {"label": "Grapes", "value": "Grapes"},
       ],
     multi=False,
     value="Apples",
     style={'width': "80%"}
      ),
    html.H1("Amount of", style={'text-align': 'left'}),
    html.Div(id='output_container', children=[]),
    html.Br(),

    dcc.Graph(id="my_bar_chart", figure={})
  ]
)

#connect the Platly graphs with Dash Components
@app.callback(
  [Output(component_id='output_container', component_property='children'),
   Output(component_id="my_bar_chart", component_property='figure')],
  [Input(component_id='slct_fruit', component_property='value')]
)
def update_graph(slct_fruit):
  container = "The fruit chosen by user: {}".format(slct_fruit)

  dff = df.copy()
  dff = dff[dff["Fruit"]== slct_fruit]
  # dff = dff[dff["Amount"] == "Amount"]

  fig = px.bar(dff, x='Fruit', y="Amount")


  return container, fig

if __name__ == '__main__':
    app.run_server(debug=True)
