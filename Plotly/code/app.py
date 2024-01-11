"""Dash App."""
# Run this app with `python sample.py` and
# visit http://127.0.0.1:8050/ in your web browser.

# Standard Library
import csv
import enum
import os
import re
import shutil
import subprocess

# 3rd party Libarary
import dash
from dash import daq
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
import webbrowser

# Get SMR Information Data From CSV File
df_smr_info = pd.read_csv("../data/Diag_SMR_Info.csv")

# SMR数分ループ
smr_num = 0
loop_index = 0
smr_no = []
project = []
SMR_Start = []
SVN_Fix = []
SMR_Fix = []
Author = []
Checker = []
Planned_WorkTime = []
Actual_WorkTime = []
Remaining_WorkTime = []
Estimated_WorkTime = []
Estimated_WorkTime_Ratio = []

# SMR数分ループ
with open("../data/Diag_SMR_Info.csv", "r", encoding="shift_jis", errors="", newline="") as read_csv_file:
    read_csv_data = csv.reader(read_csv_file, delimiter=",", doublequote=True, lineterminator="\r\n", quotechar='"', skipinitialspace=True)
    # tmp_header1:説明,第１フォルダーと第２フォルダー
    # tmp_header2:行数（>フォルダー?1）,行数（フォルダー?2）,行数（合計）,テキスト ブロック
    # tmp_loc_nochange[0]～[4]:変更なし,23633,23633,47266,1502
    # tmp_loc_modify[0]～[4]:変更箇所,9875,20865,30740,1463
    # tmp_loc_insert[0]～[4]:挿入箇所,0,1687,1687,24
    # tmp_loc_delete[0]～[4]:削除箇所,2158,0,2158,16
    tmp_header1 = next(read_csv_data)
    tmp_header2 = next(read_csv_data)
    tmp_loc_nochange = next(read_csv_data)
    tmp_loc_modify = next(read_csv_data)
    tmp_loc_insert = next(read_csv_data)
    tmp_loc_delete = next(read_csv_data)

    # loc_info[4(0～3)]:LOC差分情報
    # loc_info[0]:nochange
    # loc_info[1]:modify
    # loc_info[2]:insert
    # loc_info[3]:delete
    loc_info["nochange"] = int(tmp_loc_nochange[LOC.SUM.value])
    loc_info["modify"] = int(tmp_loc_modify[LOC.SUM.value])
    loc_info["insert"] = int(tmp_loc_insert[LOC.SUM.value])
    loc_info["delete"] = int(tmp_loc_delete[LOC.SUM.value])

fig = make_subplots(rows=smr_num, cols=2, subplot_titles=df_smr_info["SMR_No"])
fig.add_trace(go.Bar(x=df_smr_info["Actual_WorkTime"], y=smr_no[loop_index], orientation="h", text=df_smr_info["Actual_WorkTime"], name="Actual Work Time(" + smr_no[loop_index] + ")", offsetgroup=1), row=1, col=1)
fig.add_trace(go.Bar(x=df_smr_info["Remaining_WorkTime"], y=smr_no[loop_index], orientation="h", text=df_smr_info["Remaining_WorkTime"], name="Remaining Work Time(" + smr_no[loop_index] + ")", offsetgroup=1, base=df_smr_info["Actual_Work_Time"]), row=1, col=1)
fig.add_trace(go.Bar(x=df_smr_info["Planned_WorkTime"], y=smr_no[loop_index], orientation="h", text=df_smr_info["Planned_WorkTime"], name="Planned Work Time(" + smr_no[loop_index] + ")", offsetgroup=2), row=1, col=1)

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

# fig.add_trace(go.Bar(x=df_smr_info["Actual_Working_Time"], y=["SMR-XXXXX-00002"], orientation="h", text=df_smr_info["Actual_Working_Time"], name="Actual Working Time(SMR-XXXXX-00002)", offsetgroup=1), row=2, col=1)
# fig.add_trace(go.Bar(x=df_smr_info["Remaining_Working_Time"], y=["SMR-XXXXX-00002"], orientation="h", text=df_smr_info["Remaining_Working_Time"], name="Remaining Working Time(SMR-XXXXX-00002)", offsetgroup=1, base=df_smr_info["Actual_Working_Time"]), row=2, col=1)
# fig.add_trace(go.Bar(x=df_smr_info["Planned_Working_Time"], y=["SMR-XXXXX-00002"], orientation="h", text=df_smr_info["Planned_Working_Time"], name="Planned Working Time(SMR-XXXXX-00002)", offsetgroup=2), row=2, col=1)

# fig.add_trace(
#     go.Scatter(
#         mode="lines+markers",
#         x=["2023/11/1", "2023/11/2", "2023/11/3", "2023/11/4", "2023/11/5", "2023/11/6", "2023/11/7"],
#         y=[160.00, 130.00, 100.00, 70.00, 40.00, 10.00, 0.00],
#         name="Expected Remaining Working Time(SMR-XXXXX-00002)",
#         line=dict(color="red", dash="dot"),
#         marker=dict(symbol="circle"),
#     ), row=2, col=2
# )
# fig.add_trace(
#     go.Scatter(
#         mode="lines+markers",
#         x=["2023/11/1", "2023/11/2", "2023/11/3", "2023/11/4", "2023/11/5", "2023/11/6", "2023/11/7"],
#         y=[160.00, 150.00, 130.00, 100.00, 60.00, 10.00, 0.00],
#         name="Actual Remaining Working Time(SMR-XXXXX-00002)",
#         line=dict(color="blue", dash="solid"),
#         marker=dict(symbol="circle"),
#     ), row=2, col=2
# )

# fig.add_trace(go.Bar(x=df_smr_info["Actual_Working_Time"], y=["SMR-XXXXX-00003"], orientation="h", text=df_smr_info["Actual_Working_Time"], name="Actual Working Time(SMR-XXXXX-00003)", offsetgroup=1), row=3, col=1)
# fig.add_trace(go.Bar(x=df_smr_info["Remaining_Working_Time"], y=["SMR-XXXXX-00003"], orientation="h", text=df_smr_info["Remaining_Working_Time"], name="Remaining Working Time(SMR-XXXXX-00003)", offsetgroup=1, base=df_smr_info["Actual_Working_Time"]), row=3, col=1)
# fig.add_trace(go.Bar(x=df_smr_info["Planned_Working_Time"], y=["SMR-XXXXX-00003"], orientation="h", text=df_smr_info["Planned_Working_Time"], name="Planned Working Time(SMR-XXXXX-00003)", offsetgroup=2), row=3, col=1)

# fig.add_trace(
#     go.Scatter(
#         mode="lines+markers",
#         x=["2023/11/1", "2023/11/2", "2023/11/3", "2023/11/4", "2023/11/5", "2023/11/6", "2023/11/7"],
#         y=[200.00, 190.00, 170.00, 140.00, 100.00, 50.00, 0.00],
#         name="Expected Remaining Working Time(SMR-XXXXX-00003)",
#         line=dict(color="red", dash="dot"),
#         marker=dict(symbol="circle"),
#     ), row=3, col=2
# )
# fig.add_trace(
#     go.Scatter(
#         mode="lines+markers",
#         x=["2023/11/1", "2023/11/2", "2023/11/3", "2023/11/4", "2023/11/5", "2023/11/6", "2023/11/7"],
#         y=[200.00, 190.00, 180.00, 170.00, 130.00, 80.00, 40.00],
#         name="Actual Remaining Working Time(SMR-XXXXX-00003)",
#         line=dict(color="blue", dash="solid"),
#         marker=dict(symbol="circle"),
#     ), row=3, col=2
# )

app = dash.Dash(__name__)

app.layout = html.Div([
    html.H4('SMR Working Time Report'),
    html.P(id='table_out_smr_info'),
    dash.dash_table.DataTable(
        id='table_in_smr_info',
        columns=[{"name": i, "id": i}
                 for i in df_smr_info.columns],
        data=df_smr_info.to_dict('records'),
        filter_action="native",
        row_selectable="multi",
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
