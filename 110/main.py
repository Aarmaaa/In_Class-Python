import pandas as pd
import plotly.express as px
import statistics as st
import plotly.figure_factory as ff
import plotly.graph_objects as go
import random

df = pd.read_csv("data2.csv")
data = df["temp"].tolist()

""" mean = st.mean(data)
median = st.median(data)
mode = st.mode(data)
stdev = st.stdev(data)
print(mean)
#print(median)
#print(mode)
print(stdev) """


""" #Taking sample of 100 data points
sample = []
for i in range(0, 100):
    random_index = random.randint(0, len(data)-1)
    value = data[random_index]
    sample.append(value)

mean1 = st.mean(sample)
stdev1 = st.stdev(sample)

print(mean1, stdev1)
 """
""" fig = ff.create_distplot([data], ["temperature"], show_hist = False)
fig.add_trace(go.Scatter(x=[mean,mean], y = [0, 0.1], mode = "lines", name = "MEAN" ))
#fig.show() """

#Picking a sample of 100 data points
def pickSample():
    dataset = []
    for i in range(0, 100):
        random_index = random.randint(0, len(data)-1)
        value = data[random_index]
        dataset.append(value)
    mean = st.mean(dataset)
    return mean

def setup():
    means = []
    for i in range(0, 1000):
        mean = pickSample()
        means.append(mean)
    mean = st.mean(means)
    showfigure(means)
    print(mean)

def showfigure(meanlist):
    df = meanlist
    mean = st.mean(df)
    fig = ff.create_distplot([df], ["means"], show_hist = False)
    fig.add_trace(go.Scatter(x=[mean, mean], y = [0, 0.7], mode = "lines", name = "Mean"))
    fig.show()

def stdev():
    means = []
    for i in range(0, 1000):
        mean = pickSample()
        means.append(mean)
    stdev = st.stdev(means)
    print(stdev)

setup()
stdev()