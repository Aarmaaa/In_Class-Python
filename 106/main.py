import csv
import plotly.express as px
import numpy as np

with open("data.csv") as f:
    df = csv.DictReader(f)
    fig = px.scatter(df, x = "Temperature", y = "Ice-cream Sales( â‚¹ )" )
    fig.show()

