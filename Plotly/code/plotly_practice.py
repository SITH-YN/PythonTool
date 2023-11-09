import numpy as np
import pandas as pd
import plotly.express as px

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

# df = pd.DataFrame([[1, 1], [2, 5], [3, 3]], columns=["x", "y"])
# px.line(df, x="x", y="y").show()

# tips = px.data.tips()
# tips.head()
# px.scatter(tips, x="total_bill", y="tip").show()

# px.line(x=[1, 2, 3], y=[3, 5, 2]).show()

# np.random.seed(1)
# arr = np.random.rand(100, 4)
# px.scatter(arr, x=0, y=1, color=2, size=3).show()

tips = px.data.tips()
tips.head()
px.scatter(
    tips,
    x="total_bill",
    y="tip",
    color="size",  # size列で色分け
    facet_row="time",  # 縦に分割
    facet_col="sex",  # 横に分割
).show()
