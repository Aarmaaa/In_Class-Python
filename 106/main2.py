import csv
import plotly.express as px
import numpy as np


#Function to convert the datasets into lists
def getDataSource(data_path):
    ice_cream = []
    temp = []
    with open(data_path) as f:
        reader = csv.DictReader(f)
        for row in reader:
            temp.append(float(row['Temperature']))
            ice_cream.append(float(row['Ice-cream Sales( â‚¹ )']))
    return {'x':temp, 'y':ice_cream}


def findCorr(datasource):
    correlation = np.corrcoef(datasource['x'], datasource['y'])
    print(correlation[0, 1])


def setup():
    data_path = "data.csv"
    datasource = getDataSource(data_path)
    findCorr(datasource)

setup()