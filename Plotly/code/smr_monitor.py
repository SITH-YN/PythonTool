# -*- coding: utf-8 -*-

"""Dash App."""
# Run this app with `python smr_monitor.py` and
# visit http://127.0.0.1:8050/ in your web browser.

# Standard Library
# import csv
import datetime
import glob
# import os
# import shutil
# import time
# import tkinter

# 3rd Party Library
# import bs4
# from bs4 import BeautifulSoup
import dash
# import dash_daq
# import json
# import numpy as np
# import openpyxl
import pandas as pd
import plotly
# import plotly.graph_objects as go
# import plotly.express as px
from plotly.subplots import make_subplots
# import webbrowser
# import win32com.client

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
csvfile_path_list = glob.glob(r"./*.csv")
csvfile_path = csvfile_path_list[0].replace("\\", "/")
df_smr_info = pd.read_csv(csvfile_path, encoding="shift_jis")  # encoding="utf-8"
df_smr_info.replace({"SMR開始日": {"/": "-"}, "SMR Fix日": {"/": "-"}}, regex=True, inplace=True)

app = dash.Dash(__name__)

# レイアウト作成
app.layout = dash.html.Div([
    dash.html.H4("SMR Working Time Monitor"),
    # dash_daq.PowerButton(id="power_button", on=False, size=10, color="green"),
    dash.html.Button(id="reload_button", n_clicks=0, children="Reload"),
    dash.dash_table.DataTable(
        id="table_smr_info",
        columns=[{"name": i, "id": i}
                 for i in df_smr_info.columns],
        data=df_smr_info.to_dict("records"),
        editable=True,
        filter_action="native",
        fixed_rows={"headers": True},
        page_size=30,
        row_deletable=False,
        row_selectable="multi",
        selected_rows=[],
        selected_row_ids=[],
        sort_action="native",
        sort_mode="multi",
        style_cell=dict(textAlign="left"),
        style_header=dict(backgroundColor="paleturquoise"),
        style_data=dict(backgroundColor="lavender"),
        style_data_conditional=[
                {"if": {"column_id": "着地予想工数", "filter_query": "{着地予想%} <= 100"}, "backgroundColor": "lightgreen"},
                {"if": {"column_id": "着地予想工数", "filter_query": "{着地予想%} > 100"}, "backgroundColor": "yellow"},
                {"if": {"column_id": "着地予想工数", "filter_query": "{着地予想%} > 120"}, "backgroundColor": "#FF3300"},
                {"if": {"column_id": "着地予想%", "filter_query": "{着地予想%} <= 100"}, "backgroundColor": "lightgreen"},
                {"if": {"column_id": "着地予想%", "filter_query": "{着地予想%} > 100"}, "backgroundColor": "yellow"},
                {"if": {"column_id": "着地予想%", "filter_query": "{着地予想%} > 120"}, "backgroundColor": "#FF3300"},
            ],
        style_table={"height": 400, "overflowY": "auto"}
    ),
    dash.dcc.Graph(id="graph_work_time")
])


@app.callback(
    dash.dependencies.Output("graph_work_time", "figure"),
    dash.dependencies.Input("table_smr_info", "selected_row_ids"),
    dash.dependencies.Input("table_smr_info", "selected_rows"),
    # dash.dependencies.Input("power_button", "on")
    dash.dependencies.Input("reload_button", "n_clicks")
)
def update_graphs(n_clicks, selected_row_ids, selected_rows):
    # Define Local Variable

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
        fig.add_trace(plotly.graph_objects.Bar(x=[act_worktime_list[i]], y=[smr_no], orientation="h", text=act_worktime_list[i], marker={"color": "HotPink"}, name="実績工数", offsetgroup=1), row=current_row, col=COLUMN_BAR_GRAPH)
        fig.add_trace(plotly.graph_objects.Bar(x=[remain_worktime_list[i]], y=[smr_no], orientation="h", text=remain_worktime_list[i], marker={"color": "Aqua"}, name="残工数", offsetgroup=1, base=act_worktime_list[i]), row=current_row, col=COLUMN_BAR_GRAPH)
        fig.add_trace(plotly.graph_objects.Bar(x=[plan_worktime_list[i]], y=[smr_no], orientation="h", text=plan_worktime_list[i], marker={"color": "LightGreen"}, name="予定工数", offsetgroup=2), row=current_row, col=COLUMN_BAR_GRAPH)
        # 残作業工数（折れ線グラフ）
        fig.add_trace(plotly.graph_objects.Scatter(mode="lines", x=[d_today, d_today], y=[plan_worktime_list[i], MIN_WORKTIME], name="本日", line=dict(color="black", dash="dot")), row=current_row, col=COLUMN_LINE_GRAPH)
        fig.add_trace(plotly.graph_objects.Scatter(mode="lines+markers", x=[smr_start_day_list[i], smr_end_day_list[i]], y=[plan_worktime_list[i], MIN_WORKTIME], name="予測残工数", line=dict(color="red", dash="solid"), marker=dict(symbol="circle")), row=current_row, col=COLUMN_LINE_GRAPH)
        fig.add_trace(plotly.graph_objects.Scatter(mode="lines+markers", x=[smr_start_day_list[i], d_today], y=[plan_worktime_list[i], remain_worktime_list[i]], name="本日時点残工数", line=dict(color="blue", dash="solid"), marker=dict(symbol="circle")), row=current_row, col=COLUMN_LINE_GRAPH)

        current_row += 1
        i += 1
    return (fig)


if __name__ == '__main__':
    # webbrowser.open_new_tab("http://127.0.0.1:8050/")
    # app.run_server(debug=True, use_reloader=True)
    app.run_server(debug=False, use_reloader=True)
