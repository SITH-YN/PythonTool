import dash
import dash_daq as daq
from dash import dcc
from dash import html
from dash.dash_table import DataTable
from dash.dependencies import Input, Output, State, ALL, ALLSMALLER, MATCH
import json
import plotly
import plotly.graph_objects as go
import plotly.express as px

"""ch05_dash_intro"""
"""dash_concept_first.py"""
# # ➊ Dashインスタンスを生成する
# app = dash.Dash(__name__)

# # ➋ コンポーネントをlayout属性に渡す
# app.layout = html.H1("Hello Dash")

# if __name__ == "__main__":
#     # ➌ アプリケーションを起動する
#     app.run_server(debug=True)


"""dash_concept_first_style.py"""
# app = dash.Dash(__name__)

# app.layout = html.H1(
#     "Hello Dash",
#     # ➊ スタイルを設定する
#     style={"color": "red", "textAlign": "center"},
# )

# if __name__ == "__main__":
#     app.run_server(debug=True)


"""dash_concept_graph.py"""
# app = dash.Dash(__name__)

# app.layout = dcc.Graph(
#     # figure属性にbar関数で作成したfigureを渡す
#     figure=px.bar(x=[1, 2, 3, 4, 5], y=[1, 2, 3, 4, 5])
# )

# if __name__ == "__main__":
#     app.run_server(debug=True)


"""dash_concept_hellodash.py"""
# # ➊ コンポーネントのスタイル設定. 横幅80％,中央寄せにし,上下に5％の余白を作る.
# core_style = {"width": "80%", "margin": "5% auto"}


# app = dash.Dash(__name__)

# # ➋ レイアウトにdivの子要素として3つのコンポーネントを渡す
# app.layout = html.Div(
#     [  # ➌ 見出しを作成する
#         html.H1("Hello Dash", style={"textAlign": "center"}),
#         # ➍ ドロップダウンを作成する
#         dcc.Dropdown(
#             options=[
#                 {"label": "white", "value": "white"},
#                 {"label": "yellow", "value": "yellow"},
#             ],
#             value="white",
#             style=core_style,
#         ),
#         # ➎ グラフを作成する
#         dcc.Graph(
#             figure=px.bar(x=[1, 2, 3, 4, 5], y=[1, 2, 3, 4, 5]), style=core_style,
#         ),
#     ]
# )

# if __name__ == "__main__":
#     app.run_server(debug=True)


"""dash_concept_hello_callback.py"""
# core_style = {"width": "80%", "margin": "5% auto"}

# app = dash.Dash(__name__)

# # ➊ レイアウト
# app.layout = html.Div(
#     [
#         html.H1("Hello Dash", style={"textAlign": "center"}),
#         dcc.Dropdown(
#             # ➌ ID名の追加
#             id="my-dropdown",
#             options=[
#                 {"label": "white", "value": "white"},
#                 {"label": "yellow", "value": "yellow"},
#             ],
#             value="white",
#             style=core_style,
#         ),
#         dcc.Graph(
#             figure=px.bar(x=[1, 2, 3, 4, 5], y=[1, 2, 3, 4, 5]), style=core_style,
#         ),
#     ],
#     # ➍ ID名の追加
#     id="all-components",
# )


# # ➋ コールバック
# @app.callback(
#     # ➍ 戻り値の出力先を指定
#     Output("all-components", "style"),
#     # ➎ コールバックの呼び出し要素の指定
#     Input("my-dropdown", "value"),
# )
# def update_background(selected_value):
#     # ➏ 返り値
#     return {"backgroundColor": selected_value, "padding": "3%"}


# if __name__ == "__main__":
#     app.run_server(debug=True)


"""dash_getting_started_scatter.py"""
# external_stylesheets = ["https://codepen.io/chriddyp/pen/bWLwgP.css"]


# # タイトルとドロップダウンを作成するコンポーネント
# def header_and_dropdown(header_name, columns_name, dropdown_id):
#     return html.Div(
#         [
#             html.H2(header_name),
#             dcc.Dropdown(
#                 id=dropdown_id,
#                 options=[{"label": col, "value": col} for col in columns_name],
#                 value=columns_name[0],
#             ),
#         ],
#         style={"width": "49%", "display": "inline-block"},
#     )


# gapminder = px.data.gapminder()

# app = dash.Dash(__name__, external_stylesheets=external_stylesheets)
# app.layout = html.Div(
#     [
#         html.H1("Gapminder Graph"),
#         html.Div(
#             [
#                 header_and_dropdown("Select X axis", gapminder.columns[3:6], "x_axis"),
#                 header_and_dropdown("Select Y axis", gapminder.columns[3:6], "y_axis"),
#             ]
#         ),
#         dcc.Graph(id="graph"),
#     ]
# )


# # コールバック
# @app.callback(
#     Output("graph", "figure"), Input("x_axis", "value"), Input("y_axis", "value")
# )
# def update_graph(x_axis_value, y_axis_value):
#     return px.scatter(
#         gapminder,
#         x=x_axis_value,
#         y=y_axis_value,
#         color="country",
#         log_x=True,
#         log_y=True,
#     )


# if __name__ == "__main__":
#     app.run_server(debug=True)


"""dash_getting_started_with_table.py"""
# external_stylesheets = ["https://codepen.io/chriddyp/pen/bWLwgP.css"]

# gapminder = px.data.gapminder()

# app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

# app.layout = html.Div(
#     [
#         html.H1("Gapminder Graph"),
#         html.H3("左側のグラフの要素をShift+マウスクリックで複数国が選択できます。"),
#         html.Div(
#             [
#                 dcc.Graph(
#                     id="graph1",
#                     figure=px.scatter(
#                         gapminder,
#                         x="gdpPercap",
#                         y="lifeExp",
#                         size="pop",
#                         color="continent",
#                         animation_frame="year",
#                         log_x=True,
#                         size_max=70,
#                         range_y=[20, 90],
#                         hover_data=["country"],
#                         template={"layout": {"clickmode": "event+select"}},
#                     ),
#                     style={"width": "50%", "display": "inline-block", "height": 600},
#                 ),
#                 html.Div(
#                     [
#                         dcc.Graph(id="graph2", style={"height": 300}),
#                         dcc.Graph(id="graph3", style={"height": 300}),
#                     ],
#                     style={"width": "50%", "display": "inline-block", "height": 600},
#                 ),
#             ]
#         ),
#         html.Div(
#             [DataTable(id="table", export_format="csv", filter_action="native"),],
#             style={"width": "80%", "margin": "auto"},
#         ),
#     ]
# )


# @app.callback(
#     Output("graph2", "figure"),
#     Output("graph3", "figure"),
#     Output("table", "columns"),
#     Output("table", "data"),
#     Input("graph1", "selectedData"),
# )
# def update_graph(selectedData):
#     if selectedData:
#         selected_countries = [data["customdata"][0] for data in selectedData["points"]]
#         selected_df = gapminder[gapminder["country"].isin(selected_countries)]
#         fig1 = px.line(selected_df, x="year", y="pop", color="country", title="各国の人口")
#         fig2 = px.line(
#             selected_df, x="year", y="gdpPercap", color="country", title="各国の1人当たりGDP"
#         )
#         columns = [
#             {"name": col, "id": col, "deletable": True} for col in selected_df.columns
#         ]
#         return fig1, fig2, columns, selected_df.to_dict("records")
#     raise dash.exceptions.PreventUpdate


# if __name__ == "__main__":
#     app.run_server(debug=True)


"""ch06_dash_layout"""
"""dash_layout_dropdown.py"""
# app = dash.Dash(__name__)
# app.layout = dcc.Dropdown()
# app.run_server(debug=True)


"""dash_layout_dropdown_args.py"""
# app = dash.Dash(__name__)
# app.layout = dcc.Dropdown(
#     options=[  # ➊ 選択肢の設定
#         {"label": "赤", "value": "red"},
#         {"label": "黄", "value": "yellow"},
#         {"label": "青", "value": "blue"},
#     ],
#     value="red",  # ➊ 初期値の設定
#     clearable=False,  # ➊ 選択を削除できないように設定
#     style={"textAlign": "center"},  # ➊ 文字を中央に寄せる
# )
# app.run_server(debug=True)


"""dash_layout_style_component.py"""
# app = dash.Dash(__name__)

# app.layout = html.P("こんにちは。昨日は雪が降りました。")

# if __name__ == "__main__":
#     app.run_server(debug=True)


"""ash_layout_component_with_style.py"""
# app = dash.Dash(__name__)

# app.layout = html.P(
#     "こんにちは。昨日は雪が降りました。",
#     # ➊ スタイルの設定
#     style={
#         "fontSize": 50,  # 文字サイズ
#         "color": "white",  # 文字色
#         "backgroundColor": "#000000",  # 背景色
#     },
# )

# if __name__ == "__main__":
#     app.run_server(debug=True)


"""dash_layout_style_margin.py"""
# app = dash.Dash(__name__)

# app.layout = html.P(
#     "こんにちは。昨日は雪が降りました。",
#     # スタイルの設定
#     style={
#         "fontSize": 50,  # フォントサイズ
#         "color": "white",  # 文字色
#         "backgroundColor": "#000000",  # 背景色
#         "width": 400,  # 横幅
#         "margin": "auto",  # ➊ コンポーネントを中央に寄せる
#     },
# )

# if __name__ == "__main__":
#     app.run_server(debug=True)


"""dash_layout_style_two.py"""
# app = dash.Dash(__name__)

# app.layout = html.Div(
#     [
#         html.P(
#             "こんにちは。昨日は雪が降りました。",
#             style={
#                 "fontSize": 50,  # フォントサイズ
#                 "color": "white",  # 文字色
#                 "backgroundColor": "#000000",  # 背景色
#                 "width": "40%",
#                 "display": "inline-block",  # ➊
#             },
#         ),
#         html.P(
#             "こんにちは。今日は晴れました。",
#             style={
#                 "fontSize": 50,  # フォントサイズ
#                 "color": "white",  # 文字色
#                 "backgroundColor": "red",  # 背景色
#                 "width": "40%",
#                 "display": "inline-block",  # ➊
#                 "verticalAlign": "top",  # ➋
#             },
#         ),
#     ]
# )

# if __name__ == "__main__":
#     app.run_server(debug=True)


"""dash_layout_assets_style.py"""
# app = dash.Dash(__name__)

# app.layout = html.Div([html.Div(className="circle")])  # className属性を設定

# if __name__ == "__main__":
#     app.run_server(debug=True)


"""dash_layout_outlink.py"""
# app = dash.Dash(__name__)

# app.layout = html.Div(
#     [html.H1("スタイル"), dcc.Input(placeholder="スタイルシートテスト"), dcc.Graph()]
# )

# if __name__ == "__main__":
#     app.run_server(debug=True)


"""dash_layout_with_outlink.py"""
# 外部スタイルシートの読み込み
# external_stylesheets = ["https://codepen.io/chriddyp/pen/bWLwgP.css"]
# app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

# app.layout = html.Div(
#     [
#         # ➊ 各コンポーネントへのスタイルシートの適用
#         html.H1("スタイル", className="three columns"),
#         dcc.Input(placeholder="スタイルシートテスト", className="three columns"),
#         dcc.Graph(className="six columns"),
#     ]
# )

# if __name__ == "__main__":
#     app.run_server(debug=True)


"""dash_graph_px_gapminder.py"""
# gapminder = px.data.gapminder()
# gapminder2007 = gapminder[gapminder["year"] == 2007]

# app = dash.Dash(__name__)

# app.layout = dcc.Graph(
#     # ➊ 引数figureにPlotly Expressで作成したfigureを直接渡す
#     figure=px.scatter(
#         gapminder2007,  # 利用するデータフレームの設定
#         x="gdpPercap",  # x軸
#         y="pop",  # y軸
#         size="lifeExp",  # マーカサイズ
#         color="continent",  # マーカ色
#         hover_name="country",
#         log_x=True,  # x軸を対数に設定
#         log_y=True,  # y軸を対数に設定
#         title="Gapminder",  # タイトル
#     )
# )

# if __name__ == "__main__":
#     app.run_server(debug=True)


"""dash_graph_go_gapminder.py"""
# gapminder = plotly.data.gapminder()
# gapminder2007 = gapminder[gapminder["year"] == 2007]

# # ➊ figureの作成
# fig = go.Figure()
# for c in gapminder2007.continent.unique():
#     fig.add_trace(
#         go.Scatter(
#             x=gapminder2007.loc[gapminder2007["continent"] == c, "gdpPercap"],
#             y=gapminder2007.loc[gapminder2007["continent"] == c, "pop"],
#             name=c,
#             mode="markers",
#             marker={
#                 "size": gapminder2007.loc[gapminder2007["continent"] == c, "lifeExp"]
#                 / 2
#             },
#             text=gapminder2007.loc[gapminder2007["continent"] == c, "country"],
#         )
#     )
# fig.update_layout(
#     xaxis={"type": "log", "title": "gdpPercap"},
#     yaxis={"type": "log", "title": "pop"},
#     title="Gapminder",
# )


# app = dash.Dash(__name__)

# app.layout = dcc.Graph(
#     # ➋ figureにfigを渡す
#     figure=fig
# )

# if __name__ == "__main__":
#     app.run_server(debug=True)


"""dash_layout_single_div_style.py"""
# app = dash.Dash(__name__)

# app.layout = html.Div(
#     # ➊ 各スタイルを設定
#     style={
#         "width": "500px",  # 横幅: 500px
#         "height": "250px",  # 高さ: 250px
#         "backgroundColor": "lime",  # 背景色: ライム
#         "margin": "50px auto 50px",  # 要素の外側の余白領域 上下50px、autoで中央寄せ
#     }
# )
# if __name__ == "__main__":
#     app.run_server(debug=True)


"""dash_layout_multiple_divs.py"""
# # ➊ 1段目用CSS辞書
# div_style3 = {
#     "width": "40%",
#     "height": "250px",
#     "backgroundColor": "lime",
#     "margin": "5%",
#     "display": "inline-block",
# }

# # ➋ 2段目用CSS辞書
# div_style4 = {
#     "width": "29%",
#     "height": "250px",
#     "backgroundColor": "skyblue",
#     "margin": "2%",
#     "display": "inline-block",
# }

# app = dash.Dash(__name__)

# app.layout = html.Div(
#     [
#         # ➌ 1段目　2つの長方形
#         html.Div(
#             [html.Div(style=div_style3), html.Div(style=div_style3)], id="first_leader"
#         ),
#         # ➍ 2段目　3つの長方形
#         html.Div(
#             [
#                 html.Div(style=div_style4),
#                 html.Div(style=div_style4),
#                 html.Div(style=div_style4),
#             ],
#             id="second_leader",
#         ),
#     ],
#     id="leader",
# )

# if __name__ == "__main__":
#     app.run_server(debug=True)


"""dash_layout_mycss.py"""
# app = dash.Dash(__name__)

# app.layout = html.Div(
#     [
#         html.H1("5つの四角形を並べたアプリケーション"),
#         html.Div(
#             [
#                 html.Div(className="roundsqlime columns"),
#                 html.Div(className="roundsqlime columns"),
#             ]
#         ),
#         html.Div(
#             [
#                 html.Div(className="roundsqblue columns"),
#                 html.Div(className="roundsqblue columns"),
#                 html.Div(className="roundsqblue columns"),
#             ]
#         ),
#     ]
# )


# if __name__ == "__main__":
#     app.run_server(debug=True)


"""dash_layout_stylesheet.py"""
# # ➊ 1段目用CSS辞書
# div_style3 = {"height": "250px", "margin": "5%", "backgroundColor": "lime"}

# # ➋ 2段目用CSS辞書
# div_style4 = {"height": "250px", "backgroundColor": "skyblue"}

# # ➌ スタイルシートの読み込み
# external_sheet = ["https://codepen.io/chriddyp/pen/bWLwgP.css"]
# app = dash.Dash(__name__, external_stylesheets=external_sheet)

# app.layout = html.Div(
#     [
#         html.H1("5つの長方形を並べたアプリケーション"),
#         # ➍ 1段目　2つの長方形
#         html.Div(
#             [
#                 html.Div(style=div_style3, className="five columns"),
#                 html.Div(style=div_style3, className="five columns"),
#             ],
#             id="first_leader",
#         ),
#         # ➎ 2段目　3つの長方形
#         html.Div(
#             [
#                 html.Div(style=div_style4, className="four columns"),
#                 html.Div(style=div_style4, className="four columns"),
#                 html.Div(style=div_style4, className="four columns"),
#             ]
#         ),
#     ]
# )

# if __name__ == "__main__":
#     app.run_server(debug=True)


"""dash_layout_five_components.py"""
# # ➊ スタイルの作成
# div_style = {
#     "width": "40%",
#     "margin": "5%",
#     "display": "inline-block",
#     "verticalAlign": "top",
#     "textAlign": "center",
# }

# div_style2 = {
#     "width": "29%",
#     "margin": "2%",
#     "verticalAlign": "top",
#     "display": "inline-block",
# }

# external_stylesheets = ["https://codepen.io/chriddyp/pen/bWLwgP.css"]
# app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

# # ➋ レイアウトの作成
# # ➌ Divのchildren属性に渡すレイアウト（左上）
# top_left = html.Div(
#     [
#         html.H1("Dashアプリケーション"),
#         dcc.Markdown(
#             """
#             5つのDivクラスの領域に、複数のコンポーネントを並べました。

#             - 左上はH1、Markdown、右上はGraph
#             - 左下はH3、Dropdown、Slider、真ん中下はH3、TextArea、右下はH3、Checklist、RadioItems

#             上記のコンポーネントをDivのchildren属性に渡しました。
#             """,
#             style={
#                 "fontSize": 20,
#                 "textAlign": "left",
#                 "backgroundColor": "lightgrey",
#                 "padding": "3%",
#             },
#         ),
#     ],
#     style=div_style,
# )

# # グラフの作成
# fig = px.line(
#                 x=[1, 2, 3, 4, 5],
#                 y=[[3, 2, 4, 1, 5], [2, 4, 3, 5, 3]],
#                 title="Dash Graph",
#             )
# fig.data[0].name = "東京"
# fig.data[1].name = '大阪'

# # ➌ Divのchildren属性に渡すレイアウト（右上）
# top_right = html.Div(
#     [
#         dcc.Graph(
#             figure= fig 
#         )
#     ],
#     style=div_style,
# )

# # ➌ Divのchildren属性に渡すレイアウト（左下）
# bottom_left = html.Div(
#     [
#         html.H3("ドロップダウン"),
#         dcc.Dropdown(
#             options=[{"label": "東京", "value": "東京"}, {"label": "大阪", "value": "大阪"}],
#             value="大阪",
#         ),
#         html.H3("スライダー"),
#         dcc.Slider(min=-10, max=10, marks={i: f"label{i}" for i in range(-10, 11, 5)}),
#     ],
#     style=div_style2,
# )

# # ➌ Divのchildren属性に渡すレイアウト（中央下）
# bottom_mid = html.Div(
#     [
#         html.H3("テキストエリア入力"),
#         html.Textarea(style={"height": 200, "width": "60%"}),
#         html.Button("ボタン"),
#     ],
#     style=div_style2,
# )

# # ➌ Divのchildren属性に渡すレイアウト（右下）
# bottom_right = html.Div(
#     [
#         html.H3("選択肢", style={"textAlign": "center"}),
#         # 2つのコンポーネントはスタイルシートを活用して横並びに
#         dcc.Checklist(
#             options=[
#                 {"label": "北海道", "value": "北海道"},
#                 {"label": "秋田", "value": "秋田"},
#                 {"label": "新潟", "value": "新潟"},
#             ],
#             value=["北海道", "新潟"],
#             className="five columns",
#         ),
#         dcc.RadioItems(
#             options=[
#                 {"label": "福岡", "value": "福岡"},
#                 {"label": "宮崎", "value": "宮崎"},
#                 {"label": "鹿児島", "value": "鹿児島"},
#             ],
#             value="鹿児島",
#             className="five columns",
#         ),
#     ],
#     style=div_style2,
# )

# app.layout = html.Div(
#     children=[
#         html.Div([top_left, top_right]),
#         html.Div([bottom_left, bottom_mid, bottom_right]),
#     ]
# )

# if __name__ == "__main__":
#     app.run_server(debug=True)


"""ch07_dash_callback"""
"""dash_callback_start.py"""
# external_stylesheets = ["https://codepen.io/chriddyp/pen/bWLwgP.css"]

# app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

# # ➊ レイアウト 各コンポーネントにIDを付ける
# app.layout = html.Div(
#     [
#         # コールバックの返り値を表示する
#         html.H1(id="head-title"),
#         # 文字を入力するテキストエリア
#         dcc.Textarea(
#             id="my-text-state",
#             value="initial value",  # 初期値の設定
#             style={"width": "80%", "fontSize": 30},
#         ),
#         # クリックするとコールバックを呼び出すボタン
#         html.Button(id="my-button", n_clicks=0, children="submit"),
#     ],
#     style={"margin": 50},
# )


# # ➋ コールバックの作成。
# @app.callback(
#     Output("head-title", "children"),  # ➌ 出力項目
#     Input("my-button", "n_clicks"),  # ➍ 入力項目
#     State("my-text-state", "value"),  # ➎ 状態項目
# )
# # ➏ コールバック関数
# def update_title(n_clicks, text_value):
#     return text_value


# if __name__ == "__main__":
#     app.run_server(debug=True)


"""dash_callback_slider.py"""
# app = dash.Dash(__name__)

# # ➊ レイアウト
# app.layout = html.Div(
#     [
#         html.H1(id="callback-output"),
#         # 引数updatemodeに"drag"を渡し,動作を即座に反映するように設定
#         dcc.Slider(id="callback-input", value=0, updatemode="drag"),
#     ],
#     style={"textAlign": "center", "width": "60%", "margin": "auto"},
# )


# # ➋ コールバック
# @app.callback(
#     # ➌ 出力項目を指定,ID,属性を渡す
#     Output("callback-output", "children"),
#     # ➍ 入力項目を指定,ID,属性を渡す
#     Input("callback-input", "value"),
# )
# # ➎ コールバック関数
# def update_app(num_value):
#     return num_value


# if __name__ == "__main__":
#     app.run_server(debug=True)


"""dash_callback_tips.py"""
# # データの読み込み
# tips = px.data.tips()

# dash_stylesheets = ["https://codepen.io/chriddyp/pen/bWLwgP.css"]
# app = dash.Dash(__name__, external_stylesheets=dash_stylesheets)

# # ➊ レイアウトの作成
# app.layout = html.Div(
#     [
#         # ➌ 指定したグラフに応じてグラフのタイトルを変更
#         html.H3(id="title", style={"textAlign": "center"}),
#         html.Div(
#             [
#                 html.Div(
#                     [
#                         html.H4("曜日選択"),
#                         # ➍ 曜日選択のドロップダウンの作成
#                         dcc.Dropdown(
#                             id="day_selector",
#                             options=[
#                                 {"value": dow, "label": dow}
#                                 for dow in tips.day.unique()
#                             ],
#                             multi=True,
#                             value=["Thur", "Fri", "Sat", "Sun"],
#                         ),
#                     ],
#                     className="six columns",
#                 ),
#                 html.Div(
#                     [
#                         html.H4("グラフ選択"),
#                         # ➎ グラフ選択のドロップダウンの作成
#                         dcc.Dropdown(
#                             id="graph_selector",
#                             options=[
#                                 {"value": "bar", "label": "bar"},
#                                 {"value": "scatter", "label": "scatter"},
#                             ],
#                             value="bar",
#                         ),
#                     ],
#                     className="six columns",
#                 ),
#             ],
#             style={"padding": "2%", "margin": "auto"},
#         ),
#         # ➏ グラフの表示場所
#         html.Div(
#             [
#                 dcc.Graph(id="app_graph", style={"padding": "3%"}),
#             ],
#             style={"padding": "3%", "marginTop": 50},
#         ),
#     ]
# )


# # ➋ コールバックの作成
# @app.callback(
#     # ➐ Outputインスタンス,Inputインスタンスの順に配置
#     Output("title", "children"),
#     Output("app_graph", "figure"),
#     Input("day_selector", "value"),
#     Input("graph_selector", "value"),
# )
# def update_graph(selected_days, selected_graph):
#     # ➑ データフレームの作成
#     selected_df = tips[tips["day"].isin(selected_days)]
#     # ➒ 選択されたグラフの種類により、タイトル表示データとグラフを作成
#     if selected_graph == "scatter":
#         title = "テーブル毎データ（散布図）"
#         figure = px.scatter(
#             selected_df, x="total_bill", y="tip", color="smoker", height=600
#         )
#     else:
#         title = ("曜日ごとの売り上げ（棒グラフ）",)
#         figure = px.bar(selected_df, x="day", y="total_bill", height=600)
#     return title, figure


# if __name__ == "__main__":
#     app.run_server(debug=True)


"""dash_callback_pmc_all_showdata.py"""
# # gapminderデータを読み込む
# gapminder = px.data.gapminder()

# app = dash.Dash(__name__)

# # ➊ レイアウトの作成
# app.layout = html.Div(
#     [
#         html.Button("PUSH ME", id="add_drop"),  # 新たなドロップダウンを追加するボタン（➋）
#         html.Div(id="show_drop", children=[]),  # ドロップダウンを追加するDiv（➌）
#         html.P(id="my_text"),  # テキストを描画するP（➍）
#     ],
#     style={"width": "80%", "margin": "2% auto"},
# )


# # ➎ コールバック1
# @app.callback(
#     Output("show_drop", "children"),
#     Input("add_drop", "n_clicks"),
#     State("show_drop", "children"),
#     prevent_initial_call=True,  # ➏
# )
# def update_layout(n_clicks, children):
#     new_layout = html.Div(
#         [
#             dcc.Dropdown(
#                 id={"type": "my_dropdown", "index": n_clicks},  # ➐
#                 options=[{"label": c, "value": c} for c in gapminder.country.unique()],
#                 value=gapminder.country.unique()[n_clicks - 1],
#             )
#         ]
#     )
#     children.append(new_layout)  # ➑
#     return children


# # ➒ コールバック2
# @app.callback(
#     Output("my_text", "children"),
#     Input({"type": "my_dropdown", "index": ALL}, "value"),  # ➓
#     prevent_initial_call=True,
# )
# def update_graph(selected_values):
#     # 全てのドロップダウンで選択された国のリストを文字列にする
#     return str(selected_values)


# app.run_server(debug=True)


"""dash_callback_pmc_all.py"""
# # gapminderデータを読み込む
# gapminder = px.data.gapminder()

# app = dash.Dash(__name__)

# # レイアウトの作成
# app.layout = html.Div(
#     [
#         html.Button("PUSH ME", id="my_button"),  # 新たなレイアウトを追加するボタン
#         html.Div(id="my_div", children=[]),  # ドロップダウンを追加するDiv
#         html.Div(id="my_select"),  # 作成したグラフを描画するDiv
#     ]
# )


# # コールバック1
# @app.callback(
#     Output("my_div", "children"),
#     Input("my_button", "n_clicks"),
#     State("my_div", "children"),
#     prevent_initial_call=True,
# )
# def update_layout(n_clicks, children):
#     new_layout = html.Div(
#         [
#             dcc.Dropdown(
#                 id={"type": "my_dropdown", "index": n_clicks},
#                 options=[{"label": c, "value": c} for c in gapminder.country.unique()],
#                 value=gapminder.country.unique()[n_clicks - 1],
#             )
#         ]
#     )
#     children.append(new_layout)
#     return children


# # コールバック2
# @app.callback(
#     Output("my_select", "children"),
#     Input({"type": "my_dropdown", "index": ALL}, "value"),
#     prevent_initial_call=True,
# )
# def update_graph(selected_values):
#     # ➊ 全てのドロップダウンで選択された国名のデータを作成し,可視化する。
#     selected_countries = gapminder[gapminder["country"].isin(selected_values)]
#     return dcc.Graph(
#         figure=px.line(selected_countries, x="year", y="lifeExp", color="country")
#     )


# app.run_server(debug=True)


"""dash_callback_pmc_match_showdata.py"""
# # gapminderデータを読み込む
# gapminder = px.data.gapminder()

# app = dash.Dash(__name__)

# # ➊ レイアウトの作成
# app.layout = html.Div(
#     [
#         html.Button("PUSH ME", id="add_drop"),
#         html.Div(id="show_drop", children=[]),  # ドロップダウンと選択された値が追加されるUI
#     ],
#     style={"width": "80%", "margin": "2% auto"},
# )


# # ➋ コールバック1
# @app.callback(
#     Output("show_drop", "children"),
#     Input("add_drop", "n_clicks"),
#     State("show_drop", "children"),
#     prevent_initial_call=True,
# )
# def update_layout(n_clicks, children):
#     new_layout = html.Div(
#         [
#             dcc.Dropdown(
#                 id={"type": "my_dropdown", "index": n_clicks},
#                 options=[{"label": c, "value": c} for c in gapminder.country.unique()],
#                 value=gapminder.country.unique()[n_clicks - 1],
#             ),  # ➌ 文字列を表示するコンポーネント
#             html.P(id={"type": "text_show", "index": n_clicks}),
#         ]
#     )

#     children.append(new_layout)
#     return children


# # ➍ コールバック2
# @app.callback(
#     Output({"type": "text_show", "index": MATCH}, "children"),  # ➎
#     Input({"type": "my_dropdown", "index": MATCH}, "value"),  # ➏
# )
# def update_graph(selected_values):
#     return str(selected_values)


# app.run_server(debug=True)


"""dash_callback_pmc_match.py"""
# # gapminderデータを読み込む
# gapminder = px.data.gapminder()
# # 横に2つのコンポーネントを並べるためのスタイル
# half_style = {"width": "50%", "display": "inline-block"}

# app = dash.Dash(__name__)

# # 2つのコンポーネントを持つレイアウト
# app.layout = html.Div(
#     [
#         html.Button("PUSH ME", id="add_drop", n_clicks=0),
#         html.Div(id="my_div", children=[]),
#     ]
# )


# # ➊ コールバック1
# @app.callback(
#     Output("my_div", "children"),
#     Input("add_drop", "n_clicks"),
#     State("my_div", "children"),
#     prevent_initial_call=True,
# )
# def update_layout(n_clicks, children):
#     new_layout = html.Div(
#         [
#             dcc.Dropdown(
#                 id={"type": "my_dropdown", "index": n_clicks},
#                 options=[{"label": c, "value": c} for c in gapminder.country.unique()],
#                 value=gapminder.country.unique()[n_clicks - 1],
#             ),
#             dcc.Dropdown(
#                 id={"type": "my_dropdown2", "index": n_clicks},
#                 options=[
#                     {"label": col, "value": col} for col in gapminder.columns[3:6]
#                 ],
#                 value="lifeExp",
#             ),
#             dcc.Graph(id={"type": "my_graph", "index": n_clicks}),
#         ],
#         style=half_style,
#     )  # 横に2つのレイアウトを並べるためstyleを渡す
#     children.append(new_layout)
#     return children


# # ➋コールバック2
# @app.callback(
#     # ➌ indexにMATCHを渡す
#     Output({"type": "my_graph", "index": MATCH}, "figure"),
#     Input({"type": "my_dropdown", "index": MATCH}, "value"),
#     Input({"type": "my_dropdown2", "index": MATCH}, "value"),
# )
# def update_graph(selected_value, selected_col):
#     gap = gapminder[gapminder["country"] == selected_value]
#     return px.line(gap, x="year", y=selected_col)


# app.run_server(debug=True)


"""dash_callback_pmc_allsmaller_showdata.py"""
# # gapminderデータを読み込む
# gapminder = px.data.gapminder()

# app = dash.Dash(__name__)

# # ➊ レイアウトの作成
# app.layout = html.Div(
#     [
#         html.Button("PUSH ME", id="add_drop"),
#         html.Div(id="show_drop", children=[]),  # ドロップダウンと選択された値が追加されるUI
#     ],
#     style={"width": "80%", "margin": "2% auto"},
# )


# # ➋ コールバック1
# @app.callback(
#     Output("show_drop", "children"),
#     Input("add_drop", "n_clicks"),
#     State("show_drop", "children"),
#     prevent_initial_call=True,
# )
# def update_layout(n_clicks, children):
#     new_layout = html.Div(
#         [
#             dcc.Dropdown(
#                 id={"type": "my_dropdown", "index": n_clicks},
#                 options=[{"label": c, "value": c} for c in gapminder.country.unique()],
#                 value=gapminder.country.unique()[n_clicks - 1],
#             ),  # ➌ 文字列を表示するコンポーネント
#             html.P(id={"type": "text_show", "index": n_clicks}),
#         ]
#     )

#     children.append(new_layout)
#     return children


# # コールバック2
# @app.callback(
#     Output({"type": "text_show", "index": MATCH}, "children"),
#     # ➊ IDキー"index"に渡すセレクタをALLSMALLERに更新
#     Input({"type": "my_dropdown", "index": ALLSMALLER}, "value"),
# )
# def update_graph(selected_values):
#     return str(selected_values)


# app.run_server(debug=True)


"""dash_callback_pmc_allsmaller.py"""
# # gapminderデータを読み込む
# gapminder = px.data.gapminder()
# # 横に2つのコンポーネントを並べるためのスタイル
# half_style = {"width": "50%", "display": "inline-block"}

# app = dash.Dash(__name__)

# # 2つのコンポーネントを持つレイアウト
# app.layout = html.Div(
#     [
#         html.Button("PUSH ME", id="my_button", n_clicks=0),
#         html.Div(id="my_div", children=[]),
#     ]
# )


# # コールバック1
# @app.callback(
#     Output("my_div", "children"),
#     Input("my_button", "n_clicks"),
#     State("my_div", "children"),
#     prevent_initial_call=True,
# )
# def update_layout(n_clicks, children):
#     new_layout = html.Div(
#         [
#             dcc.Dropdown(
#                 id={"type": "my_dropdown", "index": n_clicks},
#                 options=[{"label": c, "value": c} for c in gapminder.country.unique()],
#                 value=gapminder.country.unique()[n_clicks - 1],
#             ),
#             dcc.Dropdown(
#                 id={"type": "my_dropdown2", "index": n_clicks},
#                 options=[
#                     {"label": col, "value": col} for col in gapminder.columns[3:6]
#                 ],
#                 value="lifeExp",
#             ),
#             dcc.Graph(id={"type": "my_graph", "index": n_clicks}),
#         ],
#         style=half_style,
#     )  # 横に2つのレイアウトを並べるためstyleを渡す
#     children.append(new_layout)
#     return children


# # コールバック2
# @app.callback(
#     Output({"type": "my_graph", "index": MATCH}, "figure"),
#     # ➊ 1つ目のInputのindexにALLSMALLER,2つ目,3つ目にMATCHを渡す
#     Input({"type": "my_dropdown", "index": ALLSMALLER}, "value"),
#     Input({"type": "my_dropdown", "index": MATCH}, "value"),  # ➋
#     Input({"type": "my_dropdown2", "index": MATCH}, "value"),
# )
# def update_graph(allsmaller_value, matching_value, selected_col):
#     selected_value = allsmaller_value + [matching_value]  # ➌
#     selected_countries = gapminder[gapminder["country"].isin(selected_value)]  # ➍
#     return px.line(selected_countries, x="year", y=selected_col, color="country")  # ➎


# app.run_server(debug=True)


"""dash_callback_multipage.py"""
# iris = px.data.iris()

# app = dash.Dash(__name__)

# # ➊ レイアウト
# app.layout = html.Div(
#     [
#         # ➍ URLを生成
#         dcc.Location(id="my_location"),
#         # ➎ コンテンツの表示
#         html.Div(
#             id="show_location",
#             style={"fontSize": 30, "textAlign": "center", "height": 400},
#         ),
#         html.Br(),
#         # ➏ Linkの設置
#         dcc.Link("home", href="/"),
#         html.Br(),
#         dcc.Link("/graph", href="/graph"),
#         html.Br(),
#         dcc.Link("/table", href="/table"),
#     ],
#     style={"fontSize": 30, "textAlign": "center"},
# )

# # ➋ ページごとのコンテンツの作成
# # home(/)のコンテンツ
# home = html.H1("irisデータ")

# # graph(/graph)のコンテンツ
# graph = dcc.Graph(
#     figure=px.scatter(
#         iris, x="sepal_width", y="sepal_length", color="species", title="irisグラフ"
#     )
# )

# # table(/table)のコンテンツ
# table = dcc.Graph(
#     figure=go.Figure(
#         data=go.Table(
#             header={"values": iris.columns},
#             cells={"values": [iris[col].tolist() for col in iris.columns]},
#         ),
#         layout=go.Layout(title="irisデータテーブル"),
#     )
# )


# @app.callback(Output("show_location", "children"), Input("my_location", "pathname"))
# # ➌ 各pathnameごとに返すコンテンツを指定する
# def update_location(pathname):
#     if pathname == "/graph":
#         return graph
#     elif pathname == "/table":
#         return table
#     else:
#         # 条件にないpathnameはhomeを返す
#         return home


# if __name__ == "__main__":
#     app.run_server(debug=True)


"""dash_callback_multipleinput.py"""
# iris = px.data.iris()

# external_stylesheets = ["https://codepen.io/chriddyp/pen/bWLwgP.css"]

# # ➊
# app = dash.Dash(
#     __name__,
#     external_stylesheets=external_stylesheets,
#     suppress_callback_exceptions=True,
# )


# # レイアウト
# app.layout = html.Div(
#     [
#         dcc.Location(id="my_location"),
#         html.Div(id="show_location1", style={"height": 600}),
#         html.Br(),
#         dcc.Link("home", href="/"),
#         html.Br(),
#         dcc.Link("/graph", href="/graph"),
#         html.Br(),
#         dcc.Link("/table", href="/table"),
#     ],
#     style={"textAlign": "center"},
# )

# # ページごとのコンテンツの作成
# # homeページ作成
# home = html.H1("irisデータ")

# # グラフページ作成
# graph = html.Div(
#     [
#         html.Div(
#             [
#                 html.Div(
#                     [
#                         html.P("X軸: "),
#                         dcc.RadioItems(
#                             id="x_axis_radio",
#                             options=[
#                                 {"label": col, "value": col} for col in iris.columns[:4]
#                             ],
#                             value="sepal_width",
#                         ),
#                     ],
#                     style={"display": "inline-block"},
#                 ),
#                 html.Div(
#                     [
#                         html.P("Y軸: "),
#                         dcc.RadioItems(
#                             id="y_axis_radio",
#                             options=[
#                                 {"label": col, "value": col} for col in iris.columns[:4]
#                             ],
#                             value="sepal_length",
#                         ),
#                     ],
#                     style={"display": "inline-block"},
#                 ),
#             ]
#         ),
#         dcc.Graph(id="radio-graph"),
#     ]
# )
# # テーブルページ作成
# table = html.Div(
#     [
#         html.Div(
#             [
#                 dcc.Dropdown(
#                     id="species-dropdown",
#                     options=[{"value": col, "label": col} for col in iris.columns],
#                     multi=True,
#                     value=["sepal_length", "sepal_width"],
#                 )
#             ],
#             style={"width": "60%", "margin": "auto"},
#         ),
#         dcc.Graph(id="table"),
#     ]
# )


# # ページ切り替え用コールバック
# @app.callback(Output("show_location1", "children"), Input("my_location", "pathname"))
# def update_location(pathname):
#     if pathname == "/graph":
#         return graph
#     elif pathname == "/table":
#         return table
#     else:
#         return home


# # グラフ更新用コールバック
# @app.callback(
#     Output("radio-graph", "figure"),
#     Input("x_axis_radio", "value"),
#     Input("y_axis_radio", "value"),
# )
# def update_graph(selected_x, selected_y):
#     return px.scatter(
#         iris,
#         x=selected_x,
#         y=selected_y,
#         color="species",
#         marginal_y="violin",
#         marginal_x="box",
#         title="irisグラフ",
#     )


# # テーブル更新用コールバック
# @app.callback(Output("table", "figure"), Input("species-dropdown", "value"))
# def update_table(selected_value):
#     iris_df = iris[selected_value]
#     return go.Figure(
#         data=go.Table(
#             header={"values": iris_df.columns},
#             cells={"values": [iris_df[col].tolist() for col in iris_df.columns]},
#         ),
#         layout=go.Layout(title="irisデータテーブル"),
#     )


# if __name__ == "__main__":
#     app.run_server(debug=True)


"""dash_callback_mousehover.py"""
# # ➊ データの作成（gapminderデータの2007年分のみ）
# gapminder = px.data.gapminder()
# gapminder2007 = gapminder[gapminder["year"] == 2007]

# dash_stylesheets = ["https://codepen.io/chriddyp/pen/bWLwgP.css"]
# app = dash.Dash(__name__, external_stylesheets=dash_stylesheets)

# # ➋ アプリケーションのレイアウト
# app.layout = html.Div(
#     [
#         html.H1("Gapminder Graph"),
#         # ➍ 散布図の作成
#         dcc.Graph(
#             id="gapminder-g",
#             figure=px.scatter(
#                 gapminder2007, x="gdpPercap", y="lifeExp", hover_name="country"
#             ),
#         ),
#         # ➎ ホバーデータを表示するPコンポーネント
#         html.P(id="hoverdata-p", style={"fontSize": 32, "textAlign": "center"}),
#     ],
#     style={"width": "80%", "margin": "auto", "textAlign": "center"},
# )


# # ➌ コールバック
# @app.callback(
#     Output("hoverdata-p", "children"), Input("gapminder-g", "hoverData")  # ➏
# )  # ➐
# def show_hover_data(hoverData):  # ➑
#     return json.dumps(hoverData)  # ➒


# if __name__ == "__main__":
#     app.run_server(debug=True)


"""dash_callback_selecteddata.py"""
# # ➊ データの作成（gapminderデータの2007年分のみ）
# gapminder = px.data.gapminder()
# gapminder2007 = gapminder[gapminder["year"] == 2007]

# dash_stylesheets = ["https://codepen.io/chriddyp/pen/bWLwgP.css"]
# app = dash.Dash(__name__, external_stylesheets=dash_stylesheets)

# # ➋ アプリケーションのレイアウト
# app.layout = html.Div(
#     [
#         html.H1("Gapminder Graph"),
#         # ➍ 散布図の作成
#         dcc.Graph(
#             id="gapminder-g",
#             figure=px.scatter(
#                 gapminder2007,
#                 x="gdpPercap",
#                 y="lifeExp",
#                 hover_name="country",
#                 # ➎ クリック＋SHIFTで複数データを選択
#                 template={"layout": {"clickmode": "event+select"}},
#             ),
#         ),
#         html.P(id="hoverdata-p", style={"fontSize": 32, "textAlign": "center"}),
#     ],
#     style={"width": "80%", "margin": "auto", "textAlign": "center"},
# )


# # ➌ コールバック
# @app.callback(
#     Output("hoverdata-p", "children"),
#     # ➏ GraphのselectedData属性を指定する
#     Input("gapminder-g", "selectedData"),
# )
# def show_hover_data(selectedData):
#     return json.dumps(selectedData)


# if __name__ == "__main__":
#     app.run_server(debug=True)


"""dash_callback_selecteddata_drag.py"""
# gapminder = px.data.gapminder()
# gapminder2007 = gapminder[gapminder["year"] == 2007]

# dash_stylesheets = ["https://codepen.io/chriddyp/pen/bWLwgP.css"]
# app = dash.Dash(__name__, external_stylesheets=dash_stylesheets)

# app.layout = html.Div(
#     [
#         html.H1("Gapminder Graph"),
#         dcc.Graph(
#             id="gapminder-g",
#             figure=px.scatter(
#                 gapminder2007,
#                 x="gdpPercap",
#                 y="lifeExp",
#                 hover_name="country",
#                 # ➊ ドラッグモードを"select"に
#                 template={"layout": {"dragmode": "select"}},
#             ),
#         ),
#         html.Div(
#             [
#                 dcc.Graph(id="graph1", className="six columns"),
#                 dcc.Graph(id="graph2", className="six columns"),
#             ]
#         ),
#     ],
#     style={"width": "80%", "margin": "auto", "textAlign": "center"},
# )


# @app.callback(
#     Output("graph1", "figure"),
#     Output("graph2", "figure"),
#     Input("gapminder-g", "selectedData"),
# )
# def show_hover_data(selectedData):
#     if selectedData:
#         selected_countries = [data["hovertext"] for data in selectedData["points"]]
#         selected_df = gapminder[gapminder["country"].isin(selected_countries)]
#         fig1 = px.line(selected_df, x="year", y="pop", color="country", title="各国の人口")
#         fig2 = px.line(
#             selected_df, x="year", y="lifeExp", color="country", title="各国の平均寿命"
#         )
#         return fig1, fig2
#     raise dash.exceptions.PreventUpdate


# if __name__ == "__main__":
#     app.run_server(debug=True)


"""dash_callback_preventupdate.py"""
# gapminder = px.data.gapminder()
# gapminder2007 = gapminder[gapminder["year"] == 2007]

# dash_stylesheets = ["https://codepen.io/chriddyp/pen/bWLwgP.css"]
# app = dash.Dash(__name__, external_stylesheets=dash_stylesheets)

# app.layout = html.Div(
#     [
#         html.H1("Gapminder Graph"),
#         dcc.Graph(
#             id="gapminder-g",
#             figure=px.scatter(
#                 gapminder2007, x="gdpPercap", y="lifeExp", hover_name="country"
#             ),
#         ),
#         html.P(
#             id="hoverdata-p",
#             style={
#                 "fontSize": 24,
#                 "textAlign": "center",
#                 "height": 100,
#                 "backgroundColor": "#e1eef6",
#             },
#         ),
#         # コールバックの出力先
#         html.P(
#             id="prevent-p",
#             style={
#                 "fontSize": 24,
#                 "textAlign": "center",
#                 "height": 100,
#                 "backgroundColor": "#D7FFF1",
#             },
#         ),
#     ],
#     style={"width": "80%", "margin": "auto", "textAlign": "center"},
# )


# # PreventUpdateを用いないコールバック
# @app.callback(Output("hoverdata-p", "children"), Input("gapminder-g", "hoverData"))
# def show_hover_data(hoverData):
#     return json.dumps(hoverData)


# # ➊ PreventUpdateを用いたコールバック
# @app.callback(Output("prevent-p", "children"), Input("gapminder-g", "hoverData"))
# def prevent_none(hoverData):
#     if hoverData is None:
#         # ➋ PreventUpdateクラスを用いて更新を停止
#         raise dash.exceptions.PreventUpdate
#     return json.dumps(hoverData)


# if __name__ == "__main__":
#     app.run_server(debug=True)


"""dash_callback_multiprevent.py"""
gapminder = px.data.gapminder()
gapminder2007 = gapminder[gapminder["year"] == 2007]

dash_stylesheets = ["https://codepen.io/chriddyp/pen/bWLwgP.css"]
app = dash.Dash(__name__, external_stylesheets=dash_stylesheets)

app.layout = html.Div(
    [
        html.H1("Gapminder Graph"),
        dcc.Graph(
            id="gapminder-g",
            figure=px.scatter(
                gapminder2007, x="gdpPercap", y="lifeExp", hover_name="country"
            ),
        ),
        html.P(
            id="hoverdata-p",
            style={
                "fontSize": 32,
                "textAlign": "center",
                "height": 100,
                "backgroundColor": "#e1eef6",
            },
        ),
        html.P(
            id="prevent-p",
            style={
                "fontSize": 32,
                "textAlign": "center",
                "height": 100,
                "backgroundColor": "#D7FFF1",
            },
        ),
    ],
    style={"width": "80%", "margin": "auto", "textAlign": "center"},
)


@app.callback(
    # ➊ データの状態に関係なくコールバックを更新する出力先
    Output("hoverdata-p", "children"),
    # ➋ Noneであれば、コールバックの更新を停止する出力先
    Output("prevent-p", "children"),
    Input("gapminder-g", "hoverData"),
)
def show_hover_data(hoverData):
    if hoverData is None:
        # ➌ 1つ目の戻り値はホバーデータをそのまま、2つ目の戻り値は更新を停止
        return (json.dumps(hoverData), dash.no_update)
    return json.dumps(hoverData), json.dumps(hoverData)


if __name__ == "__main__":
    app.run_server(debug=True)
