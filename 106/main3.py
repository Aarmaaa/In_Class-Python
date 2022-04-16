import csv
from os import read
from main2 import getDataSource
import plotly.express as px
import numpy as np

def getData(data_path):
    tvSize = []
    avgTime = []


    with open(data_path) as file :
        reader = csv.DictReader(file)
        for row in reader:
            tvSize.append(float(row["Size of TV"]))
            avgTime.append(float(row["\tAverage time spent watching TV in a week (hours)"]))
    return {'x': tvSize, 'y': avgTime }

def findCorr(datasource):
    correlation = np.corrcoef(datasource['x'], datasource['y'])
    print(correlation[0,1])

def setup():
    data_path = "data3.csv"
    datasource = getData(data_path)
    findCorr(datasource)
    
setup()     