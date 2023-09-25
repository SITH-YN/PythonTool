"""Sample Application."""
# Run this app with `python sample.py` and
# visit http://127.0.0.1:8050/ in your web browser.


from dash import Dash, html, dcc
import plotly.express as px
import pandas as pd

app = Dash(__name__)

# assume you have a "long-form" data frame
# see https://plotly.com/python/px-arguments/ for more options
df = pd.DataFrame({
    "Fruit": ["Apples", "Oranges", "Bananas", "Apples", "Oranges", "Bananas"],
    "Amount": [4, 1, 2, 2, 4, 5],
    "City": ["SF", "SF", "SF", "Montreal", "Montreal", "Montreal"]
})

fig = px.bar(df, x="Fruit", y="Amount", color="City", barmode="group")

# def serve_layout():
#     return html.H1('The time is: ' + str(datetime.datetime.now()))

# app.layout = serve_layout # app.layout = server_layout() はNG

app.layout = html.Div(children=[
    html.H1(children='SMR'),

    html.Div(children='''
        SMR Summary
    '''),

    dcc.Graph(
        id='example-graph',
        figure=fig
    )
])

if __name__ == '__main__':
    app.run(debug=True, use_reloader=True)
