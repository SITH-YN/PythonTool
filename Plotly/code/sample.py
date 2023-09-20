"""sample code."""
import plotly.express as px

gapminder = px.data.gapminder()
gapminder.head()

gapminder.plot.scatter(x="gdpPercap", y="lifeExp", logx=True, xlim=[100, 1e6])

px.scatter(gapminder, x="gdpPercap", y="lifeExp", logx=True, hover_name="country").show()
