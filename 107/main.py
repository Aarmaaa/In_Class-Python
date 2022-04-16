import csv
import pandas as pd
import plotly.graph_objects as go

dataframe = pd.read_csv("data.csv")

groupbylevel = dataframe.groupby("level")["attempt"].mean()

fig = go.Figure(go.Bar(
    x = groupbylevel,
    y = ["level 1", "level 2", "level 3", "level 4"],
    orientation = "h"
))
fig.show()