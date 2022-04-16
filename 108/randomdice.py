import random

sum = []
count = []
for i in range(0, 100):
    dice1 = random.randint(1, 6)
    dice2 = random.randint(1, 6)
    sum.append(dice1+dice2)
    count.append(i)

print(count, sum)

import plotly.express as px
import plotly.figure_factory as ff

fig = ff.create_distplot([sum], ["Dice Result"])
fig.show()