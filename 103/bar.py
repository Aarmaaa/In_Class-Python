import pandas as pd
import plotly.express as px

df = pd.read_csv("data.csv")

fig = px.bar(df, x ="Country", y = "InternetUsers", color="Country" ,title = "Internet Users" )
fig.show()