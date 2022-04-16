from cgitb import reset
from tkinter import Menu
import pandas as pd
import plotly.figure_factory as ff
import statistics as st

df = pd.read_csv("data.csv")
height = df["Height(Inches)"].to_list()

mean = st.mean(height)
median = st.median(height)
mode = st.mode(height)
stdev = st.stdev(height)

first_start, first_end = mean - stdev, mean + stdev
second_start, second_end = mean - (2*stdev), mean + (2*stdev)
third_start, third_end = mean - (3*stdev), mean + (3*stdev)


height_within_first_stdev = [result for result in height if result > first_start and result < first_end]
height_within_second_stdev = [result for result in height if result > second_start and result < second_end]
height_within_third_stdev = [result for result in height if result > third_start and result < third_end]

print("{}% of data lies within first stdev ".format(len(height_within_first_stdev)*100/len(height)))
print("{}% of data lies within second stdev ".format(len(height_within_second_stdev)*100/len(height)))
print("{}% of data lies within third stdev ".format(len(height_within_third_stdev)*100/len(height)))

#print(mean, median, mode, stdev)