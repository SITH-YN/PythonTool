# -*- coding: utf-8 -*-

"""Dash App."""
# Run this app with `python sample.py` and
# visit http://127.0.0.1:8050/ in your web browser.

# Standard Library
import csv
import datetime
import os
import shutil
import tkinter

# 3rd Party Library
import openpyxl
import win32com.client

import dash
# import dash_daq as daq
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
# from IPython.display import Image
import webbrowser

# Global Constant Define
GRAPH_NUM = 2
ROW_INIT = 1
COLUMN_BAR_GRAPH = 1
COLUMN_LINE_GRAPH = 2
MIN_WORKTIME = 0.00

# Global Variable
smr_num = 0
smr_no_list = []
act_worktime_list = []
remain_worktime_list = []
plan_worktime_list = []
smr_start_day_list = []
smr_end_day_list = []
d_today = ""
i = 0
current_row = ROW_INIT

# Get Data From CSV File
df_smr_info = pd.read_csv("../data/SMR_info.csv", encoding="utf-8")  # encoding="shift_jis"
df_smr_info.replace({"SMR START": {"/": "-"}, "SMR Fix": {"/": "-"}}, regex=True, inplace=True)

# SMR数カウント&リストに格納
# データフレームの行数取得処理
# ヘッダ行からカウントするため0行スタートのため-1の必要なし
smr_num = df_smr_info.shape[0]

# DataFrameの種類（列）に応じて全行分のデータをリスト格納
smr_no_list = df_smr_info["SMR No"].tolist()
act_worktime_list = df_smr_info["Actual Working Time[h]"].tolist()
remain_worktime_list = df_smr_info["Remain Working Time[h]"].tolist()
plan_worktime_list = df_smr_info["Planned Working Time[h]"].tolist()
smr_start_day_list = df_smr_info["SMR START"].tolist()
smr_end_day_list = df_smr_info["SMR Fix"].tolist()
d_today = datetime.date.today()

# グラフ描画エリア設定
# 行：SMR数分 列：2種類のグラフ表示
fig = make_subplots(rows=smr_num, cols=GRAPH_NUM, subplot_titles=["Work Time[h]", "Remain Work Time[h]"])

for smr_no in smr_no_list:
    # SMR予実（棒グラフ）
    fig.add_trace(go.Bar(x=[act_worktime_list[i]], y=[smr_no], orientation="h", text=act_worktime_list[i], name="Actual Working Time(" + smr_no + ")", offsetgroup=1), row=current_row, col=COLUMN_BAR_GRAPH)
    fig.add_trace(go.Bar(x=[remain_worktime_list[i]], y=[smr_no], orientation="h", text=remain_worktime_list[i], name="Remaining Working Time(" + smr_no + ")", offsetgroup=1, base=act_worktime_list[i]), row=current_row, col=COLUMN_BAR_GRAPH)
    fig.add_trace(go.Bar(x=[plan_worktime_list[i]], y=[smr_no], orientation="h", text=plan_worktime_list[i], name="Planned Working Time(" + smr_no + ")", offsetgroup=2), row=current_row, col=COLUMN_BAR_GRAPH)
    # 残作業工数（折れ線グラフ）
    fig.add_trace(
        go.Scatter(
            mode="lines+markers",
            x=[smr_start_day_list[i], smr_end_day_list[i]],
            y=[plan_worktime_list[i], MIN_WORKTIME],
            name="Expected Remaining Working Time(" + smr_no + ")",
            line=dict(color="red", dash="dot"),
            marker=dict(symbol="circle"),
        ), row=current_row, col=COLUMN_LINE_GRAPH
    )
    fig.add_trace(
        go.Scatter(
            mode="lines+markers",
            x=[smr_start_day_list[i], d_today],
            y=[plan_worktime_list[i], remain_worktime_list[i]],
            name="Actual Remaining Working Time(" + smr_no + ")",
            line=dict(color="blue", dash="solid"),
            marker=dict(symbol="circle"),
        ), row=current_row, col=COLUMN_LINE_GRAPH
    )
    # Issue:基準線を引く
    current_row += 1
    i += 1

app = dash.Dash(__name__)

# Issue:SMR一覧情報/グラフから任意のSMRを非表示可能にする
# https://dash.plotly.com/datatable/interactivity
app.layout = html.Div([
    html.H4('SMR Working Time Report'),
    html.P(id='table_out_smr_info'),
    dash.dash_table.DataTable(
        id='table_in_smr_info',
        columns=[{"name": i, "id": i}
                 for i in df_smr_info.columns],
        data=df_smr_info.to_dict('records'),
        row_selectable="multi",
        row_deletable=True,
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
# Input('table_in_smr_info', 'del_rows'))
def update_graphs(active_cell):
    """Update Graphs."""
    if active_cell:
        cell_data = df_smr_info.iloc[active_cell['row']][active_cell['column_id']]
        return f"Data: \"{cell_data}\" from table cell: {active_cell}"
    return "Click the table"
# def update_graphs(del_rows):
#     """Update Graphs."""
#     if del_rows:
#         dcc.Graph(figure=fig)


if __name__ == '__main__':
    app.run_server(debug=True, use_reloader=True)
    webbrowser.open_new_tab("http://127.0.0.1:8050/")
