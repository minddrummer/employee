'''
this script simulate the data for all the variabls needed
700 data points, 500 for training, 100 for validation,and 100 for testing
'''
import pylab
pylab.ion()
import pandas as pd
import numpy as np
import scipy as sp
import sklearn as sk
import matplotlib.pyplot as plt
import random

np.random.seed(0077)
#in the following dict, 99 means one time, 1 means one month, 6 means half year, and 12 means one year
col_dict = {
'gender':['demo' , 99],
'age':['demo' ,99 ],
'edu':[ 'demo', 99],
'marital':[ 'demo', 99],
'children':['demo' , 99],
'num_family':[ 'demo', 99],
'city_size':['demo' , 99],
'sep_spouse':[ 'demo', 99],
'sep_child':[ 'demo', 99],
'sig_event':['mag' , 99],
'month':[ 'mag', 99],
'location':[ 'mag', 99],
'change_loc_num':['mag' , 12],
'work_years':[ 'mag', 12],
'position':['mag' , 12],
'dept':['mag' , 12],
'change_job_num':['mag' , 99],
'leave_num_cur_company':[ 'mag', 99],
'application_num_leave_cur_company':['mag' , 12],
'ave_leave_persons_cur_dept':[ 'mag', 12],
'change_boss':['mag' , 1],
'off_work_num':[ 'mag', 1],
'off_work_time_gap':[ 'mag', 1],
'off_work_time':['mag' , 1],
'late_work_num':['mag' , 1],
'late_work_time':['mag' , 1],
'salary':['mag' , 1],
'bonus':[ 'mag', 1],
'equity':['mag' , 12],
'equity_cash':[ 'mag', 12],
'promotion_num':[ 'mag', 1],
'raise_num':['mag' , 1],
'raise_percent':[ 'mag', 1],
'pos_change_num':['mag' , 1],
'degrade_num':['mag' , 1],
'de_salary_num':[ 'mag', 1],
'de_salary_precent':[ 'mag', 1],
'punish_num':['mag' , 1],
'job_intensity':[ 'mag', 1],
'vacation_days':['mag' , 12],
'training_num':['mag' , 12],
'training_time':[ 'mag', 12],
'industry_leave_rate':['mag' , 12],
'pos_leave_rate':[ 'mag', 12],
'subj_efficiency':[ 'wok', 1],
'obj_efficiency':[ 'wok', 1],
'job_dept':['wok' , 1],
'job_type':['wok' , 1],
'overall_score':['wok' , 1],
'goal_individual_rate_quarter':['wok' , 3],
'goal_company_rate_quarter':[ 'wok', 3],
'regional_sale_percent':[ 'wok', 1],
'type_sale_percent':['wok' , 1],
'regional_sale_comparison_rate':['wok' , 1],
'ability_tendency':['psy' , 12],
'personality':['psy' , 12],
'motivation':['psy' , 12],
'individual_value_company_culture':['psy' , 12],
'job_satistication':['psy' , 6],
'emotional_burnout':[ 'psy', 6],
'job_avoidance':[ 'psy', 6],
'low_achievement':['psy' , 6],
'outer_pressure':['psy' , 6],
'inner_pressure':['psy' , 6],
'depression_index':['psy' , 6],
'psychatric_index':['psy' , 6],
'pressure_vul':[ 'psy', 6],
'emotion_stability':[ 'psy', 6],
'subhealth_state':['psy' , 6],
'psy_stress_event':[ 'psy', 6],
'physical_index':['psy' , 6],
'leave': ['result', 99]
}


##value generating functions::
def gene_normal_with_limit(mean, std, size, limit, rounding = 0):
	i = 1
	res = []
	while i <= size:
		tmp = round(np.random.normal(mean, std), rounding)
		if tmp>= limit[0] and tmp <= limit[1]:
			res.append(tmp)
			i += 1
	return np.array(res)		

def gene_multinom(size, ratio_lst, start_value=0, printing = False):
	'''ratio_lst is the percent for each label.
	size is the total users; and start_value is the starting label
	'''
	label_counts = np.random.multinomial(size, ratio_lst)
	label_dict = dict(zip(range(start_value, len(ratio_lst)+start_value), label_counts))
	if printing:
		print label_dict
	tmp = []
	for key in label_dict:
		tmp = tmp + [int(key)]*label_dict[key]
	#then return the shuffled list of the labels		
	return random.sample(tmp, len(tmp))

def gene_multinom_one_label(ratio_lst, start_value, printing = False):
	'''
	this function generate only one label among all possible labels given the probability list
	ratio_lst is the percent for each label.
	and start_value is the starting label
	'''
	test = np.random.random()
	#print test
	total = 0
	ratio_cum = []
	for item in ratio_lst:
		total = total + item 
		ratio_cum.append(total)
	#print ratio_cum
	for i in range(len(ratio_cum)):
		if ratio_cum[i] >= test:
			break
	return i + start_value


###parameter settings:
N = 1264
np.random.seed(777)


##--for 99 one time variable simualtion
col99 = [key for key in col_dict if col_dict[key][1] == 99]
# [--'marital',
#  --'edu',
#  --'sep_spouse',
#  --'sep_child',
#  --'children',
#  --'location',
#  --'city_size',
#  --'sig_event',
#  --'month',
#  --'num_family',
#  --'gender',
#  --'age',
#  --'change_job_num',
#  --'leave_num_cur_company']


df99 = pd.DataFrame()
#df99.columns = col99
df99.loc[:,'gender'] = np.random.randint(0,2,N)
df99.loc[:,'age'] = gene_normal_with_limit(34, 5, N, [20, 65], rounding = 0)
df99.loc[:,'edu'] = gene_multinom(N, [0.05,0.5,0.3,0.1,0.05])
df99.loc[:,'marital'] = gene_multinom(N, [0.45,0.4,0.05,0.05,0.05])
df99.loc[:,'children'] = gene_multinom(N, [0.5,0.4,0.09,0.01])
df99.loc[:,'num_family'] = gene_multinom(N, [0.3,0.2,0.4,0.09,0.01], start_value = 1)
df99.loc[:,'city_size'] = gene_multinom(N, [0.4,0.3,0.3], start_value = 1)

##the following two variables are *
def sep_spouse(x, ratio_lst, start_value):
	if x['num_family'] > 1:
		return gene_multinom_one_label(ratio_lst, start_value, printing = False)
	else:
		return 0	
df99.loc[:,'sep_spouse'] = df99.apply(sep_spouse, axis = 1, args= (([0.93,0.07]),0))

def sep_child(x):
	'''it can be living with spouse, but sep with child;
	or it can be both sep with spouse and sep with child
	'''
	#first have to have child
	#then if sep_spouse, then the pro is high:
	#if not sep_spouse, then the pro is low:
	if x['children'] >= 1:
		if x['sep_spouse'] == 1:#if NOT living with spouse, 0 means not sep with child, pro is high
			return gene_multinom_one_label([0.5, 0.5],0, printing = False)
		else: #if living with spouse, 0 means not sep with child, pro is low
			return gene_multinom_one_label([0.95, 0.05],0, printing = False)
	else:
		return 0
df99.loc[:,'sep_child'] = df99.apply(sep_child, axis = 1)
df99.loc[:, 'sig_event'] = 0
df99.loc[:, 'month'] = 6
df99.loc[:, 'location'] = 1

#change_job_num  leave_num_cur_company these two factors are *
df99.loc[:, 'change_job_num'] = gene_multinom(N, [0.8,0.1,0.04,0.03,0.02,0.01], start_value=0, printing = False)
#leave_num_cur_company
df99.loc[:, 'leave_num_cur_company'] = gene_multinom(N, [0.96,0.03,0.01], start_value=0, printing = False)


#although they are tested 12month for once, for now, we just have one record for each employee
col12 = [key for key in col_dict if col_dict[key][1] == 12]
# [--'motivation',
#  --'change_loc_num',
#  --'vacation_days',
#  --'pos_leave_rate',
#  --'ave_leave_persons_cur_dept',
#  --'equity_cash',
#  --'work_years',
#  --'equity',
#  --'ability_tendency',
#  --'individual_value_company_culture',
#  --'industry_leave_rate',
#  --'training_time',
#  --'application_num_leave_cur_company',
#  --'dept',
#  --'training_num',
#  --'position',
#  --'personality']

df12 = pd.DataFrame()
#most em for 0, few for 1, very few for 2, very very few for 3
df12.loc[:,'change_loc_num'] = gene_multinom(N, [0.92,0.05,0.02,0.01], start_value=0, printing = False)
#work_years follows normal distribution, with most in the center of 10, with a std of 5
df12.loc[:,'work_years'] = gene_normal_with_limit(10, 5, N, [0.2, 30], rounding = 1)
#different number represents for different postions
df12.loc[:,'position'] = gene_multinom(N, [0.1]*10, start_value=0, printing = False)
#different dept represents for different dept
df12.loc[:,'dept'] = gene_multinom(N, [0.2]*5, start_value=0, printing = False)
#most are 0; very few are 1
df12.loc[:,'application_num_leave_cur_company'] = gene_multinom(N, [0.992,0.008], start_value=0, printing = False)
#ave_leave_persons_cur_dept for each dept?
df12.loc[:,'ave_leave_persons_cur_dept'] = df12.loc[:,'dept'].map({0:10,1:4,2:9,3:7,4:5})
#equity is a normal distribution
df12.loc[:,'equity'] = gene_normal_with_limit(800, 500, N, [0, 3000], rounding = 0)
#equity_cash
df12.loc[:,'equity_cash'] = df12.loc[:,'equity'].apply(lambda x: x*0.12)
#vacation_days2.52.
#training_num
df12.loc[:,'training_num'] = df12.loc[:,'dept'].map({0:5,1:4,2:4,3:6,4:2})
#training_time
df12.loc[:,'training_time'] = df12.loc[:,'training_num'].apply(lambda x: x*7)
#industry_leave_rate
df12.loc[:,'industry_leave_rate'] = 0.08
#pos_leave_rate
df12.loc[:,'pos_leave_rate'] = df12.loc[:,'position'].map(dict(zip(range(10), \
	gene_normal_with_limit(0.1, 0.05, len(range(10)), [0.0001, 0.2], rounding = 2))))
#ability_tendency:similar to IQ
df12.loc[:,'ability_tendency'] = gene_normal_with_limit(100, 10, N, [70, 150], rounding = 0)
#individual_value_company_culture
df12.loc[:,'individual_value_company_culture'] = gene_normal_with_limit(50, 5, N, [0.1, 150], rounding = 1)
#personality
df12.loc[:,'personality'] = gene_normal_with_limit(100, 10, N, [60, 150], rounding = 0)
#motivation
df12.loc[:,'motivation'] = gene_normal_with_limit(50, 10, N, [0.1, 100], rounding = 0)


#`````````````combine df12 and df99, and add the results;make the results corresponding with the variables in df12 and df99
#for further analysis, it is better to simulate given the results
df = pd.concat([df12,df99], axis = 1, join = 'outer')
df.loc[:,'res'] = 0
#the 4 variables in 12 and 99 matter are:
# sep_spouse
# sep_child
# change_job_num
# ave_leave_persons_cur_dept
def gen_res(df0):
	np.random.seed(786)
	s1 =df0.apply(lambda x: gene_multinom_one_label([0.5,0.5], 0) if x.sep_spouse == 1 else 0, axis =1)
	s2 =df0.apply(lambda x: gene_multinom_one_label([0.5,0.5], 0) if x.sep_child == 1 else 0, axis =1)
	s3 =df0.apply(lambda x: gene_multinom_one_label([0.5,0.5], 0) if x.change_job_num >= 3 else 0, axis =1)
	s4 =df0.apply(lambda x: gene_multinom_one_label([0.9,0.1], 0) if x.ave_leave_persons_cur_dept >= 9 else 0, axis =1)
	s = s1 + s2 + s3 + s4
	res = s.apply(lambda x: 1 if x > 0 else 0)
	return res
df.loc[:,'res'] = gen_res(df)

##simulate result for 6-month variable, we should have 2 values for each employee
#but for simplicity, we only have 3 variables for each field: the mean, the last, and the changing rate
# 'job_satistication':['psy' , 6], ******
# 'emotional_burnout':[ 'psy', 6],******
# 'job_avoidance':[ 'psy', 6],******
# 'low_achievement':['psy' , 6],******
# 'outer_pressure':['psy' , 6],******
# 'inner_pressure':['psy' , 6],******
# 'depression_index':['psy' , 6],
# 'psychatric_index':['psy' , 6],
# 'pressure_vul':[ 'psy', 6],
# 'emotion_stability':[ 'psy', 6],
# 'subhealth_state':['psy' , 6],
# 'psy_stress_event':[ 'psy', 6],
# 'physical_index':['psy' , 6],

def gen_6_month_data_non_important(mean, std, size, limit, field, rounding = 0):
	'''this function automatically works on df, and add 3 fields to it'''
	s1 = gene_normal_with_limit(mean, std, N, limit, rounding = rounding)
	s2 = gene_normal_with_limit(mean, std, N, limit, rounding = rounding)
	s_rate = s2 - s1
	s_aver = (s2+s1)/2.0
	df.loc[:, field+'_last'] = s2
	df.loc[:, field+'_aver'] = s_aver
	df.loc[:, field+'_rate'] = s_rate



# 'depression_index':['psy' , 6], :: 8-32
gen_6_month_data_non_important(20, 4, N, [8,32],'depression_index', rounding = 0)
# 'psychatric_index':['psy' , 6],
gen_6_month_data_non_important(30, 10, N, [10,50],'psychatric_index', rounding = 0)
# 'pressure_vul':[ 'psy', 6],
gen_6_month_data_non_important(20, 5, N, [8,40],'pressure_vul', rounding = 0)
# 'emotion_stability':[ 'psy', 6],
gen_6_month_data_non_important(40, 15, N, [13,65],'emotion_stability', rounding = 0)
# 'subhealth_state':['psy' , 6],
gen_6_month_data_non_important(50, 25, N, [0,100],'subhealth_state', rounding = 0)
# 'psy_stress_event':[ 'psy', 6],
gen_6_month_data_non_important(700, 200, N, [0,1440],'psy_stress_event', rounding = 0)
# 'physical_index':['psy' , 6],
gen_6_month_data_non_important(100, 15, N, [50,200],'physical_index', rounding = 0)


# 'job_satistication':['psy' , 6], ******
# 'emotional_burnout':[ 'psy', 6],******
# 'job_avoidance':[ 'psy', 6],******
# 'low_achievement':['psy' , 6],******
# 'outer_pressure':['psy' , 6],******
# 'inner_pressure':['psy' , 6],******
	


def gen_6_month_data_important(limit, cut, upper, field, rounding = 0):
	'''this function automatically works on df, and add 3 fields to it;
	upper means the abnormal is in the upper area; 
	cut the bound for decding where is the abnormal area
	limit is the range of the values for that specific field 
	'''
	if upper:
		s_last = df.res.apply(lambda x: gene_normal_with_limit((limit[1]+cut)/2.0, (limit[1]-cut)/2.0, 1, [cut, limit[1]], rounding = rounding)[0] if x == 1 \
			else gene_normal_with_limit((limit[0]+cut)/2.0, (cut-limit[0])/2.0, 1, [limit[0], cut], rounding = rounding)[0])
		s_rate = df.res.apply(lambda x: gene_normal_with_limit((limit[1]-limit[0])/4.0, (limit[1]-limit[0])/5.0, 1, [1, (limit[1]-limit[0])], rounding = rounding)[0] if x == 1 \
			else gene_normal_with_limit(0, (limit[1]-limit[0])/5.0, 1, [-(limit[1]-limit[0])/2.0, (limit[1]-limit[0])/2.0], rounding = rounding)[0])
		s_aver = s_last - (s_rate/2.0).astype(int)	
	else:
		s_last = df.res.apply(lambda x: gene_normal_with_limit((limit[0]+cut)/2.0, (cut-limit[0])/2.0, 1, [limit[0], cut], rounding = rounding)[0] if x == 1 \
			else gene_normal_with_limit((limit[1]+cut)/2.0, (limit[1]-cut)/2.0, 1, [cut, limit[1]], rounding = rounding)[0])
		s_rate = df.res.apply(lambda x: gene_normal_with_limit(-(limit[1]-limit[0])/4.0, (limit[1]-limit[0])/5.0, 1, [-(limit[1]-limit[0]), -1], rounding = rounding)[0] if x == 1 \
			else gene_normal_with_limit(0, (limit[1]-limit[0])/5.0, 1, [-(limit[1]-limit[0])/2.0, (limit[1]-limit[0])/2.0], rounding = rounding)[0])
		s_aver = s_last - (s_rate/2.0).astype(int)	
	df.loc[:, field+'_last'] = s_last
	df.loc[:, field+'_aver'] = s_aver
	df.loc[:, field+'_rate'] = s_rate

# 'job_satistication':['psy' , 6], ******
gen_6_month_data_important([1,10], 3, False, 'job_satistication',  rounding = 0)
#test the simulated result
# sk =df.loc[:, ['res','job_satistication_aver', 'job_satistication_rate', 'job_satistication_last']]
# sk.groupby('res').apply(np.mean)

# 'emotional_burnout':[ 'psy', 6],******
gen_6_month_data_important([5,35], 23, True, 'emotional_burnout',  rounding = 0)
# sk =df.loc[:, ['res','emotional_burnout_aver', 'emotional_burnout_rate', 'emotional_burnout_last']]
# print sk.groupby('res').apply(np.mean)

# 'job_avoidance':[ 'psy', 6],******
gen_6_month_data_important([5,35], 18, True, 'job_avoidance',  rounding = 0)
# 'low_achievement':['psy' , 6],******
gen_6_month_data_important([5,35], 18, True, 'low_achievement',  rounding = 0)
# 'outer_pressure':['psy' , 6],******
gen_6_month_data_important([0,21], 15, True, 'outer_pressure',  rounding = 0)
# 'inner_pressure':['psy' , 6],******
gen_6_month_data_important([0,24], 17, True, 'inner_pressure',  rounding = 0)


##````````simulate df3 below
##approximately use the function for 6month features
# 'goal_individual_rate_quarter':['wok' , 3],******
gen_6_month_data_important([40,140], 80, False, 'goal_individual_rate_quarter',  rounding = 0)
# 'goal_company_rate_quarter':[ 'wok', 3]******
df.loc[:,'goal_company_rate_quarter'] = 107



##```````````simulate on df1 below
filter(lambda x: col_dict[x][1]==1, col_dict.keys())

 # 'pos_change_num',******
 # 'raise_percent',******
 # 'off_work_num',******
 # 'off_work_time_gap',******
 # 'off_work_time',******
 # 'punish_num',******
 # 'degrade_num',******
 # 'subj_efficiency',******
 # 'raise_num',******
 # 'change_boss',******
 # 'job_intensity',******
 # 'promotion_num',******
 # 'de_salary_num',******
 # 'obj_efficiency',******
 # 'de_salary_precent']******


def gen_every_month_data_important_continuous(limit, cut, upper, field, rounding = 0):
	'''this function automatically works on df, and add 3 fields to it;
	upper means the abnormal is in the upper area; 
	cut the bound for decding where is the abnormal area
	limit is the range of the values for that specific field 
	'''
	if upper: # upper means in the upper-zone, it is more likely to leave the current job
		s_last = df.res.apply(lambda x: gene_normal_with_limit((limit[1]+cut)/2.0, (limit[1]-cut)/2.0, 1, [cut, limit[1]], rounding = rounding)[0] if x == 1 \
			else gene_normal_with_limit((limit[0]+cut)/2.0, (cut-limit[0])/2.0, 1, [limit[0], cut], rounding = rounding)[0])
		s_aver = df.res.apply(lambda x: gene_normal_with_limit((limit[0]+limit[1])/2.0, (limit[1]-limit[0])/4.0, 1, [limit[0], limit[1]], rounding = rounding)[0] if x == 1 \
			else gene_normal_with_limit((limit[0]+cut)/2.0, (cut-limit[0])/2.0, 1, [limit[0], cut], rounding = rounding)[0])
		s_rate = (s_last - s_aver)/6.0
	else:
		s_last = df.res.apply(lambda x: gene_normal_with_limit((limit[0]+cut)/2.0, (cut-limit[0])/2.0, 1, [limit[0], cut], rounding = rounding)[0] if x == 1 \
			else gene_normal_with_limit((limit[1]+cut)/2.0, (limit[1]-cut)/2.0, 1, [cut, limit[1]], rounding = rounding)[0])
		s_aver = df.res.apply(lambda x: gene_normal_with_limit((limit[0]+limit[1])/2.0, (limit[1]-limit[0])/4.0, 1, [limit[0], limit[1]], rounding = rounding)[0] if x == 1 \
			else gene_normal_with_limit((limit[1]+cut)/2.0, (limit[1]-cut)/2.0, 1, [cut, limit[1]], rounding = rounding)[0])
		s_rate = (s_last - s_aver)/6.0
	df.loc[:, field+'_last'] = s_last
	df.loc[:, field+'_aver'] = s_aver
	df.loc[:, field+'_rate'] = s_rate



 # 'pos_change_num',******
gen_every_month_data_important_continuous([0,5], 4, True, 'pos_change_num', rounding = 0)
df.loc[:, 'pos_change_num_last'] = df.pos_change_num_last.apply(lambda x: 0 if x<=4 else x-4)
df.loc[:, 'pos_change_num_aver'] = df.pos_change_num_aver.apply(lambda x: 0 if x<=4 else x-4)
df.loc[:, 'pos_change_num_rate'] = (df.pos_change_num_last - df.pos_change_num_aver)/6.0
 # 'raise_percent',******
gen_every_month_data_important_continuous([0,50], 10, False, 'raise_percent', rounding = 0)
df.loc[:, 'raise_percent_last'] = df.raise_percent_last.apply(lambda x: 0 if x<=40 else x-40)
df.loc[:, 'raise_percent_aver'] = df.raise_percent_aver.apply(lambda x: 0 if x<=40 else x-40)
df.loc[:, 'raise_percent_rate'] = (df.raise_percent_last - df.raise_percent_aver)/6.0
 # 'off_work_num',******
gen_every_month_data_important_continuous([0,25], 8, True, 'off_work_num', rounding = 0)
df.loc[:, 'off_work_num_last'] = df.off_work_num_last.apply(lambda x: 0 if x<=12 else x-12)
df.loc[:, 'off_work_num_aver'] = df.off_work_num_aver.apply(lambda x: 0 if x<=12 else x-12)
df.loc[:, 'off_work_num_rate'] = (df.off_work_num_last - df.off_work_num_aver)/6.0
 # 'off_work_time_gap',******
gen_every_month_data_important_continuous([0,29], 3, False, 'off_work_time_gap', rounding = 0)
df.loc[:, 'off_work_time_gap_last'] = df.off_work_time_gap_last.apply(lambda x: x if x<=3 else 0)
df.loc[:, 'off_work_time_gap_aver'] = df.off_work_time_gap_aver.apply(lambda x: x if x<=3 else 0)
df.loc[:, 'off_work_time_gap_rate'] = (df.off_work_time_gap_last - df.off_work_time_gap_aver)/6.0
 # 'off_work_time',******
gen_every_month_data_important_continuous([0,60], 10, True, 'off_work_time', rounding = 0)
# 'punish_num',******
df.loc[:,'punish_num'] = df.res.apply(lambda x: gene_multinom_one_label([0.97,0.03], 0) if x == 1 else 0)
# 'degrade_num',******
df.loc[:,'degrade_num'] = df.res.apply(lambda x: gene_multinom_one_label([0.98,0.02], 0) if x == 1 else 0)
# 'subj_efficiency',******
gen_every_month_data_important_continuous([1,10], 4, False, 'subj_efficiency', rounding = 0)
# 'raise_num',******
df.loc[:,'raise_num'] = df.res.apply(lambda x: gene_multinom_one_label([0.5,0.5], 0) if x == 1 else 1)
# 'change_boss',******
df.loc[:,'change_boss'] = df.res.apply(lambda x: gene_multinom_one_label([0.95,0.05], 0) if x == 1 else 0)
# 'job_intensity',******
gen_every_month_data_important_continuous([1,10], 7, True, 'job_intensity', rounding = 0)
# 'promotion_num',****** 0 means no promotion, and 1 means 1time promotion
df.loc[:,'promotion_num'] = df.res.apply(lambda x: gene_multinom_one_label([0.95,0.05], 0) if x == 1 else  gene_multinom_one_label([0.7,0.3], 0))
# 'de_salary_num',******
df.loc[:,'de_salary_num'] = df.res.apply(lambda x: gene_multinom_one_label([0.96,0.04], 0) if x == 1 else  0)
# 'obj_efficiency',******
gen_every_month_data_important_continuous([1,10], 3, False, 'obj_efficiency', rounding = 0)
# 'de_salary_percent']******
df.loc[:,'de_salary_percent'] = df.de_salary_num.apply(lambda x: gene_multinom_one_label([0.25,0.25,0.25, 0.25], 8) if x == 1 else 0)




def gen_every_month_data_NON_important_continuous(limit, field, rounding = 0):
	'''this function automatically works on df, and add 3 fields to it;
	limit is the range of the values for that specific field 
	'''
	s_last = df.res.apply(lambda x: gene_normal_with_limit((limit[1]+limit[0])/2.0, (limit[1]-limit[0])/4.0, 1, [limit[0], limit[1]], rounding = rounding)[0])
	s_aver = df.res.apply(lambda x: gene_normal_with_limit((limit[1]+limit[0])/2.0, (limit[1]-limit[0])/4.0, 1, [limit[0], limit[1]], rounding = rounding)[0])
	s_rate = (s_last - s_aver)/6.0
	df.loc[:, field+'_last'] = s_last
	df.loc[:, field+'_aver'] = s_aver
	df.loc[:, field+'_rate'] = s_rate


# 'type_sale_percent',
df.loc[:,'type_sale_percent'] = df.loc[:,'dept'].map({0:0.12, 1:0.22, 2:0.17, 3:0.08, 4:0.41})
# 'late_work_time',
gen_every_month_data_NON_important_continuous([0,8], 'late_work_time', rounding = 1)
#  'late_work_num',
gen_every_month_data_NON_important_continuous([0,10], 'late_work_num', rounding = 0)
# 'salary',
gen_every_month_data_NON_important_continuous([3400,30000], 'salary', rounding = 0)
# 'bonus',
gen_every_month_data_NON_important_continuous([2000,20000], 'salary', rounding = 0)
# 'regional_sale_comparison_rate',
gen_every_month_data_NON_important_continuous([0,100], 'regional_sale_comparison_rate', rounding = 0)
# 'overall_score',
gen_every_month_data_NON_important_continuous([40,100], 'overall_score', rounding = 0)
#  'regional_sale_percent',
gen_every_month_data_NON_important_continuous([0,100], 'regional_sale_percent', rounding = 0)
# ['job_dept',
df.loc[:, 'job_dept'] = gene_multinom(N, [0.2,0.3,0.1,0.3,0.1], start_value=0, printing = False)
# 'job_type',
df.loc[:, 'job_type'] = gene_multinom(N, [0.25,0.45,0.3], start_value=0, printing = False)

df.to_csv('data.csv', index = False)


