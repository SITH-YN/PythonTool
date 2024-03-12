# -*- coding: utf-8 -*-

"""Dash App."""
# Run this app with `python sample.py` and
# visit http://127.0.0.1:8050/ in your web browser.

# Standard Library
import csv
import datetime
import glob
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
csvfile_path_list = []
csvfile_path = ""
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
csvfile_path_list = glob.glob(r"../data/SMR_工数データ/csv/Diag/工数集計_*.csv")
csvfile_path = csvfile_path_list[0].replace("\\", "/")
df_smr_info = pd.read_csv(csvfile_path, encoding="shift_jis")  # encoding="utf-8"
df_smr_info.replace({"SMR開始日": {"/": "-"}, "SMR Fix": {"/": "-"}}, regex=True, inplace=True)

app = dash.Dash(__name__)

# レイアウト作成
app.layout = html.Div([
    html.H4("SMR Working Time Report"),
    html.Button(id="reload_button", n_clicks=0, children="Reload"),
    dash.dash_table.DataTable(
        id="table_smr_info",
        columns=[{"name": i, "id": i}
                 for i in df_smr_info.columns],
        data=df_smr_info.to_dict("records"),
        filter_action="native",
        row_selectable="multi",
        selected_rows=[],
        selected_row_ids=[],
        row_deletable=True,
        sort_action="native",
        sort_mode="multi",
        style_cell=dict(textAlign="left"),
        style_header=dict(backgroundColor="paleturquoise"),
        style_data=dict(backgroundColor="lavender"),
    ),
    dcc.Graph(id="graph_work_time")
])


@app.callback(
    Output("graph_work_time", "figure"),
    Input("table_smr_info", "selected_row_ids"),
    Input("table_smr_info", "selected_rows"),
    Input("reload_button", "n_clicks")
)
def update_graphs(n_clicks, selected_row_ids, selected_rows):
    # Define Local Variable

    # if (n_clicks != 0):
    if selected_row_ids is None:
        df_update_smr_info = df_smr_info
        # pandas Series works enough like a list for this to be OK
        selected_row_ids = df_smr_info["id"]
    else:
        df_update_smr_info = df_smr_info.loc[selected_row_ids]

    # SMR数カウント&リストに格納
    # データフレームの行数取得処理
    # ヘッダ行からカウントするため0行スタートのため-1の必要なし
    smr_num = df_update_smr_info.shape[0]
    if (smr_num < 1):
        smr_num = 1

    # DataFrameの種類（列）に応じて全行分のデータをリスト格納
    smr_no_list = df_update_smr_info["SMR"].tolist()
    act_worktime_list = df_update_smr_info["実績工数"].tolist()
    remain_worktime_list = df_update_smr_info["残工数"].tolist()
    plan_worktime_list = df_update_smr_info["見積工数"].tolist()
    smr_start_day_list = df_update_smr_info["SMR開始日"].tolist()
    smr_end_day_list = df_update_smr_info["SMR Fix日"].tolist()
    d_today = datetime.date.today()

    # グラフ描画エリア設定
    # 行：SMR数分 列：2種類のグラフ表示
    fig = make_subplots(rows=smr_num, cols=GRAPH_NUM, subplot_titles=["Work Time[h]", "Remain Work Time[h]"])

    i = 0
    current_row = ROW_INIT
    for smr_no in smr_no_list:
        # SMR予実（棒グラフ）
        fig.add_trace(go.Bar(x=[act_worktime_list[i]], y=[smr_no], orientation="h", text=act_worktime_list[i], marker={"color": "HotPink"}, name="Actual Working Time(" + smr_no + ")", offsetgroup=1), row=current_row, col=COLUMN_BAR_GRAPH)
        fig.add_trace(go.Bar(x=[remain_worktime_list[i]], y=[smr_no], orientation="h", text=remain_worktime_list[i], marker={"color": "Aqua"}, name="Remaining Working Time(" + smr_no + ")", offsetgroup=1, base=act_worktime_list[i]), row=current_row, col=COLUMN_BAR_GRAPH)
        fig.add_trace(go.Bar(x=[plan_worktime_list[i]], y=[smr_no], orientation="h", text=plan_worktime_list[i], marker={"color": "LightGreen"}, name="Planned Working Time(" + smr_no + ")", offsetgroup=2), row=current_row, col=COLUMN_BAR_GRAPH)
        # 残作業工数（折れ線グラフ）
        fig.add_trace(go.Scatter(mode="lines", x=[d_today, d_today], y=[plan_worktime_list[i], MIN_WORKTIME], name="Today", line=dict(color="black", dash="dot")), row=current_row, col=COLUMN_LINE_GRAPH)
        fig.add_trace(go.Scatter(mode="lines+markers", x=[smr_start_day_list[i], smr_end_day_list[i]], y=[plan_worktime_list[i], MIN_WORKTIME], name="Expected Remaining Working Time(" + smr_no + ")", line=dict(color="red", dash="solid"), marker=dict(symbol="circle")), row=current_row, col=COLUMN_LINE_GRAPH)
        fig.add_trace(go.Scatter(mode="lines+markers", x=[smr_start_day_list[i], d_today], y=[plan_worktime_list[i], remain_worktime_list[i]], name="Actual Remaining Working Time(" + smr_no + ")", line=dict(color="blue", dash="solid"), marker=dict(symbol="circle")), row=current_row, col=COLUMN_LINE_GRAPH)

        current_row += 1
        i += 1
    return (fig)


if __name__ == '__main__':
    app.run_server(debug=True, use_reloader=True)
    webbrowser.open_new_tab("http://127.0.0.1:8050/")
