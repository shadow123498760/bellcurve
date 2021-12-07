
import plotly.figure_factory as ff
import pandas as pd
import csv 

df = pd.read_csv("data.csv")
fig = ff.create_displot([df["height(inches)"].tolist()], ["height"] show_hist=False)
fig.show()

