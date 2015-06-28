import numpy as np
from collections import OrderedDict
from bokeh.plotting import figure, show, output_file, vplot
from bokeh.charts import Bar, output_file, show
#from bokeh.plotting import *

output_file("new_trend_fig.html", title="time_slope_fig")

# (dict, OrderedDict, lists, arrays and DataFrames are valid inputs)
xyvalues = OrderedDict()
xyvalues['March']=[0.40, 0.40, 0.40]
xyvalues['April']=[0.37, 0.34, 0.48]
xyvalues['May']=[0.42,0.28, 0.54]

cat = ['Constant', 'Decrease', 'Increase']

# bar = Bar(xyvalues, cat, title="Monitor Average Leaving Prob By Month", \
# 	xlabel="Trends", ylabel="Average Leaving Prob", legend = 'top_left')


bar = Bar(xyvalues, cat, title="Monitor Individual Leaving Prob By Month", \
	xlabel="Trends", ylabel="Individual Leaving Prob", legend = 'top_left')

show(bar)
# show(vplot(bar,bar1))
























