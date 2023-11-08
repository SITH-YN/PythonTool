import plotly.express as px

gapminder = px.data.gapminder()
gapminder.head()

px.scatter(
    gapminder,
    x="gdpPercap",
    y="lifeExp",
    log_x=True,
    hover_name="country",
    size="pop",  # 人口を点の大きさで表現
    size_max=40,  # 点の大きさの最大値
    color="continent",  # 大陸ごとに色分け
).show()
