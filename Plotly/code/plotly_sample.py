# import mapbox_env
import numpy as np
import pandas as pd
import plotly
import plotly.express as px
import plotly.graph_objects as go
from IPython.display import Image
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
# table_values = [[1, 2, 3], [3, 5, 2]]
# table_labels = ["A", "B"]
# table_fig = make_subplots(
#     rows=2,
#     cols=2,
#     specs=[[{"type": "domain"}, {"type": "domain"}], [{"colspan": 2}, None]],
# )
# table_fig.add_trace(
#     go.Table(header={"values": table_labels}, cells={"values": table_values}),
#     row=1,
#     col=1,
# )
# table_fig.add_trace(
#     go.Table(
#         cells={
#             "values": pd.DataFrame(table_values),
#             "line": {"width": 2, "color": "black"},  # 罫線のスタイル
#             "fill": {"color": "white"},  # 塗りつぶし色
#             "align": "right",  # 配置
#         },
#         header={
#             "values": table_labels,
#             "height": 18,  # セルの高さ
#             "line": {"width": 2, "color": "black"},
#             "fill": {"color": "white"},
#             "font": {"size": 10},  # フォントサイズ
#         },
#     ),
#     row=1,
#     col=2,
# )
# table_fig.add_trace(
#     go.Scatter(x=table_values[0], y=table_values[1]), row=2, col=1
# )
# table_fig.show()
# pd.DataFrame(table_values)


"""3.2 専門的なグラフ"""
"""3.2.1 箱ひげ図（Box trace）"""
# tips = plotly.data.tips()
# tips.head()

# # ❶ 曜日ごとのデータを抽出
# tips_by_day = tips.groupby("day")  # day列でグループ化
# days = ["Thur", "Fri", "Sat", "Sun"]
# # グループ化された各DataFrameを抽出
# thur, fri, sat, sun = [tips_by_day.get_group(day) for day in days]

# box_fig = go.Figure()
# box_fig.add_trace(go.Box(y=thur["tip"], name="Thur"))
# box_fig.add_trace(go.Box(y=fri["tip"], name="Fri"))
# box_fig.add_trace(go.Box(y=sat["tip"], name="Sat"))
# box_fig.add_trace(go.Box(y=sun["tip"], name="Sun"))
# box_fig.show()


"""3.2.2 バイオリン図（Violin trace）"""
# tips = plotly.data.tips()
# tips.head()

# # ❶ 曜日ごとのデータを抽出
# tips_by_day = tips.groupby("day")  # day列でグループ化
# days = ["Thur", "Fri", "Sat", "Sun"]
# # グループ化された各DataFrameを抽出
# thur, fri, sat, sun = [tips_by_day.get_group(day) for day in days]

# violin_fig = make_subplots(rows=1, cols=2)
# # ❶ 1列目のサブプロット
# violin_fig.add_trace(
#     go.Violin(
#         y=thur["tip"],
#         name="Thur",
#         box_visible=True,  # ❸ 箱ひげ図を重ねて描画
#     ),
#     row=1,
#     col=1,
# )
# violin_fig.add_trace(
#     go.Violin(y=fri["tip"], name="Fri", box_visible=True), row=1, col=1
# )
# violin_fig.add_trace(
#     go.Violin(y=sat["tip"], name="Sat", box_visible=True), row=1, col=1
# )
# violin_fig.add_trace(
#     go.Violin(y=sun["tip"], name="Sun", box_visible=True), row=1, col=1
# )

# # ❷ 2列目のサブプロット
# for data in thur, fri, sat, sun:
#     smoker = data.loc[data["smoker"] == "Yes"]  # smoker列がYesのデータ
#     non_smoker = data.loc[data["smoker"] == "No"]  # smoker列がNoのデータ
#     day = data["day"].iloc[0]  # day列の先頭のデータ(ラベルに使用)
#     violin_fig.add_trace(
#         go.Violin(
#             x=smoker["day"],
#             y=smoker["tip"],
#             side="negative",  # ❹ 左側に描画
#             name=f"{day}: somoker",
#         ),
#         row=1,
#         col=2,
#     )
#     violin_fig.add_trace(
#         go.Violin(
#             x=non_smoker["day"],
#             y=non_smoker["tip"],
#             side="positive",  # ❺ 右側に描画
#             name=f"{day}: non-somoker",
#         ),
#         row=1,
#         col=2,
#     )
# violin_fig.show()


"""3.2.3 ヒストグラム（Histogram trace）"""
# np.random.seed(1)
# data0 = np.random.normal(10, 1, 10000)
# data1 = np.random.normal(12, 1.5, 10000)
# histogram_fig = make_subplots(rows=1, cols=2)
# histogram_fig.add_trace(go.Histogram(x=data0, name="data0"), row=1, col=1)
# histogram_fig.add_trace(go.Histogram(x=data1, name="data1"), row=1, col=1)
# histogram_fig.add_trace(go.Histogram(y=data0, name="data0"), row=1, col=2)
# histogram_fig.add_trace(
#     go.Histogram(
#         y=data1,  # ❶ 引数yで横向き
#         name="data1",
#         nbinsy=50,  # ❷ ビンの数を変更
#     ),
#     row=1,
#     col=2,
# )
# histogram_fig.show()

# go.Figure(
#     [go.Histogram(x=data0, name="data0"), go.Histogram(x=data1, name="data1")],
#     layout=go.Layout(barmode="stack"),  # ❶ ヒストグラムを積み上げ
# ).show()

# probability_comulative_histogram_fig = make_subplots(rows=1, cols=2)
# probability_comulative_histogram_fig.add_trace(
#     go.Histogram(
#         x=data0,
#         # ❶ サンプル数の合計を1とした正規化
#         histnorm="probability",
#         name="probability",
#     ),
#     row=1,
#     col=1,
# )
# probability_comulative_histogram_fig.add_trace(
#     go.Histogram(
#         x=data0,
#         # ❷ 累積ヒストグラム
#         cumulative={"enabled": True},
#         name="comulative",
#     ),
#     row=1,
#     col=2,
# )
# probability_comulative_histogram_fig.show()

# go.Figure(
#     go.Histogram(
#         x=data0,
#         # ❷ ヒストグラムの範囲を指定
#         xbins={"start": 8, "end": 11, "size": 0.01},
#     )
# ).show()


"""3.2.4 2 次元ヒストグラム（Histogram2d trace）"""
# np.random.seed(1)
# data0 = np.random.normal(10, 1, 10000)
# data1 = np.random.normal(12, 1.5, 10000)

# histogram2d_fig = make_subplots(rows=1, cols=2)
# # ❶ 2次元ヒストグラム
# histogram2d_fig.add_trace(go.Histogram2d(x=data0, y=data1), row=1, col=1)
# # ❷ 等高線
# histogram2d_fig.add_trace(
#     go.Histogram2dContour(x=data0, y=data1, showscale=False), row=1, col=2
# )
# histogram2d_fig.update_layout(coloraxis_showscale=False)
# histogram2d_fig.show()


"""3.2.5 エラーバー"""
# np.random.seed(1)
# x = np.arange(1, 4)
# y = np.random.rand(3)
# err_value = np.random.rand(3) * 0.1
# err_value_minus = np.random.rand(3) * 0.1
# error_fig = make_subplots(rows=2, cols=2)
# # ❶ エラーバーを一定の値で指定
# error_fig.add_trace(
#     go.Scatter(
#         x=x,
#         y=y,
#         # エラーバーを定数で指定
#         error_y={"type": "constant", "value": 0.1},
#     ),
#     row=1,
#     col=1,
# )
# # ❷ 各要素ごとにエラーバーを指定
# error_fig.add_trace(
#     go.Scatter(
#         x=x,
#         y=y,
#         # 各要素のエラーバーを指定
#         error_x={"type": "data", "array": err_value},
#     ),
#     row=1,
#     col=2,
# )
# # ❸ エラーバーを正の値と負の値をそれぞれ指定
# error_fig.add_trace(
#     go.Bar(
#         x=x,
#         y=y,
#         error_y={
#             "symmetric": False,  # エラーバーを非対称
#             "type": "data",
#             "array": err_value,
#             "arrayminus": err_value_minus,  # 各要素の負の値を指定
#         },
#     ),
#     row=2,
#     col=1,
# )
# error_fig.show()


"""3.2.6 平行座標プロット（Parcoords trace）"""
# iris = plotly.data.iris()
# iris.head()

# go.Figure(
#     [
#         go.Parcoords(
#             dimensions=[
#                 {"label": "sepal_length", "values": iris["sepal_length"]},
#                 {"label": "sepal_width", "values": iris["sepal_width"]},
#                 {"label": "petal_length", "values": iris["petal_length"]},
#                 {"label": "petal_width", "values": iris["petal_width"]},
#             ],
#             line={"color": iris["species_id"]},  # ❶ species_idで色分け
#         )
#     ]
# ).show()


"""3.2.7 平行プロット（Parcats trace）"""
# tips = px.data.tips()
# tips.head()

# go.Figure(
#     [
#         go.Parcats(
#             dimensions=[
#                 {"label": "sex", "values": tips["sex"]},
#                 {"label": "smoker", "values": tips["smoker"]},
#                 {"label": "day", "values": tips["day"]},
#                 {"label": "time", "values": tips["time"]},
#             ],
#             line={"color": tips["size"]},  # ❶ size列で色分け
#         )
#     ]
# ).show()


"""3.2.8 ヒートマップ（Heatmap trace）"""
# np.random.seed(1)
# x = np.arange(0, 5)
# y = np.arange(0, 50, 10)
# z = np.random.randn(5, 5)

# go.Figure([go.Heatmap(x=x, y=y, z=z)]).show()


"""3.2.9 等高線図（Contour trace）"""
# np.random.seed(1)
# x = np.arange(0, 5)
# y = np.arange(0, 50, 10)
# z = np.random.randn(5, 5)

# go.Figure([go.Contour(x=x, y=y, z=z)]).show()


"""3.2.10 ポーラチャート（Scatterpolar trace）"""
# np.random.seed(7)
# r1 = np.random.rand(6)
# theta = np.linspace(0, 360, 7)[:-1]
# r1_close = np.hstack([r1, np.array(r1[0])])
# r2 = r1 + np.random.uniform(-0.3, 0.3, 6)
# r2_close = np.hstack([r2, np.array(r2[0])])
# label = list("abcdefa")

# polar_fig = make_subplots(
#     rows=2,
#     cols=2,
#     specs=[
#         [{"type": "polar"}, {"type": "polar"}],
#         [{"type": "polar"}, {"type": "polar"}],
#     ],
# )
# # ❶ 点で描画
# polar_fig.add_trace(
#     go.Scatterpolar(r=r1, theta=theta, mode="markers"), row=1, col=1
# )
# # ❷ 線で描画(レーダチャート)
# polar_fig.add_trace(
#     go.Scatterpolar(
#         r=r1_close, theta=label, mode="lines", fill="toself", name="r1"
#     ),
#     row=1,
#     col=2,
# )
# polar_fig.add_trace(
#     go.Scatterpolar(
#         r=r2_close, theta=label, mode="lines", fill="toself", name="r2"
#     ),
#     row=1,
#     col=2,
# )
# # ❸ 鶏頭図
# polar_fig.add_trace(go.Barpolar(r=r1, theta=label), row=2, col=1)
# polar_fig.add_trace(go.Barpolar(r=r2, theta=label), row=2, col=1)
# polar_fig.show()


"""3.2.11 三角図（Scatterternary trace）"""
# election = plotly.data.election()
# election.head()

# scatterternary_trace = go.Scatterternary(
#     a=election["Bergeron"],
#     b=election["Coderre"],
#     c=election["Joly"],
#     mode="markers",  # ❶
#     marker={"size": election["total"] * 1e-3},  # ❶
# )
# scatterternary_layout = go.Layout(
#     ternary={  # ❷
#         "aaxis": {"title": "Bergeron"},  # ❸
#         "baxis": {"title": "Coderre"},  # ❸
#         "caxis": {"title": "Joly"},  # ❸
#     }
# )
# go.Figure(scatterternary_trace, layout=scatterternary_layout)


"""3.2.12 ローソク足（Candlestick trace）"""
# stocks = plotly.data.stocks(indexed=True)
# stocks.index = pd.to_datetime(stocks.index)
# stocks.head()

# ohlc_df = (
#     stocks["GOOG"]
#     .resample("1M")  # 1週間ごとにリサンプル
#     .ohlc()  # 4本値にリサンプル
# )
# go.Figure(
#     [
#         go.Candlestick(
#             x=ohlc_df.index,
#             open=ohlc_df["open"],  # 始値
#             high=ohlc_df["high"],  # 高値
#             low=ohlc_df["low"],  # 安値
#             close=ohlc_df["close"],  # 終値
#         )
#     ]
# ).show()


"""3.2.13 ウォーターフォール図（Waterfall trace）"""
# go.Figure(
#     go.Waterfall(
#         x=[
#             "売上高",
#             "売上原価",
#             "売上総利益",
#             "販売費及び一般管理費",
#             "営業利益",
#             "営業外収益",
#             "営業外費用",
#             "経常利益",
#             "特別利益",
#             "特別損失",
#             "税引前当期純利益",
#             "法人税等",
#             "当期純利益",
#         ],
#         measure=[
#             "relative",
#             "relative",
#             "total",
#             "relative",
#             "total",
#             "relative",
#             "relative",
#             "total",
#             "relative",
#             "relative",
#             "total",
#             "relative",
#             "total",
#         ],
#         y=[1000, -300, 0, -150, 0, 100, -80, 0, 3, -5, 0, -100, 0],
#     )
# ).show()


"""3.2.14 ファンネル図（Funnel trace）"""
# funnel_fig = go.Figure()
# funnel_fig.add_trace(
#     go.Funnel(
#         name="商品A",
#         y=["閲覧", "クリック", "カートに追加", "購入"],
#         x=[300, 150, 20, 18],
#         textinfo="percent initial",  # ❶ 初期値からの変化
#     )
# )
# funnel_fig.add_trace(
#     go.Funnel(
#         name="商品B",
#         orientation="h",
#         y=["閲覧", "クリック", "カートに追加", "購入"],
#         x=[200, 40, 15, 13],
#         textinfo="label+percent previous",  # ❶ 前の値からの変化
#     )
# )
# funnel_fig.show()


"""3.2.15 階級区分図（Choropleth trace）"""
# gapminder = plotly.data.gapminder()
# gapminder_2007 = gapminder.loc[gapminder["year"] == 2007]
# gapminder_2007.head()

# go.Figure(
#     [
#         go.Choropleth(
#             locations=gapminder_2007["country"],  # ❶ 国名
#             locationmode="country names",  # 位置データを国名で指定
#             z=gapminder["lifeExp"],
#         )
#     ]
# ).show()


"""3.2.16 地図上の散布図（Scattergeo trace）"""
# populations = np.array([38_505_000, 34_365_000, 28_125_000])
# area = np.array([8_223, 3_367, 2_240])
# lon, lat = [139.691711, 106.845131, 77.216667], [35.6, -6.214620, 28.666668]
# text = ["Tokyo", "Jakarta", "Delhi"]
# go.Figure(
#     [
#         go.Scattergeo(
#             lon=lon,  # ❶ 経度
#             lat=lat,  # ❶ 緯度
#             # ❷
#             marker={
#                 "size": populations / 1_000_000,  # 要素の大きさ
#                 "color": populations / area,  # 要素の色
#                 "cmin": 1000,  # 色の下限値
#                 "cmax": 15000,  # 色の上限値
#                 # カラーバーを表示し、タイトルを指定
#                 "colorbar": {"title": "人口密度"},
#             },
#             text=text,  # ホバーツールに表示するテキスト
#             mode="markers",  # 散布図として描画,
#         )
#     ],
#     layout={"geo": {"scope": "asia"}},
# ).show()


"""3.2.17 地図上の折れ線グラフ（Scattergeo trace）"""
# populations = np.array([38_505_000, 34_365_000, 28_125_000])
# area = np.array([8_223, 3_367, 2_240])
# lon, lat = [139.691711, 106.845131, 77.216667], [35.6, -6.214620, 28.666668]
# text = ["Tokyo", "Jakarta", "Delhi"]

# go.Figure(
#     go.Scattergeo(
#         lon=lon + [-74.005966],  # ❶ 経度
#         lat=lat + [40.714272],  # ❶ 緯度
#         mode="lines",  # ❷ 要素間を線で接続
#         text=text,
#     ),
#     # ❸ 投影法を指定
#     layout={"geo": {"projection": {"type": "azimuthal equal area"}}},
# ).show()


"""3.2.18 mapbox の利用"""
# mapbox_token = mapbox_env.token
# go.Figure(
#     go.Scattermapbox(
#         lon=lon,
#         lat=lat,
#         text=text,
#         marker={
#             "size": populations / 1000000,
#             "color": populations / area,
#             "cmin": 1000,
#             "cmax": 15000,
#             "colorbar": {"title": "人口密度"},
#         },
#     ),
#     layout={
#         # ❶ Mapboxインスタンス
#         "mapbox": go.layout.Mapbox(
#             accesstoken=mapbox_token, center={"lat": 19, "lon": 95}, zoom=2
#         )
#     },
# ).show()


"""3.3 3Dグラフ"""
"""3.3.1 3D 散布図（Scatter3d trace）"""
# np.random.seed(1)
# bubble3d_data = np.random.rand(5, 100)
# go.Figure(
#     go.Scatter3d(
#         x=bubble3d_data[0],
#         y=bubble3d_data[1],
#         z=bubble3d_data[2],
#         mode="markers",  # ❶ 点で描画
#         # ❷ 要素のサイズと色を指定
#         marker={"size": bubble3d_data[3] * 10, "color": bubble3d_data[4]},
#     )
# ).show()


"""3. 3. 2 3D 折れ線グラフ（Scatter3d trace）"""
# line3d_z = np.linspace(-2, 2, 100)
# theta = np.linspace(-4 * np.pi, 4 * np.pi, 100)
# line3d_r = line3d_z ** 2 + 5
# line3d_x = line3d_r * np.sin(theta)
# line3d_y = line3d_r * np.cos(theta)
# go.Figure(
#     go.Scatter3d(
#         x=line3d_x,
#         y=line3d_y,
#         z=line3d_z,
#         # ❶ 線で描画
#         mode="lines",
#     )
# ).show()


"""3.3.3 サーフェスグラフ（Surface trace）"""
# surface_x, surface_y = np.mgrid[-10:10, -10:10]
# surface_z = surface_x ** 2 + surface_y ** 2 + surface_x * surface_y
# go.Figure(go.Surface(x=surface_x, y=surface_y, z=surface_z)).show()


"""3.3.4 メッシュグラフ（Mesh3d trace）"""
# np.random.seed(1)
# mesh3d_data = np.random.randn(3, 200)
# go.Figure(
#     go.Mesh3d(x=mesh3d_data[0], y=mesh3d_data[1], z=mesh3d_data[2])
# ).show()


"""4.1 サブプロット"""
# line_trace = go.Scatter(x=[0, 1, 2], y=[5, 3, 4], name="line")
# scatter_trace = go.Scatter(
#     x=[1, 2, 3], y=[2, 1, 5], mode="markers", name="scatter"
# )
# bar_trace = go.Bar(x=[1, 2, 3], y=[1, 2, 3], name="bar")
# area_trace = go.Scatter(
#     x=[3, 4, 5],
#     y=[5, 3, 4],
#     mode="none",
#     fillcolor="#1f77b4",
#     fill="tozeroy",
#     name="area",
# )
# subplots_fig = make_subplots(rows=2, cols=2)
# subplots_fig.add_trace(line_trace, row=1, col=1)
# subplots_fig.add_trace(scatter_trace, row=1, col=2)
# subplots_fig.add_trace(bar_trace, row=2, col=1)
# subplots_fig.add_trace(area_trace, row=2, col=2)
# subplots_fig.show()

# complex_fig = make_subplots(
#     rows=3,
#     cols=2,
#     # ❶
#     specs=[
#         # 1行目
#         [{}, {"rowspan": 2}],  # ❷ 行結合
#         # 2行目
#         [{}, None],
#         # 3行目
#         [{"colspan": 2}, None],  # ❸ 列結合
#     ],
#     shared_xaxes=True,  # X軸を共有
#     column_widths=[0.6, 0.4],  # 幅に割り当てる割合を指定
#     row_heights=[0.4, 0.4, 0.2],  # 高さに割り当てる割合を指定
# )
# complex_fig.add_trace(line_trace, row=1, col=1)
# complex_fig.add_trace(scatter_trace, row=1, col=2)
# complex_fig.add_trace(bar_trace, row=2, col=1)
# complex_fig.add_trace(area_trace, row=3, col=1)
# complex_fig.show()

# barpolar_trace = go.Barpolar(theta=[0, 60, 180], r=[6, 5, 3], name="barpolar")
# pie_trace = go.Pie(values=[30, 60, 10], labels=["a", "b", "c"], name="pie")
# scatter3d_trace = go.Scatter3d(
#     x=[1, 2, 3],
#     y=[5, 3, 4],
#     z=[2, 5, 1],
#     mode="markers",
#     marker={"size": 2},
#     name="3D scatter",
# )
# multiple_types_fig = make_subplots(
#     rows=2,
#     cols=2,
#     specs=[
#         [{"type": "xy"}, {"type": "polar"}],
#         [{"type": "domain"}, {"type": "scene"}],
#     ],
# )
# multiple_types_fig.add_trace(scatter_trace, row=1, col=1)
# multiple_types_fig.add_trace(barpolar_trace, row=1, col=2)
# multiple_types_fig.add_trace(pie_trace, row=2, col=1)
# multiple_types_fig.add_trace(scatter3d_trace, row=2, col=2)
# multiple_types_fig.show()


"""4.2 グラフのカスタマイズ"""
"""4.2.1 グラフのスタイル"""
# x = [1, 2, 3]
# line_y = [5, 3, 2]
# scatter_y = [-2, 4, 3]
# bar_y = [1, 3, 4]

# line_trace = go.Scatter(
#     x=x,
#     y=line_y,
#     # 折れ線グラフのスタイル
#     # colorを16進数で指定
#     line={"width": 5, "color": "#1f77b4", "dash": "dashdot"},
#     opacity=0.4,  # 不透明度
#     name="line",
# )
# scatter_trace = go.Scatter(
#     x=x,
#     y=scatter_y,
#     mode="markers",
#     # 要素のスタイル
#     marker={
#         "size": 20,
#         # colorをrgbaで指定
#         "color": "rgba(255, 127, 14, 0.5)",
#         "line": {"width": 3, "color": "rgba(214, 39, 40, 0.5)"},
#     },
#     name="scatter",
# )
# bar_trace = go.Bar(
#     x=x,
#     y=bar_y,
#     width=0.3,
#     marker={
#         # colorをrgbで指定
#         "color": ["rgb(255, 127, 14)", "rgb(44, 160, 44)", "rgb(214, 39, 40)"],
#         "line": {"width": 3, "color": "black"},
#     },
#     opacity=0.4,  # 不透明度
#     name="bar",
# )
# layout = go.Layout(
#     # グラフタイトルのスタイル
#     # colorをCSSカラーネームで指定
#     title={
#         "text": "Title",
#         "font": {"family": "arial", "size": 20, "color": "green"},
#     },
#     # X軸のスタイル
#     xaxis={
#         "title": {
#             "text": "X軸",
#             "font": {"family": "arial", "size": 10, "color": "navy"},
#         },
#         "tickfont": {"family": "arial", "size": 10, "color": "olive"},
#         "tickangle": 45,
#     },
#     # Y軸のスタイル
#     yaxis={
#         "title": {
#             "text": "Y軸",
#             "font": {"family": "arial", "size": 10, "color": "darkviolet"},
#         },
#         "showline": True,
#         "linewidth": 2,
#         "linecolor": "darkgray",
#         "gridwidth": 1,
#         "gridcolor": "indianred",
#         "zeroline": True,
#         "zerolinewidth": 2,
#         "zerolinecolor": "indigo",
#     },
# )
# go.Figure([line_trace, scatter_trace, bar_trace], layout=layout).show()


"""4.2.2 グラフサイズと余白"""
# fig = go.Figure(
#     go.Scatter(x=["2020-01-01", "2020-01-02", "2020-01-03"], y=[3, 5, 2])
# )
# fig.update_layout(
#     autosize=False,
#     width=300,
#     height=300,
#     # ❶ bを50に設定しているが、xaxis.automarginが優先される
#     margin={"l": 50, "r": 50, "b": 50, "t": 50, "pad": 15},
#     paper_bgcolor="lightcoral",
#     xaxis={"title": {"text": "X"}},
#     yaxis={"title": {"text": "y"}},
# )
# fig.show()

# fig = make_subplots(rows=1, cols=2)

# # ❶ X軸に日付、Y軸に対数をとった折れ線グラフ
# fig.add_trace(
#     go.Scatter(x=["2010", "2011", "2012"], y=[1, 10, 1000]), row=1, col=1
# )
# fig.update_xaxes(type="date", row=1, col=1)  # 日付
# fig.update_yaxes(type="log", row=1, col=1)  # 対数

# # ❷ サブカテゴリを持った棒グラフ
# fig.add_trace(go.Bar(x=[["1年", "1年"], ["A組", "B組"]], y=[70, 60]), row=1, col=2)
# fig.add_trace(go.Bar(x=[["2年", "2年"], ["A組", "B組"]], y=[70, 60]), row=1, col=2)
# fig.update_xaxes(type="multicategory", row=1, col=2)  # 階層カテゴリ
# fig.show()


"""4.2.3 軸の設定"""
# # Y軸に2軸目が存在するサブプロット
# two_yaxis_fig = make_subplots(specs=[[{"secondary_y": True}]]) 
# two_yaxis_fig.add_trace(go.Scatter(x=[1, 2, 3], y=[3, 2, 4], name="1st"))
# two_yaxis_fig.add_trace(
#     go.Scatter(x=[1, 2, 3], y=[1, 20, 15], name="2nd"),
#     secondary_y=True,  # traceを2軸目とする
# )
# two_yaxis_fig.update_yaxes(title={"text": "1st"}, showgrid=False)
# two_yaxis_fig.update_yaxes(
#     secondary_y=True,  # 2軸目の設定
#     title={"text": "2nd"},  # 軸ラベルの指定
#     showgrid=False  # 補助線を非表示
# )
# two_yaxis_fig.show()

# config_tick_fig = make_subplots(
#     rows=2, cols=2, horizontal_spacing=0.15, vertical_spacing=0.2
# )
# config_tick_fig.add_trace(go.Scatter(x=[1, 2, 3], y=[5, 3, 4]))
# config_tick_fig.update_xaxes(
#     tick0=2, dtick=0.3, title="2を基準に刻み幅を0.3", row=1, col=1
# )
# config_tick_fig.update_yaxes(
#     autorange="reversed", title="Y軸の順序を逆に設定", row=1, col=1
# )

# config_tick_fig.add_trace(go.Scatter(x=[1, 2, 3], y=[5, 3, 4]), row=1, col=2)
# config_tick_fig.update_xaxes(
#     tickvals=[1.8, 2, 2.2], title="表示する目盛を指定", row=1, col=2
# )
# config_tick_fig.update_yaxes(range=[2, 4], title="描画範囲を指定", row=1, col=2)

# config_tick_fig.add_trace(go.Scatter(x=[-1, 0, 1], y=[4, 5, 3]), row=2, col=1)
# config_tick_fig.update_xaxes(
#     rangemode="nonnegative", title="正の値の範囲のみを描画", row=2, col=1
# )
# config_tick_fig.update_yaxes(
#     rangemode="tozero", title="0からの範囲を描画", row=2, col=1
# )
# config_tick_fig.show()

# x = [1, 2, 3]
# various_legend_fig = go.Figure()
# various_legend_fig.add_trace(go.Scatter(x=x, y=[5, 3, 2]))  # ❶
# various_legend_fig.add_trace(go.Scatter(x=x, y=[4, 2, 3], name="line2"))  # ❷
# various_legend_fig.add_trace(
#     go.Scatter(x=x, y=[3, 5, 4], name="line3", showlegend=False)  # ❸
# )
# various_legend_fig.show()

# horizontal_legend_fig = go.Figure()
# horizontal_legend_fig.add_trace(go.Scatter(x=x, y=[5, 3, 2], name="line1"))
# horizontal_legend_fig.add_trace(go.Scatter(x=x, y=[4, 2, 3], name="line2"))
# horizontal_legend_fig.update_layout(legend_orientation="h")  # ❶ 横並びの凡例
# horizontal_legend_fig.show()

# moved_legend_fig = go.Figure()
# moved_legend_fig.add_trace(go.Scatter(x=x, y=[5, 3, 2], name="line1"))
# moved_legend_fig.add_trace(go.Scatter(x=x, y=[4, 2, 3], name="line2"))
# moved_legend_fig.layout.update(legend={"x": -0.15, "y": 0.5})  # ❶ 凡例の位置
# moved_legend_fig.show()

# grouped_legend_fig = go.Figure()
# grouped_legend_fig.add_trace(
#     go.Scatter(x=x, y=[5, 3, 2], name="A-1", legendgroup="groupA")
# )
# grouped_legend_fig.add_trace(
#     go.Scatter(x=x, y=[3, 5, 4], name="B-1", legendgroup="groupB")
# )
# grouped_legend_fig.add_trace(
#     go.Scatter(x=x, y=[4, 2, 3], name="A-2", legendgroup="groupA")
# )
# grouped_legend_fig.add_trace(
#     go.Scatter(x=x, y=[2, 3, 4], name="B-2", legendgroup="groupB")
# )
# grouped_legend_fig.show()


"""4.2.5 カラースケール"""
# np.random.seed(1)
# go.Figure(
#     go.Heatmap(
#         z=np.random.randn(10, 10),
#         colorscale="PuBu",  # カラースケール
#         zmin=-1,  # ❶ 値の最小値
#         zmax=3,  # ❶ 値の最大値
#     )
# ).show()

# np.random.seed(1)
# x, y, z = np.random.randn(3, 100)
# go.Figure(
#     go.Scatter(
#         x=x,
#         y=y,
#         mode="markers",
#         marker={
#             "color": z,
#             "colorscale": "Greens",
#             "cmin": -1,
#             "cmax": 1,
#             # ❶ カラーバー、0を基準に0.2刻みの目盛を表示
#             "colorbar": {"title": "z", "tick0": 0, "dtick": 0.2},
#         },
#     )
# ).show()

# go.Figure(
#     go.Heatmap(
#         z=np.random.randn(10, 10),  # ❶ カスタマイズしたカラースケール
#         colorscale=[
#             [0, "rgb(0,255,255)"],
#             [0.5, "rgb(0,80,80)"],
#             [1, "rgb(0,20,20)"],
#         ],
#     )
# ).show()


"""4.3 オブジェクトの描画"""
"""4.3.1 テキストの描画と設定"""
# go.Figure(
#     go.Scatter(
#         x=[1, 2, 3],
#         y=[3, 5, 2],
#         text=["A", "B", "C"],
#         mode="text",  # ❶ テキストを描画
#         textfont={"size": 20},  # ❷ フォントサイズを指定
#     )
# ).show()

# textpositions = [
#     "top left",
#     "top center",
#     "top right",
#     "middle left",
#     "middle center",
#     "middle right",
#     "bottom left",
#     "bottom center",
#     "bottom right",
# ]

# fix_text_position_fig = go.Figure(layout={"showlegend": False})  # 凡例を非表示
# for i, textposition in enumerate(textpositions):
#     fix_text_position_fig.add_trace(
#         go.Scatter(
#             x=[1, 2, 3],
#             y=[i, i, i],
#             text=[None, textposition, None],
#             mode="lines+markers+text",  # 線、点、テキストを描画
#             textposition=textposition,  # ❶ テキストの位置を指定
#         )
#     )
# fix_text_position_fig.show()

# annotate_text_fig = go.Figure()
# annotate_text_fig.add_trace(go.Scatter(x=[1, 2, 3], y=[3, 5, 2], mode="lines"))
# annotate_text_fig.update_layout(
#     annotations=[
#         go.layout.Annotation(
#             x=2,
#             y=5,
#             text="max=5",
#             showarrow=True,  # 矢印を表示
#             arrowhead=1,  # 矢印の形状
#             bgcolor="midnightblue",  # テキスト部分の塗りつぶし色
#             font={"size": 15, "color": "white"},  # フォントサイズと色
#         ),
#         go.layout.Annotation(
#             x=3,
#             y=2,
#             text="min=2",
#             showarrow=True,
#             arrowhead=1,
#             bgcolor="mediumvioletred",
#             font={"size": 15, "color": "white"},
#         ),
#     ]
# )

# paper_fig = go.Figure()
# paper_fig.update_layout(
#     annotations=[
#         go.layout.Annotation(
#             # 描画領域を基準
#             xref="paper",
#             yref="paper",
#             x=0.5,
#             y=0.5,
#             showarrow=False,
#             text="領域内に描画",
#         ),
#         go.layout.Annotation(
#             xref="paper",
#             yref="paper",
#             x=0.25,
#             y=-0.2,
#             showarrow=False,
#             text="領域外に描画",
#         ),
#     ]
# )
# paper_fig.show()


"""4.3.2 図形の描画"""
# rect_fig = go.Figure()
# rect_fig.add_trace(go.Scatter(x=[1, 2, 3], y=[3, 5, 2]))
# rect_fig.update_layout(
#     shapes=[
#         go.layout.Shape(
#             type="rect",  # 長方形
#             xref="x",  # X座標
#             yref="paper",  # 描画領域からの相対位置
#             x0=1.8,  # X座標の開始位置
#             x1=2.2,  # X座標の終了位置
#             y0=0,  # Y座標の開始位置
#             y1=1,  # Y座標の終了位置
#             fillcolor="LightSalmon",  # 塗りつぶし色
#             opacity=0.5,  # 不透明度
#             layer="below",  # traceの背面に描画
#             line={"width": 0},  # 枠線を表示しない
#         )
#     ]
# )
# rect_fig.show()

# np.random.seed(1)
# x0 = np.random.normal(2, 0.45, 300)
# y0 = np.random.normal(2, 0.45, 300)
# x1 = np.random.normal(6, 0.4, 200)
# y1 = np.random.normal(6, 0.4, 200)

# circle0 = go.layout.Shape(
#     type="circle",  # 円を描画
#     x0=min(x0),
#     y0=min(y0),
#     x1=max(x0),
#     y1=max(y0),
#     opacity=0.2,
#     fillcolor="blue",
#     line={"width": 0},
# )
# circle1 = go.layout.Shape(
#     type="circle",
#     x0=min(x1),
#     y0=min(y1),
#     x1=max(x1),
#     y1=max(y1),
#     opacity=0.2,
#     fillcolor="orange",
#     line={"width": 0},
# )
# circle_fig = go.Figure()
# circle_fig.add_trace(go.Scatter(x=x0, y=y0, mode="markers", name="groupA"))
# circle_fig.add_trace(go.Scatter(x=x1, y=y1, mode="markers", name="groupB"))
# circle_fig.update_layout(shapes=[circle0, circle1])
# circle_fig.show()

# svg_fig = go.Figure()
# svg_fig.update_layout(
#     shapes=[
#         go.layout.Shape(
#             type="path",  # SVGパスを指定
#             path=" M 1 1 L 1 3 L 4 1 Z",  # ❶ SVGパス
#             fillcolor="LightPink",
#         )
#     ]
# )
# svg_fig.show()


"""4.4 インタラクティブな可視化"""
"""4.4.1 ホバーツールの設定"""
# go.Figure(
#     go.Scatter(
#         x=[1, 2, 3],
#         y=[3, 5, 2],
#         # ホバーツールに表示するテキスト
#         hovertext=["a", "b", "c"],
#         # Y値とテキストを表示
#         hoverinfo="y+text",
#     )
# ).show()

# go.Figure(
#     go.Scatter(
#         x=[1, 2, 3],
#         y=[3.1415, 5.4772, 1.7320],
#         # ホバーツールのテンプレート
#         hovertemplate="Y値を小数点2桁で表示<br><b>y:</b> %{y:.2f}",
#     )
# ).show()


"""4.4.2 コールバックによるインタラクティブな可視化"""
# change_title_fig = go.FigureWidget(go.Scatter(x=[1, 2, 3], y=[3, 5, 2]))
# change_title_fig.update_layout(width=400, height=300)


# # ❷ グラフタイトルを変更するコールバック関数
# def update_title(trace, points, selector):
#     n = points.point_inds[0] + 1  # ❸
#     # ❹ layout.title.text属性を変更
#     change_title_fig.layout.title.text = f"{n}番目の要素をクリックしました"


# change_title_fig.data[0].on_click(update_title)  # ❶ クリック時のイベント
# change_title_fig

# gapminder = plotly.data.gapminder()

# # ❶ 引数にfigureを渡す
# subplots_fig = go.FigureWidget(make_subplots(rows=1, cols=2))
# subplots_fig.add_trace(
#     go.Scatter(
#         x=gapminder["gdpPercap"],
#         y=gapminder["lifeExp"],
#         text=gapminder["country"],
#         mode="markers",
#         name="散布図",
#     ),
#     row=1,
#     col=1,
# )
# subplots_fig.add_trace(go.Scatter(name="時系列データ"), row=1, col=2)
# trace0, trace1 = subplots_fig.data
# title_text = "1人当りGDPと平均寿命の散布図（左図）と平均寿命の時系列データ（右図）"
# subplots_fig.update_layout(title={"text": title_text})
# # 軸ラベル
# subplots_fig.update_xaxes(title="1人当りGDP", type="log", row=1, col=1)
# subplots_fig.update_xaxes(title="年", type="log", row=1, col=2)
# subplots_fig.update_yaxes(title="平均寿命")


# def update_line(trace, points, selector):  # ❷
#     n = points.point_inds[0]
#     country = gapminder.iloc[n, 0]  # ❸ インデックスから国名を取得
#     # ❸ 国名からデータを抽出
#     country_df = gapminder.loc[gapminder["country"] == country].sort_values(
#         "year"
#     )
#     trace1.x = country_df["year"]  # ❹
#     trace1.y = country_df["lifeExp"]  # ❹
#     subplots_fig.update_layout(  # ❺
#         annotations=[
#             {
#                 "x": 1,
#                 "y": 1.1,
#                 "showarrow": False,
#                 "text": country,
#                 "xref": "paper",
#                 "yref": "paper",
#             }
#         ]
#     )


# trace0.on_click(update_line)
# subplots_fig


"""4.5 グラフを画像ファイルに出力"""
# !pip install plotly==4.10.0
# !wget https://github.com/plotly/orca/releases/download/v1.2.1/orca-1.2.1-x86_64.AppImage -O /usr/local/bin/orca
# !chmod +x /usr/local/bin/orca
# !apt-get install xvfb libgtk2.0-0 libgconf-2-4

# fig = go.Figure([go.Scatter(x=[1, 2, 3], y=[5, 3, 2])])
# fig.write_image("fig1.png")

# img_bytes = fig.to_image(format="png")
# Image(img_bytes)
