#import bokeh for plotting graph
from bokeh.plotting import figure
from bokeh.io import output_file,show

#prepare some test data
x=[1,2,3,4,5]
y=[6,7,8,9,10]

#prepare the output file
output_file("Line.html")

#create a figure object
f=figure()

#create line plot
f.line(x,y)

show(f)