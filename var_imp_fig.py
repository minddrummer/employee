from collections import OrderedDict
from bokeh.charts import Bar, output_file, show,Horizon
import numpy as  np
import matplotlib.pyplot as plt; plt.rcdefaults()
import mpld3
import matplotlib.pyplot as plt

imp_var = ['Outer Pressure',
	'Job Satisfication',
	'Job Avoidance',
	'Average No Work Time',
	'Inner Pressure',
	'Low Achievement',
	'Job Intensity',
	'Last No Work Time',
	'Emotional Burnout',
	'Individual Assess Score']

imp_coef =[0.02,
	0.02,
	0.059999999999999998,
	0.080000000000000002,
	0.080000000000000002,
	0.12,
	0.14000000000000001,
	0.14000000000000001,
	0.14000000000000001,
	0.17999999999999999]

imp_coef_100 = list((np.array(imp_coef)/imp_coef[-1])*100)



# imp_var = [i[0] for i in imp[:10]][::-1]
# imp_coef = [i[1] for i in imp[:10]][::-1]
pos = np.arange(10)+.5
fig = plt.figure(1)
plt.barh(pos,imp_coef_100, align='center', alpha = 0.8, color = '#0066FF', linewidth = 3, edgecolor = '#888888')
plt.yticks(pos, imp_var)
plt.xlabel('Variable Importance Score', fontsize=14)
plt.title('Top 10 Important Variables From Boosting Tree', fontsize=22)
#plt.grid(True)
#plt.show()
#mpld3.show()
#plt.tight_layout()
fig.savefig('top10importance_boostingTree.png', bbox_inches='tight')
#plt.close()

# standard = imp_coef[-1]
# imp_coef_100 =  [[i*100/standard] for i in imp_coef]
# #imp_coef_100 =  [i*100/standard for i in imp_coef]
# # (dict, OrderedDict, lists, arrays and DataFrames are valid inputs)

# xyvalues = OrderedDict(zip(imp_var, imp_coef_100))

# #Bar(values, cat=None, stacked=False, xscale='categorical', yscale='linear',  continuous_range=None, **kw)
# bar = Bar(xyvalues, xscale='categorical',xgrid=True, ygrid=True, title="Top 10 Important Variables From Boosting Tree", xlabel="", ylabel="Variable Importance")
# output_file("bar.html")
# show(bar)


