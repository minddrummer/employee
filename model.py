import pylab
pylab.ion()
import pandas as pd
import numpy as np
import scipy as sp
import matplotlib.pyplot as plt
import random
from sklearn.ensemble import RandomForestClassifier
from sklearn import preprocessing
from sklearn.preprocessing import Imputer
from sklearn import linear_model as lm
from sklearn.ensemble import AdaBoostClassifier as Ada
import mpld3

#(1264, 126)
df = pd.read_csv('data.csv')
X = df.drop('res', axis = 1).values
#print X.shape
y = df.res.values
#print y.shape
train_samples = 900
X_train = X[:train_samples]
X_test = X[train_samples:]
y_train = y[:train_samples]
y_test = y[train_samples:]

np.random.seed(0123)
##random forest classifier
rfc = RandomForestClassifier(n_estimators=100)
rfc.fit(X_train, y_train)
print (rfc.predict(X_train) == y_train).sum()/len(y_train)
print (rfc.predict(X_test) == y_test).sum()/len(y_test)

rfc.score(X_train, y_train)
rfc.predict_proba(X_train)
predict_prob = rfc.predict_proba(X_test)
imp = sorted(zip(df.drop('res', axis = 1).columns.values, rfc.feature_importances_), key= lambda x: x[1], reverse = True)

imp_var = [i[0] for i in imp[:10]][::-1]
imp_coef = [i[1] for i in imp[:10]][::-1]
pos = np.arange(10)+.5
fig = plt.figure(1)
plt.barh(pos,imp_coef, align='center')
plt.yticks(pos, imp_var)
plt.xlabel('Importance')
plt.title('The top 10 important variables for employee turnout')
plt.grid(True)
#plt.tight_layout()
fig.savefig('top10importance.png', bbox_inches='tight')
#plt.show()
plt.close()

##logistic regression
#should use the training mean and std to normalize  the test set; should also create dummy variables for the nominal variables
#by now, not doing these above

X_train_scaled = preprocessing.scale(X_train)
X_test_scaled = preprocessing.scale(X_test)
logistic = lm.LogisticRegression()
logistic.fit(X_train_scaled, y_train)
(logistic.predict(X_train_scaled) == y_train).sum()/len(y_train)
(logistic.predict(X_test_scaled) == y_test).sum()/len(y_test)
logistic.decision_function(X_test_scaled)
imp = sorted(zip(df.drop('res', axis = 1).columns.values, logistic.coef_.transpose()), key= lambda x: x[1], reverse = True)



##last we try the boosting tree model:
ada_tree = Ada()

ada_tree.fit(X_train, y_train)
print (ada_tree.predict(X_train) == y_train).sum()/len(y_train)
print (ada_tree.predict(X_test) == y_test).sum()/len(y_test)
#print ada_tree.feature_importances_

imp = sorted(zip(df.drop('res', axis = 1).columns.values, ada_tree.feature_importances_), key= lambda x: x[1], reverse = True)


imp_var = [i[0] for i in imp[:10]][::-1]
imp_coef = [i[1] for i in imp[:10]][::-1]
pos = np.arange(10)+.5
fig = plt.figure(1)
plt.barh(pos,imp_coef, align='center')
plt.yticks(pos, imp_var)
plt.xlabel('Importance')
plt.title('The top 10 important variables for employee turnout for Boosting Tree')
plt.grid(True)
#mpld3.show()
#plt.tight_layout()
fig.savefig('top10importance_boostingTree.png', bbox_inches='tight')
plt.close()