#import bokeh for plotting graph
from bokeh.plotting import figure
from bokeh.io import output_file,show
import pandas

#prepare some test data
df=pandas.read_csv("bachelors.csv")
x=df["Year"]
y=df["Engineering"]

#prepare the output file
output_file("Line from Bachelors.html")

print(df)

#create a figure object
f=figure()

#create line plot
f.line(x,y)

show(f)