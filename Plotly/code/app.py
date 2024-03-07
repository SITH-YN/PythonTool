"""Dash App."""
# Run this app with `python sample.py` and
# visit http://127.0.0.1:8050/ in your web browser.

import dash
import dash_daq as daq
from dash import dcc
from dash import html
from dash.dash_table import DataTable
from dash.dependencies import Input, Output, State, ALL, ALLSMALLER, MATCH
import plotly
import plotly.graph_objects as go
import plotly.express as px
from plotly.subplots import make_subplots
import json
import numpy as np
import pandas as pd
from IPython.display import Image
import webbrowser

# Get SMR Information From SMR List.xlsx

# Get Data From CSV File
df_smr_info = pd.read_csv("../data/SMR_info.csv")

fig = make_subplots(rows=3, cols=2, subplot_titles=["SMR-XXXXX-00001", "SMR-XXXXX-00001", "SMR-XXXXX-00002", "SMR-XXXXX-00002", "SMR-XXXXX-00003", "SMR-XXXXX-00003"])

# ループ1回目
fig.add_trace(go.Bar(x=df_smr_info["Actual Working Time[h]"], y=["SMR-XXXXX-00001"], orientation="h", text=df_smr_info["Actual Working Time[h]"], name="Actual Working Time(SMR-XXXXX-00001)", offsetgroup=1), row=1, col=1)
fig.add_trace(go.Bar(x=df_smr_info["Remain Working Time[h]"], y=["SMR-XXXXX-00001"], orientation="h", text=df_smr_info["Remain Working Time[h]"], name="Remaining Working Time(SMR-XXXXX-00001)", offsetgroup=1, base=df_smr_info["Actual Working Time[h]"]), row=1, col=1)
fig.add_trace(go.Bar(x=df_smr_info["Planned Working Time[h]"], y=["SMR-XXXXX-00001"], orientation="h", text=df_smr_info["Planned Working Time[h]"], name="Planned Working Time(SMR-XXXXX-00001)", offsetgroup=2), row=1, col=1)
# fig.update_xaxes(title_text="Working Time[h]")
# fig.update_yaxes(title_text="SMR No")

fig.add_trace(
    go.Scatter(
        mode="lines+markers",
        x=["2023/11/1", "2023/11/2", "2023/11/3", "2023/11/4", "2023/11/5", "2023/11/6", "2023/11/7"],
        y=[120.00, 100.00, 80.00, 60.00, 40.00, 20.00, 0.00],
        name="Expected Remaining Working Time(SMR-XXXXX-00001)",
        line=dict(color="red", dash="dot"),
        marker=dict(symbol="circle"),
    ), row=1, col=2
)
fig.add_trace(
    go.Scatter(
        mode="lines+markers",
        x=["2023/11/1", "2023/11/2", "2023/11/3", "2023/11/4", "2023/11/5", "2023/11/6", "2023/11/7"],
        y=[120.00, 80.00, 40.00, 20.00, 0.00, 0.00, 0.00],
        name="Actual Remaining Working Time(SMR-XXXXX-00001)",
        line=dict(color="blue", dash="solid"),
        marker=dict(symbol="circle"),
    ), row=1, col=2
)

# ループ2回目
fig.add_trace(go.Bar(x=df_smr_info["Actual Working Time[h]"], y=["SMR-XXXXX-00002"], orientation="h", text=df_smr_info["Actual Working Time[h]"], name="Actual Working Time(SMR-XXXXX-00002)", offsetgroup=1), row=2, col=1)
fig.add_trace(go.Bar(x=df_smr_info["Remain Working Time[h]"], y=["SMR-XXXXX-00002"], orientation="h", text=df_smr_info["Remain Working Time[h]"], name="Remaining Working Time(SMR-XXXXX-00002)", offsetgroup=1, base=df_smr_info["Actual Working Time[h]"]), row=2, col=1)
fig.add_trace(go.Bar(x=df_smr_info["Planned Working Time[h]"], y=["SMR-XXXXX-00002"], orientation="h", text=df_smr_info["Planned Working Time[h]"], name="Planned Working Time(SMR-XXXXX-00002)", offsetgroup=2), row=2, col=1)
# fig.update_xaxes(title_text="Working Time[h]")
# fig.update_yaxes(title_text="SMR No")

fig.add_trace(
    go.Scatter(
        mode="lines+markers",
        x=["2023/11/1", "2023/11/2", "2023/11/3", "2023/11/4", "2023/11/5", "2023/11/6", "2023/11/7"],
        y=[160.00, 130.00, 100.00, 70.00, 40.00, 10.00, 0.00],
        name="Expected Remaining Working Time(SMR-XXXXX-00002)",
        line=dict(color="red", dash="dot"),
        marker=dict(symbol="circle"),
    ), row=2, col=2
)
fig.add_trace(
    go.Scatter(
        mode="lines+markers",
        x=["2023/11/1", "2023/11/2", "2023/11/3", "2023/11/4", "2023/11/5", "2023/11/6", "2023/11/7"],
        y=[160.00, 150.00, 130.00, 100.00, 60.00, 10.00, 0.00],
        name="Actual Remaining Working Time(SMR-XXXXX-00002)",
        line=dict(color="blue", dash="solid"),
        marker=dict(symbol="circle"),
    ), row=2, col=2
)

# ループ3回目
fig.add_trace(go.Bar(x=df_smr_info["Actual Working Time[h]"], y=["SMR-XXXXX-00003"], orientation="h", text=df_smr_info["Actual Working Time[h]"], name="Actual Working Time(SMR-XXXXX-00003)", offsetgroup=1), row=3, col=1)
fig.add_trace(go.Bar(x=df_smr_info["Remain Working Time[h]"], y=["SMR-XXXXX-00003"], orientation="h", text=df_smr_info["Remain Working Time[h]"], name="Remaining Working Time(SMR-XXXXX-00003)", offsetgroup=1, base=df_smr_info["Actual Working Time[h]"]), row=3, col=1)
fig.add_trace(go.Bar(x=df_smr_info["Planned Working Time[h]"], y=["SMR-XXXXX-00003"], orientation="h", text=df_smr_info["Planned Working Time[h]"], name="Planned Working Time(SMR-XXXXX-00003)", offsetgroup=2), row=3, col=1)
# fig.update_xaxes(title_text="Working Time[h]")
# fig.update_yaxes(title_text="SMR No")

fig.add_trace(
    go.Scatter(
        mode="lines+markers",
        x=["2023/11/1", "2023/11/2", "2023/11/3", "2023/11/4", "2023/11/5", "2023/11/6", "2023/11/7"],
        y=[200.00, 190.00, 170.00, 140.00, 100.00, 50.00, 0.00],
        name="Expected Remaining Working Time(SMR-XXXXX-00003)",
        line=dict(color="red", dash="dot"),
        marker=dict(symbol="circle"),
    ), row=3, col=2
)
fig.add_trace(
    go.Scatter(
        mode="lines+markers",
        x=["2023/11/1", "2023/11/2", "2023/11/3", "2023/11/4", "2023/11/5", "2023/11/6", "2023/11/7"],
        y=[200.00, 190.00, 180.00, 170.00, 130.00, 80.00, 40.00],
        name="Actual Remaining Working Time(SMR-XXXXX-00003)",
        line=dict(color="blue", dash="solid"),
        marker=dict(symbol="circle"),
    ), row=3, col=2
)


app = dash.Dash(__name__)

app.layout = html.Div([
    html.H4('SMR Working Time Report'),
    html.P(id='table_out_smr_info'),
    dash.dash_table.DataTable(
        id='table_in_smr_info',
        columns=[{"name": i, "id": i}
                 for i in df_smr_info.columns],
        data=df_smr_info.to_dict('records'),
        style_cell=dict(textAlign='left'),
        style_header=dict(backgroundColor="paleturquoise"),
        style_data=dict(backgroundColor="lavender")
    ),
    html.P(id='graph_work_time'),
    dcc.Graph(
        figure=fig
    ),
])


@app.callback(
    Output('table_out_smr_info', 'children'),
    Input('table_in_smr_info', 'active_cell'))
def update_graphs(active_cell):
    """Update Graphs."""
    if active_cell:
        cell_data = df_smr_info.iloc[active_cell['row']][active_cell['column_id']]
        return f"Data: \"{cell_data}\" from table cell: {active_cell}"
    return "Click the table"


if __name__ == '__main__':
    app.run_server(debug=True, use_reloader=True)
    webbrowser.open_new_tab("http://127.0.0.1:8050/")
