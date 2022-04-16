import random
import plotly.figure_factory as ff
import statistics as st
import plotly.graph_objects as go

dice_result = []

for i in range(0, 1000):
    dice1 = random.randint(1,6)
    dice2 = random.randint(1,6)
    dice_result.append(dice1+dice2)

mean = sum(dice_result)/len(dice_result)
median = st.median(dice_result)
mode = st.mode(dice_result)
stdev = st.stdev(dice_result)

print(mean, median, mode, stdev)


#Creating 3 ranges of standard deviation
first_stdev_start, first_stdev_end = mean - stdev , mean + stdev
second_stdev_start, second_stdev_end = mean - (2*stdev), mean + (2*stdev)
third_stdev_start, third_stdev_end = mean - (3*stdev), mean + (3*stdev)


fig = ff.create_distplot([dice_result], ["Result"], show_hist = False)

fig.add_trace(go.Scatter( x = [mean, mean], y = [0, 0.17], mode = 'lines', name = "MEAN"))
fig.add_trace(go.Scatter( x = [first_stdev_start, first_stdev_start], y = [0, 0.17], mode = 'lines', name = "First stdev start"))
fig.add_trace(go.Scatter( x = [first_stdev_end, first_stdev_end], y = [0, 0.17], mode = 'lines', name = "First stdev end"))
fig.add_trace(go.Scatter( x = [second_stdev_start, second_stdev_start], y = [0, 0.17], mode = 'lines', name = "second stdev start"))
fig.add_trace(go.Scatter( x = [second_stdev_end, second_stdev_end], y = [0, 0.17], mode = 'lines', name = "second stdev end"))

fig.show()