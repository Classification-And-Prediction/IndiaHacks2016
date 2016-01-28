################## LIBRARIES ###################
import pandas as pd
import numpy as np
import re, nltk
from nltk.stem import WordNetLemmatizer      
from sklearn.feature_extraction.text import *
import xgboost as xgb

################ dataset load ###################
train_data_df = pd.read_csv('train_shuffle.csv', header = None)
test_data_df = pd.read_csv('test_shuffle.csv', header = None)

train_data_df = train_data_df.astype('float')
test_data_df = test_data_df.astype('float')

train_data_df = train_data_df.drop(train_data_df.columns[8], axis=1)
test_data_df = test_data_df.drop(test_data_df.columns[7], axis=1)

train_data_df.columns = ["skillcount","user_solved_count", "attempts", "level", "accuracy", "prob_solved_count", "error_count", "output"]
test_data_df.columns = ["skillcount", "user_solved_count", "attempts", "level", "accuracy", "prob_solved_count", "error_count"]

xg_train = xgb.DMatrix(train_data_df[[0,1,2,3,4,5,6]], label = train_data_df.output)
xg_test = xgb.DMatrix(test_data_df)

############## Prediction model #################
param = {}
param['objective'] = 'binary:logistic'
param['eta'] = 0.1
param['max_delta_step'] = 1
param['max_depth'] = 20		#20
# param['num_class'] = 2
# param['lambda']=0.8
param['subsample'] = 0.85
param['colsample_bytree'] = 0.5
param['gamma'] = 10
param['min_child_weight'] = 6
num_round = 2000					#2000

# cv = xgb.cv(param,xg_train,num_boost_round=500,nfold=5,maximize=False,early_stopping_rounds=40,show_progress=True)

# print cv

gbm = xgb.train(param,xg_train,num_round)
test_pred = gbm.predict(xg_test)

################ save Output ####################
temp = 0
f = open("output_xgb_2000.csv","w")
f.write("Id,solved_status"+"\n")
for i in test_pred:
	j = float(i)
	if j>0:
		f.write(str(temp)+",1\n")
	else:
		f.write(str(temp)+",0\n")
	temp = temp+1