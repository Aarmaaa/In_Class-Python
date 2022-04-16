import pandas as pd
import plotly.express as px
import plotly.figure_factory as ff

df = pd.read_csv("data.csv")
height = df["Height(Inches)"].tolist()

fig = ff.create_distplot([height], ["Height"], show_hist = False)
fig.show()