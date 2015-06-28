import numpy as np
from bokeh.plotting import figure, show, output_file, vplot
#from bokeh.plotting import *

def gene_normal_with_limit(mean, std, size, limit, rounding = 0):
	i = 1
	res = []
	while i <= size:
		tmp = round(np.random.normal(mean, std), rounding)
		if tmp>= limit[0] and tmp <= limit[1]:
			res.append(tmp)
			i += 1
	return np.array(res)		


x_range = [-4, 4]
y_range = [-3, 4]

output_file("new_trend_fig.html", title="new_trend_fig")
p1 = figure(title="Detect New Trends or Changes", tools="resize,save", \
	y_range=y_range, x_range=x_range)

#add labels
p1.xaxis.axis_label = 'Job Satisfication'
p1.yaxis.axis_label = 'Inner Pressure'


#scatter the stay dots as green
np.random.seed(117)
x = gene_normal_with_limit(2.5, 1.5, 20, [-1,3.9], rounding = 1)
y = 0.6*x + 1 + gene_normal_with_limit(-2, 1, 20, [-2.9,3], rounding = 1) -1
p1.scatter(x, y, marker='circle', legend = 'Stay', line_color="gray", fill_color="green", fill_alpha=0.5, size=10)
# x1 = x
# y1 = y
# -0.2,-0.52
# approximate---3.8,2.18

#scatter the leave dots as red
np.random.seed(8)
x = gene_normal_with_limit(2, 1.5, 20, [-3,1.5], rounding = 1)
y = x*0.3 + 4 + gene_normal_with_limit(-2, 1, 20, [-2.9,3], rounding = 1)
p1.scatter(x, y, marker='circle', legend = 'Leave', line_color="gray", fill_color="red", fill_alpha=0.5, size=10)

# x2 = x
# y2 = y
# 0.2, 1.26
# y = 0.755*x+1.109
#add the margin two lines and some points on them
# a = .755
# b = -.369
p1.segment([-3],[-2.634],[3.8],[2.5], line_width = 4, line_color = 'gray', line_dash ='dashed', line_alpha = 0.75)
p1.segment([-3.5],[-1.609],[3.8],[3.978], line_width = 4, line_color = 'gray', line_dash ='dashed', line_alpha = 0.75)

# add the middle line--the exact model on the graph
# -0.2 + 0.2= 0
# -0.52+1.26= .37
# y = .755*x + .37

p1.segment([-3.25],[-2.084],[3.8],[3.239], legend = 'SVM model', line_width = 4, line_color = 'black', line_dash ='solid', line_alpha = 0.8)
#add legend


#set legend position
p1.legend.orientation = "top_left"

#add dots for condition 1
# np.random.seed(126)
# x = gene_normal_with_limit(3, 0.5, 7, [2,4], rounding = 1)
# y = gene_normal_with_limit(3, 0.5, 7, [2,4], rounding = 1)
# p1.scatter(x, y, marker='triangle', legend = 'New Stay', line_color="gray", fill_color="green", fill_alpha=0.5, size=12)
# x = gene_normal_with_limit(3, 0.5, 7, [2,4], rounding = 1)
# y = gene_normal_with_limit(3, 0.5, 7, [2,4], rounding = 1)
# p1.scatter(x, y, marker='triangle', line_color="gray",  legend = 'New Leave' ,fill_color="red", fill_alpha=0.5, size=12)


#add dots for condition 2
np.random.seed(777)
x = gene_normal_with_limit(-2, 0.5, 7, [-3,-1], rounding = 1)
y = gene_normal_with_limit(-2, 0.5, 7, [-3,-1], rounding = 1)
p1.scatter(x, y, marker='triangle', legend = 'New Stay', line_color="gray", fill_color="green", fill_alpha=0.5, size=12)
x = gene_normal_with_limit(-2, 0.5, 7, [-3,-1], rounding = 1)
y = gene_normal_with_limit(-2, 0.5, 7, [-3,-1], rounding = 1)
p1.scatter(x, y, marker='triangle', line_color="gray",  legend = 'New Leave' ,fill_color="red", fill_alpha=0.5, size=12)

show(p1)









