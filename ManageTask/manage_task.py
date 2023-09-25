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
import openpyxl
import pandas as pd
import plotly.express as px
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
    ROOT_DIR = "C:/git/PythonTool/ManageTask/data/"
    PROJECT_PROGRESS_CSV_DIR = "ProjectProgress/csv/"
    PROJECT_PROGRESS_HTML_DIR = "ProjectProgress/html/"
    TEAM_RESOURCE_CSV_DIR = "TeamResource/csv/"
    TEAM_RESOURCE_HTML_DIR = "TeamResource/html/"

    # Define Local Variable
    date_today = ""
    team_dir = []
    target_team = ""
    target_smr = ""
    project_progress_csv_path = ""
    project_progress_html_path = ""
    team_resource_csv_path = ""
    team_resource_html_path = ""

    # 処理開始
    print("\n-----Start Manage Task-----\n")

    date_today = datetime.datetime.today()

    # WBSのExcelファイルからCSVデータ生成（SMR単位のプロジェクト進捗/Team単位のリソース情報）
    # ※CSVデータ生成時は重複項目の値のマージが必要
    # ACTION_ITEMが同一のものはマージする（項目に応じてデータ修正処理は異なる）

    # Team数分ループ（ルートフォルダ直下のTeamフォルダ数で判定）
    files = os.listdir(ROOT_DIR)
    team_dir = [f for f in files if os.path.isdir(os.path.join(ROOT_DIR, f))]
    print("\nTarget Team List\n", team_dir)

    for team in team_dir:
        target_team = team
        print("Target Team:", target_team)

        # SMR数分ループ（ProjectProgressフォルダ配下のCSVファイル数で判定）
        target_project_progress_csv_dir = ROOT_DIR + target_team + "/" + PROJECT_PROGRESS_CSV_DIR
        project_progress_csv_file_list = os.listdir(target_project_progress_csv_dir)

        for smr in project_progress_csv_file_list:
            # *.csv拡張子削除
            target_smr = os.path.splitext(os.path.basename(smr))[0]
            print("Target SMR:", target_smr)

            # Project Progress情報作成
            # 入力CSVファイルパス/出力HTMLファイルパス設定
            project_progress_csv_path = target_project_progress_csv_dir + target_smr + ".csv"
            project_progress_html_path = ROOT_DIR + target_team + "/" + PROJECT_PROGRESS_HTML_DIR + target_smr + ".html"

            # 出力HTMLファイルが既に存在している場合は削除
            if os.path.isfile(project_progress_html_path) is True:
                os.remove(project_progress_html_path)

            # Team\ProjectProgressフォルダのCSVファイルからDataFrame作成
            plot_project_progress(date_today, target_smr, project_progress_csv_path, project_progress_html_path)

        # Team Resource情報作成
        # 入力CSVファイルパス/出力HTMLファイルパス設定
        team_resource_csv_path = ROOT_DIR + target_team + "/" + TEAM_RESOURCE_CSV_DIR + target_team + "_resource.csv"
        team_resource_html_path = ROOT_DIR + target_team + "/" + TEAM_RESOURCE_HTML_DIR + target_team + "_resource.html"

        # 出力HTMLファイルが既に存在している場合は削除
        if os.path.isfile(team_resource_html_path) is True:
            os.remove(team_resource_html_path)

        # Team\TeamResourceフォルダのCSVファイルからDataFrame作成
        plot_team_resource(date_today, target_team, team_resource_csv_path, team_resource_html_path)

    # 処理終了
    print("\n-----End Manage Task-----\n")


def plot_project_progress(date, smr, csv_path, html_path):
    """Plot Project Progress."""
    # Refer Global Variable

    # Define Local Constant

    # Define Local Variable

    # Plot Project Progress処理開始
    print("\n-----Start Plot Project Progress-----\n")
    df_project_progress = pd.read_csv(csv_path, encoding="shift_jis", header=0)
    discrete_map_progress = {"進捗率：0%": "#FF0000", "進捗率：10%": "#FF4500", "進捗率：20%": "#FF8C00", "進捗率：30%": "#FFA500", "進捗率：40%": "#FFFF00", "進捗率：50%": "#ADFF2F", "進捗率：60%": "#7CFC00", "進捗率：70%": "#00FF00", "進捗率：80%": "#32CD32", "進捗率：90%":  "#228B22", "進捗率：100%": "#008000"}
    fig_project_progress = px.timeline(df_project_progress, x_start="START", x_end="FINISH", y="PROCESS", color="PROGRESS", color_discrete_map=discrete_map_progress, hover_name="PROGRESS", title=smr)
    fig_project_progress.update_layout(
        barmode="group",
        xaxis=dict(
            rangeselector=dict(
                buttons=list([
                    dict(count=1, label="1m", step="month", stepmode="backward"),
                    dict(count=3, label="3m", step="month", stepmode="backward"),
                    dict(count=6, label="6m", step="month", stepmode="backward"),
                    dict(count=1, label="1y", step="year", stepmode="backward"),
                    dict(count=1, label="YTD", step="year", stepmode="todate"),
                    dict(step="all")
                ])
            ),
            # rangeslider=dict(visible=True),
            type="date",
            tickformat="%Y/%m/%d",
            dtick="D1"
        )
    )
    fig_project_progress.update_layout(shapes=[
        dict(
            type="line",
            yref="paper", y0=0, y1=1,
            xref="x", x0=date, x1=date
        )
    ])
    fig_project_progress.update_yaxes(autorange="reversed")
    pio.write_html(fig_project_progress, html_path)
    print("\n-----End Plot Project Progress-----\n")


def plot_team_resource(date, team, csv_path, html_path):
    """Plot Project Progress."""
    # Refer Global Variable

    # Define Local Constant

    # Define Local Variable

    print("\n-----Start Plot Team Resource-----\n")
    df_team_resource = pd.read_csv(csv_path, encoding="shift_jis", header=0)
    fig_team_resource = px.timeline(df_team_resource, x_start="START", x_end="FINISH", y="MEMBER", color="SMR", hover_name="PROCESS", title=team)
    fig_team_resource.update_layout(
        barmode="group",
        xaxis=dict(
            rangeselector=dict(
                buttons=list([
                    dict(count=1, label="1m", step="month", stepmode="backward"),
                    dict(count=3, label="3m", step="month", stepmode="backward"),
                    dict(count=6, label="6m", step="month", stepmode="backward"),
                    dict(count=1, label="1y", step="year", stepmode="backward"),
                    dict(count=1, label="YTD", step="year", stepmode="todate"),
                    dict(step="all")
                ])
            ),
            # rangeslider=dict(visible=True),
            type="date",
            tickformat="%Y/%m/%d",
            dtick="D1"
        )
    )
    fig_team_resource.update_layout(shapes=[
        dict(
            type="line",
            yref="paper", y0=0, y1=1,
            xref="x", x0=date, x1=date
        )
    ])
    fig_team_resource.update_yaxes(autorange="reversed")
    pio.write_html(fig_team_resource, html_path)
    print("\n-----End Plot Team Resource-----\n")


if __name__ == "__main__":
    main()
