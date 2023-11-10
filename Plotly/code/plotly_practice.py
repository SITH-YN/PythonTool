import numpy as np
import pandas as pd
import plotly
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots

"""1.1 Plotly Expressとは"""
"""1.1.1 インタラクティブな可視化事例"""
# gapminder = px.data.gapminder()
# gapminder.head()

# px.scatter(
#     gapminder, x="gdpPercap", y="lifeExp", log_x=True, hover_name="country",
# ).show()

# px.scatter(
#     gapminder,
#     x="gdpPercap",
#     y="lifeExp",
#     log_x=True,
#     hover_name="country",
#     size="pop",  # 人口を点の大きさで表現
#     size_max=40,  # 点の大きさの最大値
#     color="continent",  # 大陸ごとに色分け
# ).show()

# facet_fig = px.scatter(
#     gapminder,
#     x="gdpPercap",
#     y="lifeExp",
#     log_x=True,
#     hover_name="country",
#     size="pop",  # 人口を点の大きさで表現
#     size_max=40,  # 点の大きさの最大値
#     color="continent",  # 大陸ごとに色分け
#     facet_col="continent",  # 大陸ごとのグラフに分割
#     width=800  # グラフの横幅
# )
# facet_fig.update_xaxes(tickfont={"size": 8})  # X軸ラベルのフォントサイズ
# facet_fig.show()

# animation_fig = px.scatter(
#     gapminder,
#     x="gdpPercap",
#     y="lifeExp",
#     log_x=True,
#     hover_name="country",
#     size="pop",  # 人口を点の大きさで表現
#     size_max=40,  # 点の大きさの最大値
#     color="continent",  # 大陸ごとに色分け
#     facet_col="continent",  # 大陸ごとのグラフに分割
#     width=800,  # グラフの横幅
#     animation_frame="year"  # 年ごとのデータでアニメーション
# )
# animation_fig.update_xaxes(tickfont={"size": 8})  # X軸ラベルのフォントサイズ
# animation_fig.show()

"""1.2 Plotly Express 入門"""
"""1.2.1 グラフを描画する関数"""
# df = pd.DataFrame([[1, 1], [2, 5], [3, 3]], columns=["x", "y"])
# px.line(df, x="x", y="y").show()


"""1.2.2 データ型"""
# tips = px.data.tips()
# tips.head()

# px.scatter(tips, x="total_bill", y="tip").show()

# px.line(x=[1, 2, 3], y=[3, 5, 2]).show()

# np.random.seed(1)
# arr = np.random.rand(100, 4)
# px.scatter(arr, x=0, y=1, color=2, size=3).show()


"""1.3 Plotly Express 応用"""
"""1.3.1 ファセット"""
# tips = px.data.tips()
# tips.head()
# px.scatter(
#     tips,
#     x="total_bill",
#     y="tip",
#     color="size",  # size列で色分け
#     facet_row="time",  # 縦に分割
#     facet_col="sex",  # 横に分割
# ).show()


"""1.3.2 アニメーション"""
# gapminder = px.data.gapminder()
# gapminder.head()
# gapminder_fig = px.scatter(
#     gapminder,
#     x="gdpPercap",
#     y="lifeExp",
#     animation_frame="year",  # アニメーションのためにデータを分割する列を指定
#     size="pop",  # 要素の大きさを指定（バブルチャート）
#     color="continent",  # 色分け
#     hover_name="country",  # ホバーツールの名前
#     facet_col="continent",  # 横に分割
#     log_x=True,  # X軸を対数にとる
#     size_max=40,  # 要素の大きさの最大値
#     width=800  # グラフの横幅
# )
# gapminder_fig.update_xaxes(tickfont={"size": 8})  # 軸目盛のフォントサイズ
# gapminder_fig.show()


"""1.3.3 スタイルの設定"""
# tips = px.data.tips()
# tips.head()
# # figureを作成: 「2.3.2 figure による描画領域の作成」を参照
# styled_fig = px.scatter(tips, x="total_bill", y="tip", facet_col="sex")
# # traceを変更: 「2.4.6 update から始まるメソッドによる指定」を参照
# # 「4.2.1 グラフのスタイル」を参照
# styled_fig.update_traces(
#     marker={
#         "size": 10,  # 要素のサイズ
#         "color": "lightblue",  # 要素の色
#         "line": {"width": 2, "color": "slateblue"},  # 枠線のスタイル
#     },
#     row=1,
#     col=1,
# )
# styled_fig.update_traces(
#     marker={
#         "size": 10,
#         "color": "lightpink",
#         "line": {"width": 2, "color": "deeppink"},
#     },
#     row=1,
#     col=2,
# )
# # layoutを変更: 「2.4.6 update から始まるメソッドによる指定」を参照
# # 「4.2.1 グラフのスタイル」を参照
# styled_fig.update_layout(
#     width=800,  # figureの幅
#     height=400,  # figureの高さ
#     title={
#         "text": "総支払金額とチップの金額",
#         # グラフタイトルのスタイル
#         "font": {"family": "Courier", "size": 20, "color": "slategray"},
#     },
#     margin={"l": 20, "r": 20, "t": 40, "b": 20},  # 余白
#     paper_bgcolor="antiquewhite",  # グラフ領域の背景色
# )
# styled_fig.update_xaxes(
#     ticks="outside",  # 軸メモリを外側に表示
#     tickwidth=2,  # 軸メモリの太さ
#     tickcolor="seagreen",  # 軸メモリの色
#     ticklen=10,  # 軸メモリの長さ
#     # X軸タイトル、フォントサイズ
#     title={"text": "総支払金額", "font": {"size": 10}},
# )
# styled_fig.update_yaxes(
#     ticks="outside",
#     tickwidth=2,
#     tickcolor="dimgray",
#     ticklen=10,
#     col=1,
#     title={"text": "チップの金額", "font": {"size": 10}},
# )
# styled_fig.show()


"""1.4 Plotly Express の様々なグラフ"""
"""1.4.1 散布図（scatter 関数）"""
# gapminder = px.data.gapminder()
# gapminder.head()
# gapminder_2007 = gapminder.loc[gapminder["year"] == 2007]
# px.scatter(
#     gapminder_2007,
#     x="gdpPercap",
#     y="lifeExp",
#     size="pop",  # 要素の大きさ
#     color="continent",  # 要素の色
#     hover_name="country",  # ホバーツールのタイトル
#     log_x=True,  # X軸を対数にとる
#     size_max=60,  # 要素の大きさの最大値
# ).show()

"""1.4.2 散布図行列（scatter matrix 関数）"""
# tips = px.data.tips()
# tips.head()
# scatter_matrix_fig = px.scatter_matrix(
#     tips,
#     # 描画対象の列名
#     dimensions=["total_bill", "tip", "size"],
#     color="time",  # ❶ time列で色分け
#     symbol="smoker",  # ❷ smoker列ごとにマーカの形状で分類
# ).show()


"""1.4.3 折れ線グラフ（line 関数）"""
# gapminder = px.data.gapminder()
# gapminder.head()
# gapminder_Oceania = gapminder.loc[gapminder["continent"] == "Oceania"]
# px.line(
#     gapminder_Oceania,
#     x="year",
#     y="lifeExp",
#     color="country",  # ❶ country列でデータを分割
# ).show()


"""1.4.4 棒グラフ（bar 関数）"""
# gapminder = px.data.gapminder()
# gapminder.head()
# gapminder_Canada = gapminder.loc[gapminder["country"] == "Canada"]
# px.bar(
#     gapminder_Canada,
#     x="year",
#     y="pop",
#     color="lifeExp",  # ❶ 値をカラースケールで表現する列
#     hover_data=["lifeExp", "gdpPercap"],  # ❷ ホバーツールに表示する列
# ).show()

# tips = px.data.tips()
# tips.head()
# px.bar(
#     tips,
#     x="sex",
#     y="total_bill",  # ❶ smoker列で分割してグループ化
#     color="smoker",
#     barmode="group",
# ).show()


"""1.4.5 面グラフ（area 関数）"""
# gapminder = px.data.gapminder()
# gapminder.head()
# px.area(
#     gapminder,
#     x="year",
#     y="pop",  # ❶ continent列で分割
#     color="continent",  # ❷ country列のデータごとに境界線を描画
#     line_group="country",
# ).show()


"""1.4.6 エラーバー"""
# np.random.seed(1)
# df = pd.DataFrame(np.random.randn(100, 2), columns=["x", "y"])
# px.scatter(
#     df,
#     x="x",
#     y="y",
#     error_x=np.random.rand(100) * 0.1,  # X値のエラー値
#     error_y=np.random.rand(100) * 0.1,  # Y値のエラー値
# ).show()


"""1.4.7 箱ひげ図（box 関数）"""
# tips = px.data.tips()
# tips.head()

# px.box(tips, x="time", y="total_bill").show()

# px.box(
#     tips,
#     x="time",
#     y="total_bill",
#     color="smoker",  # smoker列で色分け
#     notched=True,  # ❶ ノッチを入れる
#     points="all",  # ❷ すべての要素を点で描画
#     title="Box plot of total bill",
#     hover_data=["day"],  # ❸ ホバーツールにday列の値を表示
# ).show()


"""1.4.8 バイオリン図（violin 関数）"""
# tips = px.data.tips()
# tips.head()
# px.violin(
#     tips,
#     y="tip",
#     x="smoker",
#     color="sex",  # ❶ sex列で色分け
#     box=True,  # ❷ 箱ひげ図を重ねて描画
#     points="all",  # ❸ すべての要素を点で描画
#     hover_data=tips.columns,  # ホバーツールにすべて列の値を表示
# ).show()


"""1.4.9 ヒストグラム（histogram 関数）"""
# tips = px.data.tips()
# tips.head()

# px.histogram(tips, x="total_bill").show()

# px.histogram(
#     tips,
#     x="total_bill",
#     color="sex",  # ❶ sex列で分割して積み上げ
#     marginal="rug",  # ❷ ラグプロットをサブプロットで表示
#     hover_data=tips.columns,  # ❸ ホバーツールにすべて列の値を表示
# ).show()


"""1.4.10 円グラフ（pie 関数）"""
# tips = px.data.tips()
# tips.head()
# px.pie(tips, names="day", values="tip").show()


"""1.4.11 サンバーストグラフ（sunburst 関数）"""
# gapminder = px.data.gapminder()
# gapminder.head()
# gapminder_2007 = gapminder.loc[gapminder["year"] == 2007]
# px.sunburst(
#     gapminder_2007, path=["continent", "country"], values="pop"
# ).show()


"""1.4.12 ツリーマップ（treemap 関数）"""
# gapminder = px.data.gapminder()
# gapminder.head()
# gapminder_2007 = gapminder.loc[gapminder["year"] == 2007]
# px.treemap(
#     gapminder_2007, path=["continent", "country"], values="pop"
# ).show()


"""1.4.13 平行座標プロット（parallel coordinates 関数）"""
# iris = px.data.iris()
# iris.head()
# px.parallel_coordinates(
#     iris,
#     dimensions=["sepal_length", "sepal_width", "petal_length", "petal_width"],
#     color="species_id",  # ❶ species_id列をカラースケールで表現
# ).show()


"""1.4.14 平行プロット（parallel categories 関数）"""
# tips = px.data.tips()
# tips.head()
# px.parallel_categories(
#     tips,
#     dimensions=["sex", "smoker", "time", "day"],  # 対象列を指定
#     color="size",  # ❶ size列で色分け
#     color_continuous_scale=px.colors.sequential.Inferno,  # カラースケール
# ).show()


"""1.4.15 三角図（scatter ternary・ line ternary 関数）"""
# election = px.data.election()
# election.head()
# px.scatter_ternary(
#     election,
#     a="Joly",
#     b="Coderre",
#     c="Bergeron",
#     color="winner",  # ❶ winner列で色分け
#     size="total",  # ❷ 要素の大きさをtotal列の値
#     size_max=15,  # ❷ 要素の大きさの最大値
#     hover_name="district",  # ❸ ホバーツールのタイトル
# ).show()


"""1.4.16 ポーラチャート（scatter polar 関数・ line polar 関数・ bar polar関数）"""
# wind = px.data.wind()
# wind.head()
# px.bar_polar(
#     wind,
#     r="frequency",  # 値
#     theta="direction",  # 角度
#     color="strength",  # ❶ strengthで分割して積み上げ
# ).show()


"""1.4.17 階級区分図（choropleth 関数）"""
# gapminder = px.data.gapminder()
# gapminder.head()
# gapmider_2007 = gapminder[gapminder["year"] == 2007]
# px.choropleth(
#     gapmider_2007,
#     locations="iso_alpha",  # 位置をISO 3166-1 alpha-3形式で指定
#     color="lifeExp",
#     hover_name="country",  # ❶ ホバーツールのタイトル
# ).show()


"""1.4.18 地図上の散布図（scattergeo 関数）"""
# gapminder = px.data.gapminder()
# gapminder.head()
# gapmider_2007 = gapminder[gapminder["year"] == 2007]
# px.scatter_geo(
#     gapmider_2007,
#     locations="iso_alpha",
#     size="gdpPercap",  # ❶ 要素のサイズ
#     color="lifeExp",  # ❷ 要素の色
#     hover_name="country",
#     animation_frame="year",  # ❸ アニメーション
# ).show()


"""1.4.19 3D 散布図（scatter 3d 関数・ line 3d 関数）"""
# gapminder = px.data.gapminder()
# gapminder.head()
# scatter_3d_fig = px.scatter_3d(
#     gapminder,
#     x="year",
#     y="continent",
#     z="pop",
#     size="gdpPercap",  # ❶ 要素の大きさ
#     color="lifeExp",  # ❷ lifeExp列で色分け
#     hover_data=["country"],  # ❸ ホバーツールに表示
# )
# # Z軸を対数にとる
# scatter_3d_fig.layout.update(scene={"zaxis": {"type": "log"}})
# scatter_3d_fig.show()


"""2.2 plotly.py のコンセプト"""
"""2.2.2 figure による描画領域の作成"""
# fig = go.Figure()
# fig.show()


"""2.2.3 trace によるグラフの登録"""
# scatter_trace = go.Scatter(x=[1, 2, 3], y=[3, 1, 6])

# scatter_fig = go.Figure(data=scatter_trace)
# scatter_fig.show()

# bar_trace = go.Bar(x=[1, 2, 3], y=[4, 3, 1])
# scatter_bar_fig = go.Figure(data=[scatter_trace, bar_trace])
# scatter_bar_fig.show()


"""2.2.4 layout によるグラフの調整"""
# scatter_trace = go.Scatter(x=[1, 2, 3], y=[3, 1, 6])
# layout = go.Layout(width=300, height=300)
# fix_size_fig = go.Figure(data=scatter_trace, layout=layout)
# fix_size_fig.show()


"""2.3 plotly.py の記法"""
"""2.3.1 plotly.js のデータ構造"""
# fig = go.Figure()
# fig.to_json()[:80]
# fig.add_trace(go.Scatter(x=[1, 2], y=[1, 2]))
# fig.to_json()[:80]
# fig.data
# fig.data[0].x = [3, 4]
# fig.data
# fig.show()


"""2.3.3 コンストラクタの引数による指定"""
# layout = go.Layout(title="グラフタイトル")
# fig = go.Figure(layout=layout)
# fig.show()
# fig.layout
# fig.layout.title
# go.Layout(title={"text": "辞書を渡す例"})
# go.Layout({"title": {"text": "ネストした辞書を渡した例"}})
# fig = go.Figure(layout_title_text="マジックアンダースコア記法")
# fig.layout
# fig.show()


"""2.3.4 属性に代入"""
# fig = go.Figure()
# fig.layout.title.text = "属性値を代入"
# fig.layout
# fig.show()


"""2.3.5 update メソッドによる指定"""
# fig = go.Figure()
# fig.layout.update(title={"text": "updateメソッドによる属性変更"})
# fig.layout
# fig.show()


"""2.3.6 update から始まるメソッドによる指定"""
# fig = go.Figure()
# fig.update_layout(title={"text": "update_layoutメソッドによる属性変更"})
# fig.layout
# fig.show()


"""2.3.7 add から始まるメソッドによる trace の追加"""
# fig2 = go.Figure()

# fig2.add_trace(go.Scatter(x=[1, 2, 3], y=[1, 5, 3]))
# fig2.show()

# fig2.add_traces(
#     [go.Scatter(x=[1, 2, 3], y=[3, 2, 4]), go.Bar(x=[1, 2, 3], y=[1, 2, 3])]
# )
# fig2.show()


"""2.4 標準的なインタラクティブ操作"""
"""2. 4. 1 ホバーツール"""
# go.Figure(
#     [
#         go.Bar(
#             x=[1, 2, 3], y=[1, 2, 3], hovertext=["A社", "B社", "C社"], name="bar"
#         ),
#         go.Scatter(x=[1, 2, 3], y=[2, 3, 1], name="line"),
#     ]
# ).show()


"""2. 4. 2 凡例による要素の選択"""
# np.random.seed(1)
# data0 = np.random.randn(200, 200)
# data1 = np.random.randn(200, 200) + 1

# go.Figure(
#     [
#         go.Scatter(x=data0[0], y=data0[1], mode="markers", name="A"),
#         go.Scatter(x=data1[0], y=data1[1], mode="markers", name="B"),
#     ]
# ).show()


"""3.1 基本的なグラフ"""
"""3.1.1 折れ線グラフ（Scatter trace）"""
# go.Figure(go.Scatter(x=[1, 2, 3], y=[3, 5, 2])).show()

# stocks = plotly.data.stocks()
# stocks.head()
# go.Figure(go.Scatter(x=stocks["date"], y=stocks["GOOG"])).show()

# ts_layout = go.Layout(
#     # X軸のRange SliderとRange Selectorを表示
#     xaxis={
#         "rangeslider": {"visible": True},  # ❶ RangeSliderを表示
#         "rangeselector": {  # ❷ RangeSelectを設定
#             "buttons": [
#                 {"label": "1m", "step": "month", "count": 1},  # 1ヵ月
#                 {"label": "7d", "step": "day", "count": 7},  # 7日間
#                 {"step": "all"},  # 全期間
#             ]
#         },
#     }
# )
# go.Figure(
#     go.Scatter(x=stocks["date"], y=stocks["GOOG"]), layout=ts_layout
# ).show()

# line_x_not_null = np.arange(5)
# line_y_with_null = np.array([1, 2, np.nan, 4, 5])  # 欠損値を含んだデータ
# with_null_fig = go.Figure()
# with_null_fig.add_trace(
#     go.Scatter(x=line_x_not_null, y=line_y_with_null, name="default")
# )
# with_null_fig.add_trace(
#     go.Scatter(
#         x=line_x_not_null,
#         y=line_y_with_null + 1,
#         name="connectgaps",  # ❶ 欠損値を無視して線を接続
#         connectgaps=True,
#     )
# )
# with_null_fig.show()

# interp_x, interp_y = np.array([1, 2, 3]), np.array([1, 3, 2])
# line_shapes = "linear", "spline", "hv", "vh", "hvh", "vhv"
# # 6行1列のfigureを作成
# interp_fig = make_subplots(rows=6, cols=1, subplot_titles=line_shapes)
# for i, shape_name in enumerate(line_shapes, 1):
#     interp_fig.add_trace(
#         go.Scatter(
#             x=interp_x,
#             y=interp_y,
#             name=shape_name,
#             line={"shape": shape_name},  # ❶ 補間方法を指定
#             hovertext=shape_name,
#         ),
#         row=i,
#         col=1,
#     )
# interp_fig.show()


"""3.1.2 散布図（Scatter trace）"""
# np.random.seed(1)
# scatter_x, scatter_y = np.random.randn(2, 100)  # 正規分布に従う乱数を生成
# go.Figure(
#     go.Scatter(
#         x=scatter_x,
#         y=scatter_y,
#         name="standard normal distribution",
#         mode="markers",  # ❶ 描画モードを指定
#     )
# ).show()

# np.random.seed(1)
# scatter_color = np.random.rand(100)
# scatter_size = np.random.rand(100) * 30
# go.Figure(
#     go.Scatter(
#         x=scatter_x,
#         y=scatter_y,
#         name="4d",
#         mode="markers",
#         marker={
#             "color": scatter_color,  # ❶ 要素の大きさを色で表現
#             "size": scatter_size,  # ❷ 要素ごとに大きさを指定
#             "sizemode": "diameter",  # 大きさを直径で指定
#             "opacity": 0.8,  # 要素の不透明度
#             "showscale": True,  # カラースケールを表示
#         },
#     )
# ).show()

# np.random.seed(1)
# large_x, large_y = np.random.randn(2, 10000)
# go.Figure([go.Scattergl(x=large_x, y=large_y, mode="markers")]).show()


"""3.1.3 棒グラフ（Bar trace）"""
# bar_fig = make_subplots(rows=2, cols=2, subplot_titles=["ラベル", "座標", "横"])
# # ❶ X値が文字列型
# bar_fig.add_trace(go.Bar(x=["a", "b", "c"], y=[3, 5, 2]), row=1, col=1)
# # ❶ X値が数値型
# bar_fig.add_trace(go.Bar(x=[0, 1, 4], y=[1, 4, 3]), row=1, col=2)
# # ❷ 横向きの棒グラフ
# bar_fig.add_trace(
#     go.Bar(x=[3, 2, 4], y=[1, 2, 3], orientation="h"), row=2, col=1
# )
# bar_fig.show()

# bar_trace1 = go.Bar(x=["a", "b", "c"], y=[3, 5, 2], name="group1")
# bar_trace2 = go.Bar(x=["a", "b", "c"], y=[4, 3, 1], name="group2")
# grouped_fig = go.Figure([bar_trace1, bar_trace2])
# grouped_fig.show()

# bar_trace1 = go.Bar(x=["a", "b", "c"], y=[3, 5, 2], name="group1")
# bar_trace2 = go.Bar(x=["a", "b", "c"], y=[4, 3, 1], name="group2")
# stacked_fig = go.Figure(
#     [bar_trace1, bar_trace2],
#     # 積み上げ棒グラフにするためのlayoutを設定
#     layout=go.Layout(barmode="stack"),
# )
# stacked_fig.show()

# bar_trace1 = go.Bar(x=["a", "b", "c"], y=[3, 5, 2], name="group1")
# bar_trace2 = go.Bar(x=["a", "b", "c"], y=[4, 3, 1], name="group2")
# bar_trace3 = go.Bar(x=["a", "b", "c"], y=[-2, -3, 1], name="group3")
# relative_fig = go.Figure(
#     [bar_trace1, bar_trace2, bar_trace3],
#     # ❶ 0未満の値を下方向に積み上げるlayoutを作成
#     layout=go.Layout(barmode="relative"),
# )
# relative_fig.show()


"""3.1.4 面グラフ（Scatter trace）"""
# np.random.seed(7)
# area_x = np.arange(10)
# area_y1, area_y2 = np.random.rand(2, 10)  # 一様乱数を生成
# area_trace = go.Scatter(
#     x=area_x,
#     y=area_y1,
#     name="area1",
#     fill="tozeroy",  # ❶ 0からY値まで塗りつぶし,
#     mode="none",  # ❷ 線とマーカーを描画しない
#     fillcolor="mediumslateblue",  # 塗りつぶし色
# )
# area_fig = go.Figure([area_trace])
# area_fig.show()

# np.random.seed(7)
# area_x = np.arange(10)
# area_y1, area_y2 = np.random.rand(2, 10)  # 一様乱数を生成
# area_trace = go.Scatter(
#     x=area_x,
#     y=area_y1,
#     name="area1",
#     fill="tozeroy",  # ❶ 0からY値まで塗りつぶし,
#     mode="none",  # ❷ 線とマーカーを描画しない
#     fillcolor="mediumslateblue",  # 塗りつぶし色
# )
# next_area_trace = go.Scatter(
#     x=area_x,
#     y=area_y1 + area_y2,
#     name="area2",
#     fill="tonexty",  # ❶ 前のtraceからY値までを塗りつぶし
#     mode="none",
#     fillcolor="lightpink",
# )
# stacked_area_fig = go.Figure([area_trace, next_area_trace])
# stacked_area_fig.show()

# np.random.seed(7)
# area_x = np.arange(10)
# area_y1, area_y2 = np.random.rand(2, 10)  # 一様乱数を生成
# area_trace = go.Scatter(
#     x=area_x,
#     y=area_y1,
#     name="area1",
#     fill="tozeroy",  # ❶ 0からY値まで塗りつぶし,
#     mode="none",  # ❷ 線とマーカーを描画しない
#     fillcolor="mediumslateblue",  # 塗りつぶし色
# )
# next_area_trace = go.Scatter(
#     x=area_x,
#     y=area_y1 + area_y2,
#     name="area2",
#     fill="tonexty",  # ❶ 前のtraceからY値までを塗りつぶし
#     mode="none",
#     fillcolor="lightpink",
# )
# normed_area_fig = go.Figure()
# normed_area_fig.add_trace(
#     go.Scatter(
#         x=area_x,
#         y=area_y1,
#         stackgroup="groupA",  # 同じ名前の要素が積み上げられる
#         mode="none",
#         groupnorm="fraction",  # ❶ 合計を1として正規化
#         fillcolor="mediumslateblue",
#     )
# )
# normed_area_fig.add_trace(
#     go.Scatter(
#         x=area_x,
#         y=area_y2,
#         stackgroup="groupA",  # 同じ名前の要素が積み上げられる
#         mode="none",
#         groupnorm="fraction",  # ❶ 合計を1として正規化
#         fillcolor="lightpink",
#     )
# )
# normed_area_fig.show()


"""3.1.5 円グラフ（Pie trace）"""
# companies = ["A社", "B社", "C社", "D社"]
# sales_2019 = [1000, 700, 300, 100]
# sales_2020 = [1500, 1100, 450, 380]
# go.Figure(
#     go.Pie(labels=companies, values=sales_2019),
#     layout=go.Layout(title="売上"),  # figureのタイトル
# ).show()

# companies = ["A社", "B社", "C社", "D社"]
# sales_2019 = [1000, 700, 300, 100]
# sales_2020 = [1500, 1100, 450, 380]
# sales_pie_fig = make_subplots(
#     rows=1,
#     cols=2,
#     specs=[[{"type": "domain"}, {"type": "domain"}]],
#     subplot_titles=["2019年の売上", "2020年の売上"],  # サブプロットのタイトル
# )
# sales_pie_fig.add_trace(
#     go.Pie(
#         labels=companies,
#         values=sales_2019,  # ❶ 同じscalegroupでサイズが調整される
#         scalegroup="sales",
#     ),
#     row=1,
#     col=1,
# )
# sales_pie_fig.add_trace(
#     go.Pie(labels=companies, values=sales_2020, scalegroup="sales"),
#     row=1,
#     col=2,
# )
# sales_pie_fig.show()


"""3.1.6 サンバーストグラフ（Sunburst trace）"""
# asset_labels = ["資産", "債権", "A社", "B社", "株式", "C社", "D社", "預金"]
# asset_parents = ["", "資産", "債権", "債権", "資産", "株式", "株式", "資産"]
# asset_values = [1000, 400, 300, 100, 200, 160, 40, 400]
# sunburst_fig = make_subplots(
#     1, 2, specs=[[{"type": "domain"}, {"type": "domain"}]]
# )
# sunburst_fig.add_trace(
#     go.Sunburst(
#         labels=asset_labels,  # セクタごとのラベル
#         parents=asset_parents,  # 親セクタのラベル
#         values=asset_values,  # セクタごとの値
#         branchvalues="total",  # ❶ 親が子の階層すべての合計値
#     ),
#     row=1,
#     col=1,
# )
# sunburst_fig.add_trace(
#     go.Sunburst(
#         labels=asset_labels,
#         parents=asset_parents,
#         values=asset_values,
#         branchvalues="remainder",  # ❷ 子が親とは別の値
#     ),
#     row=1,
#     col=2,
# )
# sunburst_fig.show()


"""3.1.7 ツリーマップ（Treemap trace）"""
# asset_labels = ["資産", "債権", "A社", "B社", "株式", "C社", "D社", "預金"]
# asset_parents = ["", "資産", "債権", "債権", "資産", "株式", "株式", "資産"]
# asset_values = [1000, 400, 300, 100, 200, 160, 40, 400]
# go.Figure(
#     go.Treemap(
#         labels=asset_labels,  # セクタごとのラベル
#         parents=asset_parents,  # 親セクタのラベル
#         values=asset_values,  # セクタごとの値
#         branchvalues="total",  # 親が子の階層すべての合計値
#     )
# ).show()


"""3.1.8 テーブル（Table trace）"""
table_values = [[1, 2, 3], [3, 5, 2]]
table_labels = ["A", "B"]
table_fig = make_subplots(
    rows=2,
    cols=2,
    specs=[[{"type": "domain"}, {"type": "domain"}], [{"colspan": 2}, None]],
)
table_fig.add_trace(
    go.Table(header={"values": table_labels}, cells={"values": table_values}),
    row=1,
    col=1,
)
table_fig.add_trace(
    go.Table(
        cells={
            "values": pd.DataFrame(table_values),
            "line": {"width": 2, "color": "black"},  # 罫線のスタイル
            "fill": {"color": "white"},  # 塗りつぶし色
            "align": "right",  # 配置
        },
        header={
            "values": table_labels,
            "height": 18,  # セルの高さ
            "line": {"width": 2, "color": "black"},
            "fill": {"color": "white"},
            "font": {"size": 10},  # フォントサイズ
        },
    ),
    row=1,
    col=2,
)
table_fig.add_trace(
    go.Scatter(x=table_values[0], y=table_values[1]), row=2, col=1
)
table_fig.show()
pd.DataFrame(table_values)
