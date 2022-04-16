import csv
import pandas as pd     
import plotly.express as px


with open("class2.csv", newline = '') as f:
    reader = csv.reader(f)
    file_data = list(reader)

file_data.pop(0)

#MEAN
n = len(file_data)
sum = 0

for i in file_data:
    sum = sum + float(i[1]) 

mean = sum/n
print(mean)

df = pd.read_csv("class2.csv")

fig = px.scatter(df, x = "Student Number", y = "Marks")

fig.update_layout(shapes = [dict(
    type = "line",
    x0 = 0,
    x1 = n,
    y0 = mean,
    y1 = mean
    )])
fig.update_yaxes(rangemode = "tozero")
fig.show()