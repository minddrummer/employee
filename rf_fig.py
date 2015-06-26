import numpy as np
from bokeh.plotting import figure, show, output_file, vplot
#from bokeh.plotting import *


x_range = [-20, 210]
y_range = [-120, 510]


output_file("random_forest.html", title="random forest model")
p1 = figure(title="Random Forest Model Prediction", tools="resize,save", \
	y_range=y_range, x_range=x_range)

#the first set of dots and lines
y0 = [420, 260, -40]
y1 = [460,380,300,220,0,-80] 
x0 = [10, 10, 10]
x1 = [40]*6
tmpx = x0*2
tmpy = [420, 420, 260, 260, -40, -40]

y2 = [460,380,300,220,0,-80] 
y3 = [475,445,395,365,315,285,235,205,15,-15,-65,-95] 
x2 = [40]*6
x3 = [100]*12
x3_yes = [100]*3
y3_yes = [y3[1],y3[6],y3[11]]
x3_no = [100]*9
y3_no = [i for i in y3 if i not in y3_yes]
tmpx2 = x2*2
tmpy2 = reduce(lambda total,x: total+x,map(lambda x: [x,x], y2))



p1.segment(tmpx, tmpy, x1, y1, line_width=5, line_color="gray",)
p1.segment(tmpx2,tmpy2,x3,y3,line_width=5,line_color = 'gray',)
p1.circle(x0, y0, size=12, fill_color="#0000FF", line_color="gray", line_width=3, )
p1.circle(x1, y1, size=12, fill_color= '#00FFFF', line_color="gray", line_width=3, )
p1.circle(x3_yes, y3_yes, size=12, fill_color= 'red', line_color="gray", line_width=3, )
p1.circle(x3_no, y3_no, size=12, fill_color= 'green', line_color="gray", line_width=3, )
p1.circle([60,60,60,60,60,60,60], [50,70,90,110,130,150,170], size=5, fill_color= 'black',)


#p1.xaxis.axis_label = "L"
#p1.xaxis.axis_label_text_color = "#aa6666"
#p1.xaxis.axis_label_standoff = 30
# p1.xaxis.axis_label_text_alpha = 0
# p1.xaxis.axis_label_text_font_size = '0pt'
#add text labels and legend
result = ['Stay']*12
result[1] = 'Leave';result[6] = 'Leave';result[11] = 'Leave'
p1.text([105]*12,list(np.array(y3)-10), result, text_font_size = '12pt', text_color='black')#,text_font_style='bold')
p1.quad(top=[500], bottom=[400], left=[150], right=[200], fill_alpha = 0, line_width = 4, color="#0099CC")
p1.circle([165],[470],fill_color = 'green', line_color = 'gray',size = 12,line_width=3,)
p1.circle([165],[430],fill_color = 'red', line_color = 'gray',size = 12,line_width=3,)
p1.text([170],[458], ['Stay'], text_font_size = '12pt', text_color='black', text_font_style='bold')
p1.text([170],[418], ['Leave'], text_font_size = '12pt', text_color='black', text_font_style='bold')

#add the judgement label on the graph
p1.text([-18],[-12], ['emotional burnout'], text_font_size = '10pt', text_color='#0000FF')
p1.text([28],[-34], ['<=23'], text_font_size = '10pt', text_color='#0000FF')
p1.text([28],[-65], ['>23'], text_font_size = '10pt', text_color='#0000FF')

p1.text([-18],[280], ['off work time'], text_font_size = '10pt', text_color='#0000FF')
p1.text([28],[268], ['<=12.5'], text_font_size = '10pt', text_color='#0000FF')
p1.text([28],[235], ['>12.5'], text_font_size = '10pt', text_color='#0000FF')


p1.text([-18],[440], ['quarter goal rate'], text_font_size = '10pt', text_color='#0000FF')
p1.text([28],[428], ['<=71'], text_font_size = '10pt', text_color='#0000FF')
p1.text([28],[395], ['>71'], text_font_size = '10pt', text_color='#0000FF')


p1.text([20],[470], ['emotional burnout'], text_font_size = '10pt', text_color='green')
p1.text([70],[475], ['<=23'], text_font_size = '10pt', text_color='green')
p1.text([70],[430], ['>23'], text_font_size = '10pt', text_color='green')
p1.text([20],[355], ['low achievement'], text_font_size = '10pt', text_color='green')
p1.text([70],[395], ['<=18'], text_font_size = '10pt', text_color='green')
p1.text([70],[350], ['>18'], text_font_size = '10pt', text_color='green')

p1.text([20],[310], ['outer pressure'], text_font_size = '10pt', text_color='green')
p1.text([70],[270], ['<=15'], text_font_size = '10pt', text_color='green')
p1.text([70],[312], ['>15'], text_font_size = '10pt', text_color='green')

p1.text([20],[195], ['subj efficiency'], text_font_size = '10pt', text_color='green')
p1.text([70],[232], ['<=4'], text_font_size = '10pt', text_color='green')
p1.text([70],[190], ['>4'], text_font_size = '10pt', text_color='green')

p1.text([20],[15], ['quarter goal rate'], text_font_size = '10pt', text_color='green')
p1.text([70],[-29], ['<=71'], text_font_size = '10pt', text_color='green')
p1.text([70],[15], ['>71'], text_font_size = '10pt', text_color='green')

p1.text([20],[-105], ['inner pressure'], text_font_size = '10pt', text_color='green')
p1.text([70],[-65], ['<=17'], text_font_size = '10pt', text_color='green')
p1.text([70],[-110], ['>17'], text_font_size = '10pt', text_color='green')

# p1.text([],[-34], ['<=23'], text_font_size = '10pt', text_color='#0000FF')
# p1.text([28],[-65], ['>23'], text_font_size = '10pt', text_color='#0000FF')
# p1.ygrid.grid_line_alpha = 0
# p1.xgrid.grid_line_alpha = 0
p1.yaxis.major_tick_line_color = None
p1.yaxis.minor_tick_line_color = None
p1.xaxis.major_tick_line_color = None
p1.xaxis.minor_tick_line_color = None
p1.xaxis.axis_label_text_alpha = 0
p1.xaxis.axis_label_text_font_size = '0pt'
p1.xaxis.axis_label_text_color = None
p1.xaxis.axis_label_standoff = 30
# p1.xaxis.major_tick_line_alpha = 0
# p1.yaxis.major_tick_line_alpha = 0
# factors = ["foo", "bar", "baz"]
# x = ["foo", "foo", "foo", "bar", "bar", "bar", "baz", "baz", "baz"]
# y = ["foo", "bar", "baz", "foo", "bar", "baz", "foo", "bar", "baz"]
# colors = [
#     "#0B486B", "#79BD9A", "#CFF09E",
#     "#79BD9A", "#0B486B", "#79BD9A",
#     "#CFF09E", "#79BD9A", "#0B486B"
# ]

# p2 = figure(title="Categorical Heatmap", tools="resize,hover,save",
#     x_range=factors, y_range=factors)

# p2.rect(x, y, color=colors, width=1, height=1)

# show(vplot(p1, p2))  # open a browser
show(p1)






