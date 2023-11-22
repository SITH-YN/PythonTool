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
df_member_info_total = pd.read_csv("../data/MEMBER_Info_Total.csv")
df_member_info_weekly = pd.read_csv("../data/MEMBER_Info_Weekly.csv")
df_smr_worktime = pd.read_csv("../data/SMR_WorkTime.csv")

fig = make_subplots(rows=3, cols=2, subplot_titles=["SMR-XXXXX-00001", "SMR-XXXXX-00001", "SMR-XXXXX-00002", "SMR-XXXXX-00002", "SMR-XXXXX-00003", "SMR-XXXXX-00003"])
# 横向きの棒グラフ
fig.add_trace(
    go.Bar(
        x=[120],
        y=["Plan Work Time[h]"],
        orientation="h",
        name="Plan Work Time[h]",
    ), row=1, col=1
)
fig.add_trace(
    go.Bar(
        x=[80],
        y=["Estimate Work Time[h]"],
        orientation="h",
        name="Estimate Work Time[h]",
    ), row=1, col=1
)
fig.add_trace(
    go.Bar(
        x=[160],
        y=["Landing Work Time[h]"],
        orientation="h",
        name="Landing Work Time[h]",
    ), row=1, col=1
)
fig.add_trace(
    go.Bar(
        x=[240],
        y=["Plan Work Time[h]"],
        orientation="h",
        name="Plan Work Time[h]",
    ), row=2, col=1
)
fig.add_trace(
    go.Bar(
        x=[120],
        y=["Estimate Work Time[h]"],
        orientation="h",
        name="Estimate Work Time[h]",
    ), row=2, col=1
)
fig.add_trace(
    go.Bar(
        x=[200],
        y=["Landing Work Time[h]"],
        orientation="h",
        name="Landing Work Time[h]",
    ), row=2, col=1
)
fig.add_trace(
    go.Bar(
        x=[80],
        y=["Plan Work Time[h]"],
        orientation="h",
        name="Plan Work Time[h]",
    ), row=3, col=1
)
fig.add_trace(
    go.Bar(
        x=[50],
        y=["Estimate Work Time[h]"],
        orientation="h",
        name="Estimate Work Time[h]",
    ), row=3, col=1
)
fig.add_trace(
    go.Bar(
        x=[130],
        y=["Landing Work Time[h]"],
        orientation="h",
        name="Landing Work Time[h]",
    ), row=3, col=1
)

# 横向きの折れ線グラフ
fig.add_trace(
    go.Scatter(
        mode="lines+markers",
        x=["2023/11/1", "2023/11/2", "2023/11/3", "2023/11/4", "2023/11/5", "2023/11/6", "2023/11/7"],
        y=[120, 100, 80, 60, 40, 20, 0],
        name="Base(SMR-XXXXX-00001)",
        line=dict(color="red", dash="dot"),
        marker=dict(symbol="circle"),
    ), row=1, col=2
)
fig.add_trace(
    go.Scatter(
        mode="lines+markers",
        x=["2023/11/1", "2023/11/2", "2023/11/3", "2023/11/4", "2023/11/5", "2023/11/6", "2023/11/7"],
        y=[120, 80, 40, 20, 0, 0, 0],
        name="Target(SMR-XXXXX-00001)",
        line=dict(color="blue", dash="solid"),
        marker=dict(symbol="circle"),
    ), row=1, col=2
)
fig.add_trace(
    go.Scatter(
        mode="lines+markers",
        x=["2023/11/1", "2023/11/2", "2023/11/3", "2023/11/4", "2023/11/5", "2023/11/6", "2023/11/7"],
        y=[160, 130, 100, 70, 40, 10, 0],
        name="Base(SMR-XXXXX-00002)",
        line=dict(color="red", dash="dot"),
        marker=dict(symbol="circle"),
    ), row=2, col=2
)
fig.add_trace(
    go.Scatter(
        mode="lines+markers",
        x=["2023/11/1", "2023/11/2", "2023/11/3", "2023/11/4", "2023/11/5", "2023/11/6", "2023/11/7"],
        y=[160, 150, 130, 100, 60, 10, 0],
        name="Target(SMR-XXXXX-00002)",
        line=dict(color="blue", dash="solid"),
        marker=dict(symbol="circle"),
    ), row=2, col=2
)
fig.add_trace(
    go.Scatter(
        mode="lines+markers",
        x=["2023/11/1", "2023/11/2", "2023/11/3", "2023/11/4", "2023/11/5", "2023/11/6", "2023/11/7"],
        y=[200, 190, 170, 140, 100, 50, 0],
        name="Base(SMR-XXXXX-00003)",
        line=dict(color="red", dash="dot"),
        marker=dict(symbol="circle"),
    ), row=3, col=2
)
fig.add_trace(
    go.Scatter(
        mode="lines+markers",
        x=["2023/11/1", "2023/11/2", "2023/11/3", "2023/11/4", "2023/11/5", "2023/11/6", "2023/11/7"],
        y=[200, 190, 180, 170, 130, 80, 40],
        name="Target(SMR-XXXXX-00003)",
        line=dict(color="blue", dash="solid"),
        marker=dict(symbol="circle"),
    ), row=3, col=2
)

app = dash.Dash(__name__)

app.layout = html.Div([
    html.H4('SMR WorkTime Report'),
    dcc.Dropdown(
        options=[
            {'label': 'PlatForm', 'value': 'PF'},
            {'label': 'Development Environment', 'value': 'DE'},
            {'label': 'Diagnostic', 'value': 'DIAG'},
            {'label': 'Safety Function', 'value': 'SF'},
        ],
        value='', style={'width': '40%'}
    ),
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
    # html.H4('MEMBER WorkTime Report'),
    # # ドロップダウンでTotal/Weekly(This Week/Last Week/Next Week)切り替え
    # dcc.Dropdown(
    #     options=[
    #         {'label': 'Total', 'value': 'TOTAL'},
    #         {'label': 'This Week', 'value': 'THIS'},
    #         {'label': 'Last Week', 'value': 'LAST'},
    #         {'label': 'Next Week', 'value': 'NEXT'},
    #     ],
    #     value='TOTAL', style={'width': '30%'}
    # ),
    # # Total表示
    # html.P(id='table_out_member_info_total'),
    # dash.dash_table.DataTable(
    #     id='table_in_member_info_total',
    #     columns=[{"name": i, "id": i}
    #              for i in df_member_info_total.columns],
    #     data=df_member_info_total.to_dict('records'),
    #     style_cell=dict(textAlign='left'),
    #     style_header=dict(backgroundColor="paleturquoise"),
    #     style_data=dict(backgroundColor="lavender")
    # ),
    # html.P(id='table_out_member_info_weekly'),
    # dash.dash_table.DataTable(
    #     id='table_in_member_info_weekly',
    #     columns=[{"name": i, "id": i}
    #              for i in df_member_info_weekly.columns],
    #     data=df_member_info_weekly.to_dict('records'),
    #     style_cell=dict(textAlign='left'),
    #     style_header=dict(backgroundColor="paleturquoise"),
    #     style_data=dict(backgroundColor="lavender")
    # ),
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


test_fig = make_subplots(rows=3, cols=1, subplot_titles=["SMR-XXXXX-00001", "SMR-XXXXX-00002", "SMR-XXXXX-00003"])
# 横向きの棒グラフ
test_fig.add_trace(
    go.Bar(
        x=[120],
        y=["Plan Work Time[h]"],
        orientation="h",
        name="Plan Work Time[h]",
    ), row=1, col=1
)
test_fig.add_trace(
    go.Bar(
        x=[80],
        y=["Estimate Work Time[h]"],
        orientation="h",
        name="Estimate Work Time[h]",
    ), row=1, col=1
)
test_fig.add_trace(
    go.Bar(
        x=[160],
        y=["Landing Work Time[h]"],
        orientation="h",
        name="Landing Work Time[h]",
    ), row=1, col=1
)
test_fig.add_trace(
    go.Bar(
        x=[240],
        y=["Plan Work Time[h]"],
        orientation="h",
        name="Plan Work Time[h]",
    ), row=2, col=1
)
test_fig.add_trace(
    go.Bar(
        x=[120],
        y=["Estimate Work Time[h]"],
        orientation="h",
        name="Estimate Work Time[h]",
    ), row=2, col=1
)
test_fig.add_trace(
    go.Bar(
        x=[200],
        y=["Landing Work Time[h]"],
        orientation="h",
        name="Landing Work Time[h]",
    ), row=2, col=1
)
test_fig.add_trace(
    go.Bar(
        x=[80],
        y=["Plan Work Time[h]"],
        orientation="h",
        name="Plan Work Time[h]",
    ), row=3, col=1
)
test_fig.add_trace(
    go.Bar(
        x=[50],
        y=["Estimate Work Time[h]"],
        orientation="h",
        name="Estimate Work Time[h]",
    ), row=3, col=1
)
test_fig.add_trace(
    go.Bar(
        x=[130],
        y=["Landing Work Time[h]"],
        orientation="h",
        name="Landing Work Time[h]",
    ), row=3, col=1
)
test_fig.show()

"""3.1.3 棒グラフ（Bar trace）"""
# bar_trace1 = go.Bar(x=["120", "80", "240"], y=["Estimate"], orientation="h", name="Estimate")
# bar_trace2 = go.Bar(x=["60", "20", "50"], y=["Remain"], orientation="h", name="Remain")
# grouped_fig = go.Figure([bar_trace1, bar_trace2])
# grouped_fig.show()

# test1_fig = make_subplots(rows=3, cols=1, subplot_titles=["SMR-XXXXX-00001", "SMR-XXXXX-00002", "SMR-XXXXX-00003"])

bar_trace1 = go.Bar(y=["SMR-xxxx-00001", "SMR-xxxx-00002", "SMR-xxxx-00003"], x=[120, 40, 80], orientation="h", name="Estimate")
bar_trace2 = go.Bar(y=["SMR-xxxx-00001", "SMR-xxxx-00002", "SMR-xxxx-00003"], x=[20, 80, 120], orientation="h", name="Remain")
bar_trace3 = go.Bar(x=[160, 240, 320], y=["SMR-xxxx-00001", "SMR-xxxx-00002", "SMR-xxxx-00003"], orientation="h", name="Plan]", ),
stacked_fig = go.Figure(
    [bar_trace1, bar_trace2],
    # 積み上げ棒グラフにするためのlayoutを設定
    layout=go.Layout(barmode="stack"),
)
stacked_fig.show()


if __name__ == '__main__':
    app.run_server(debug=True, use_reloader=True)
    webbrowser.open_new_tab("http://127.0.0.1:8050/")
