import pandas as pd
import plotly.figure_factory as ff

df = pd.read_csv("data.csv")
weight = df["Weight(Pounds)"].tolist()

fig = ff.create_distplot([weight], ["weight"], show_hist = False)
fig.show()