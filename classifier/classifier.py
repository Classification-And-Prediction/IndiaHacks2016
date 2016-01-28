################## LIBRARIES ###################
import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestClassifier

# from sklearn.svm import LinearSVC
# from sklearn.linear_model import LogisticRegression
# from sklearn.ensemble import GradientBoostingClassifier
# from sklearn.naive_bayes import *
# from sklearn.neighbors import *
# from sklearn.neural_network import MLPClassifier
# from sknn.mlp import Classifier, Layer
# import logging
# logging.basicConfig()

################ dataset load ###################
train_data_df = pd.read_csv('train_shuffle.csv', header=None)
test_data_df = pd.read_csv('test_shuffle.csv', header=None)
train_data_df = train_data_df.astype('float')
test_data_df = test_data_df.astype('float')
train_data_df = train_data_df.drop(train_data_df.columns[8], axis=1)
test_data_df = test_data_df.drop(test_data_df.columns[7], axis=1)
train_data_df.columns = ["skillcount","user_solved_count", "attempts", "level", "accuracy", "prob_solved_count", "error_count", "output"]
test_data_df.columns = ["skillcount", "user_solved_count", "attempts", "level", "accuracy", "prob_solved_count", "error_count"]

############## Prediction model #################
my_model = RandomForestClassifier(max_depth=6, class_weight={1: 5})						#best
# my_model = LogisticRegression(penalty = 'l1',C=0.1, class_weight={1: 5})
# my_model = LinearSVC(penalty = 'l1',dual=False,C=0.1, class_weight={1: 5})

# my_model = MLPClassifier(alpha=0.1, activation="logistic")
# my_model = GradientBoostingClassifier(max_depth=6, learning_rate=0.1, n_estimators=10,loss="exponential", verbose=1)
# my_model = Classifier(
#     layers=[
#         # Layer("Linear", units=2)
#         # Layer("Gaussian"),
#         Layer("Softmax")
#         ],
#     learning_rate=0.001,
#     n_iter=25)


my_model = my_model.fit(X=train_data_df[[0,1,2,3,4,5,6]], y=train_data_df.output)
pred = my_model.predict(test_data_df)

################ save Output ####################
f = open("output.csv","w")
f.write("Id,solved_status"+"\n")
for i in range(0,len(pred)):
	f.write(str(i)+","+str(int(pred[i]))+"\n")