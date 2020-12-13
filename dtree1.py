import argparse
import pickle
from sklearn import tree
from sklearn.model_selection import train_test_split


X,y = pickle.load(open('data.p', 'rb'))

X_fit, X_eval, y_fit, y_eval = train_test_split(X, y, test_size=0.30, random_state=2)

clf = tree.DecisionTreeRegressor()
clf = clf.fit(X_fit, y_fit)

accuracy = clf.score(X_eval, y_eval)

print(accuracy)