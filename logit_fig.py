import numpy as np
from bokeh.plotting import figure, show, output_file, vplot
#from bokeh.plotting import *


x_range = [-5, 5]
y_range = [-0.05,1.4]


output_file("logit_fig.html", title="logistic regression model")
p1 = figure(title="Logistic Regression Model Prediction", tools="resize,save", \
	y_range=y_range, x_range=x_range)
#two lines as the bound
p1.segment([-5,-5],[0,1],[5,5],[0,1], line_width =1, line_color = 'gray', line_dash ='dashed')

#add labels
p1.xaxis.axis_label = 'Composite of all Variables'
p1.yaxis.axis_label = 'Probability of Leaving of Employees'

#add curves for logistic function
N = 400
x = np.linspace(-5, 5, N)
y =  1/(1+np.exp(-x))
p1.line(x, y, legend= 'logistic model', fill_color=None, line_color="#0000FF", line_width = 3,line_alpha = 0.65)
p1.legend.orientation = "top_right"

# add points scatter around logistic curve
x = [.6, 0.9,1.1,1.5,1.8, 2.32,2.47,3.54,4.59]
y =  [1]*len(x)
p1.scatter(x, y, marker='circle', legend = 'Stay Right', line_color="gray", fill_color="green", fill_alpha=0.5, size=10)
p1.scatter([-0.5], [1], marker='circle_x', legend = 'Stay Wrong', line_color="gray", fill_color="green", fill_alpha=0.5, size=10)

x = [-.6, -0.9,-1.1,-1.5,-1.8, -2.32,-2.47,-3.54,-4.59]
y = [0]*len(x)
p1.scatter(x, y, marker='circle', legend = 'Leave right', line_color="gray", fill_color="red", fill_alpha=0.5, size=10)
p1.scatter([0.5], [0], marker='circle_x', legend = 'Leave Wrong', line_color="gray", fill_color="red", fill_alpha=0.5, size=10)
#colored points
p1.segment([0],[-0.05],[0],[1.4], line_width = 4, line_color = 'gray', line_dash ='dashed')
show(p1)









