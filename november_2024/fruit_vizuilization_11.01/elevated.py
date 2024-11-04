import dash
from dash import dcc, html
from dash.dependencies import Input, Output
import pandas as pd
import plotly.express as px



data = {
    'Fruit': ['Apples', 'Oranges', 'Bananas', 'Grapes', 'Strawberries'],
    'Amount': [4, 1, 2, 5, 3],
    'Color': ['#dd1533', '#FFA500', '#FFE135 ', '#6F2DA8', '#C83F49']
}

app = dash.Dash(__name__)

df = pd.DataFrame(data)

# creating default figure with default selected value so inital load doent look like ass
default_fruit = "Apples"
default_df = df[df["Fruit"] == default_fruit]
default_fig = px.bar(default_df, x='Fruit', y="Amount")
default_fig.update_traces(marker_color=default_df['Color'].iloc[0])

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
     value=default_fruit,
     style={'width': "80%"}
      ),
    html.H1(id="fruit_header", style={'text-align': 'left'}),
    html.Div(id='output_container', children=[]),
    html.Br(),
    #pass in the default fig for inital layout, this will be overwritten when user changes selection
    dcc.Graph(id="my_bar_chart", figure=default_fig)
  ]
)

@app.callback(
  [ Output(component_id="fruit_header", component_property="children"),
   Output(component_id="my_bar_chart", component_property='figure')],
  [Input(component_id='slct_fruit', component_property='value')]
)
def update_graph(slct_fruit):

  #removed orignial firsr output and replaced with fruit_header
  #the order of the output Determenes the order you should return arguments with
  header_text= f"Amount of {slct_fruit}"


  dff = df.copy()


  dff = dff[dff["Fruit"]== slct_fruit]

  #iloc is using array like context to grab approriate key from data frame created by pandas
  # since fruit was filtered, each col only has one row
  # so you are grabbing the only value with .iloc[0]
  fig = px.bar(dff, x='Fruit', y="Amount")

  # displaying all data at once
  fig.update_traces(marker_color=dff['Color'].iloc[0])

  # the order in which you return outputs in is determined by the orter in which they outputs were declared in the callback
  return header_text, fig

if __name__ == '__main__':
    app.run_server(debug=True)
