"""Manage Task."""

# Standard Library
import csv
import datetime
# import enum
import os
# import re
import shutil
# import subprocess
# from tkinter import filedialog

# 3rd partyライブラリ
from dash import Dash, html, dcc
from plotly.subplots import make_subplots
import openpyxl
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import plotly.io as pio


# Define Global Constant
NORMAL = 0
ERROR = 1

# Define Global Variable


# Define Function
def main():
    """Call Main function."""
    # Refer Global Variable

    # Define Local Constant
    ROOT_DIR = "C:/git/PythonTool/ManageTask/"

    # Define Local Variable
    date_today = ""
    smr_progress_csv_path = ""
    smr_worktime_csv_path = ""
    smr_html_path = ""

    # 処理開始
    print("\n-----Start Manage Task-----\n")

    date_today = datetime.datetime.today()

    # Project Progress情報作成
    # 入力CSVファイルパス/出力HTMLファイルパス設定
    smr_progress_csv_path = ROOT_DIR + "csv/SMR-xxxx-xxxxx/Progress.csv"
    smr_worktime_csv_path = ROOT_DIR + "csv/SMR-xxxx-xxxxx/WorkTime.csv"
    smr_html_path = ROOT_DIR + "html/SMR-xxxx-xxxxx/SMR_INFO.html"

    # 出力HTMLファイルが既に存在している場合は削除
    if os.path.isfile(smr_html_path) is True:
        os.remove(smr_html_path)

    # CSVファイルからDataFrame作成
    df_smr_progress = generate_dataframe(smr_progress_csv_path)
    df_smr_worktime = generate_dataframe(smr_worktime_csv_path)

    # グラフ描画/HTMLファイル出力
    plot_graph_html(smr_html_path, df_smr_progress, df_smr_worktime)
    # plot_project_progress(date_today, project_progress_csv_path, project_progress_html_path)

    # 処理終了
    print("\n-----End Manage Task-----\n")


def generate_dataframe(csv_path):
    """Generate DataFrame From CSV File."""
    # Refer Global Variable

    # Define Local Constant

    # Define Local Variable

    # DataFrame生成処理
    df = pd.read_csv(csv_path, encoding="shift_jis", header=0)

    return df


def plot_graph_html(html_path, df_progress, df_worktime):
    """Plot Graph HTML."""
    # Refer Global Variable

    # Define Local Constant

    # Define Local Variable

    # Plot data処理開始
    print("\n-----Start Plot Project Progress-----\n")
    # fig_project_progress = px.bar(df_project_progress, x="PROGRESS", y="TASK", color="TASK", hover_name="PROGRESS", orientation="h")
    # discrete_map_progress = {"進捗率：0%": "#FF0000", "進捗率：10%": "#FF4500", "進捗率：20%": "#FF8C00", "進捗率：30%": "#FFA500", "進捗率：40%": "#FFFF00", "進捗率：50%": "#ADFF2F", "進捗率：60%": "#7CFC00", "進捗率：70%": "#00FF00", "進捗率：80%": "#32CD32", "進捗率：90%":  "#228B22", "進捗率：100%": "#008000"}
    # fig_project_progress = px.timeline(df_project_progress, x_start="START", x_end="FINISH", y="TASK", color="PROGRESS", color_discrete_map=discrete_map_progress, hover_name="PROGRESS", title=smr)
    # fig_project_progress = px.timeline(df_project_progress, x_start="START", x_end="FINISH", y="TASK", color="MEMBER", hover_name="PROGRESS", title=smr)
    # fig_project_progress.update_layout(
    # fig_project_progress.update_layout(
    #     barmode="group",
    #     xaxis=dict(
    #         rangeselector=dict(
    #             buttons=list([
    #                 dict(count=1, label="1m", step="month", stepmode="backward"),
    #                 dict(count=3, label="3m", step="month", stepmode="backward"),
    #                 dict(count=6, label="6m", step="month", stepmode="backward"),
    #                 dict(count=1, label="1y", step="year", stepmode="backward"),
    #                 dict(count=1, label="YTD", step="year", stepmode="todate"),
    #                 dict(step="all")
    #             ])
    #         ),
    #         # rangeslider=dict(visible=True),
    #         type="date",
    #         tickformat="%Y/%m/%d",
    #         dtick="D1"
    #     )
    # )
    # fig_project_progress.update_layout(shapes=[
    #     dict(
    #         type="line",
    #         yref="paper", y0=0, y1=1,
    #         xref="x", x0=date, x1=date
    #     )
    # ])
    # fig_project_progress.update_yaxes(autorange="reversed")

    subplots_fig = make_subplots(rows=2, cols=1)
    subplots_fig.add_trace(go.Bar(x=df_progress["PROGRESS"], y=df_worktime["TASK"], orientation="h"), row=1, col=1)
    subplots_fig.update_xaxes(rangemode="tozero", title="PROGRESS[%]", row=1, col=1)
    subplots_fig.update_yaxes(autorange="reversed", title="TASK", row=1, col=1)

    # Make traces for graph
    trace1 = go.Bar(x=df_worktime["PLANNED_WORK_TIME"], y=df_worktime["TASK"], xaxis="x3", yaxis="y3", marker=dict(color='#0099ff'), name="PLANNED WORK TIME", orientation="h")
    trace2 = go.Bar(x=df_worktime["ACTUAL_WORK_TIME"], y=df_worktime["TASK"], xaxis="x3", yaxis="y3", marker=dict(color='#404040'), name="ACTUAL WORK TIME", orientation="h")
    trace3 = go.Bar(x=df_worktime["ESTIMATED_WORK_TIME"], y=df_worktime["TASK"], xaxis="x3", yaxis="y3", marker=dict(color='#404040'), name="ESTIMATED WORK TIME", orientation="h")
    # grouped_fig = go.Figure([trace1, trace2, trace3])
    # subplots_fig.add_traces(grouped_fig, row=2, col=1)
    subplots_fig.add_traces([trace1, trace2, trace3])
    # subplots_fig.add_trace(go.Bar(x=df_worktime["PLANNED_WORK_TIME"], y=df_worktime["TASK"], orientation="h"), row=2, col=1)
    subplots_fig.update_xaxes(rangemode="tozero", title="WORK TIME[h]", row=2, col=1)
    subplots_fig.update_yaxes(autorange="reversed", title="TASK", row=2, col=1)

    pio.write_html(subplots_fig, html_path)
    # pio.write_html(fig_project_progress, html_path)
    print("\n-----End Plot Project Progress-----\n")


if __name__ == "__main__":
    main()
