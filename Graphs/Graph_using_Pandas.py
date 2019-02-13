#import bokeh for plotting graph
from bokeh.plotting import figure
from bokeh.io import output_file,show
import pandas

#prepare some test data
df=pandas.read_csv("data.csv")
x=df["x"]
y=df["y"]

#prepare the output file
output_file("Line from CSV.html")

print(df)

#create a figure object
f=figure()

#create line plot
f.line(x,y)

show(f)