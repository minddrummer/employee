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
	return res		

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
N = 700
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
df99.loc[:, 'sig_event'] = np.NaN
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
#vacation_days
df12.loc[:,'vacation_days'] = gene_normal_with_limit(10, 4, N, [0.2, 30], rounding = 0)
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




