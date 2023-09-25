"""Dash App."""

from dash import Dash, html, Input, Output, dash_table, dcc, callback
import plotly.express as px
import plotly.graph_objects as go
import pandas as pd

# Get SMR Information From SMR List.xlsx

# Get Data From CSV File
df_smr_info = pd.read_csv("SMR_info.csv")
df_member_info_total = pd.read_csv("MEMBER_Info_Total.csv")
df_member_info_weekly = pd.read_csv("MEMBER_Info_Weekly.csv")

app = Dash(__name__)

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
    dash_table.DataTable(
        id='table_in_smr_info',
        columns=[{"name": i, "id": i}
                 for i in df_smr_info.columns],
        data=df_smr_info.to_dict('records'),
        style_cell=dict(textAlign='left'),
        style_header=dict(backgroundColor="paleturquoise"),
        style_data=dict(backgroundColor="lavender")
    ),
    html.H4('MEMBER WorkTime Report'),
    # ドロップダウンでTotal/Weekly(This Week/Last Week/Next Week)切り替え
    dcc.Dropdown(
        options=[
            {'label': 'Total', 'value': 'TOTAL'},
            {'label': 'This Week', 'value': 'THIS'},
            {'label': 'Last Week', 'value': 'LAST'},
            {'label': 'Next Week', 'value': 'NEXT'},
        ],
        value='TOTAL', style={'width': '30%'}
    ),
    # Total表示
    html.P(id='table_out_member_info_total'),
    dash_table.DataTable(
        id='table_in_member_info_total',
        columns=[{"name": i, "id": i}
                 for i in df_member_info_total.columns],
        data=df_member_info_total.to_dict('records'),
        style_cell=dict(textAlign='left'),
        style_header=dict(backgroundColor="paleturquoise"),
        style_data=dict(backgroundColor="lavender")
    ),
    html.P(id='table_out_member_info_weekly'),
    dash_table.DataTable(
        id='table_in_member_info_weekly',
        columns=[{"name": i, "id": i}
                 for i in df_member_info_weekly.columns],
        data=df_member_info_weekly.to_dict('records'),
        style_cell=dict(textAlign='left'),
        style_header=dict(backgroundColor="paleturquoise"),
        style_data=dict(backgroundColor="lavender")
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
