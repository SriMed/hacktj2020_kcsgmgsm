import argparse
import pickle
from sklearn import tree
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor

X,y = pickle.load(open('data.p', 'rb'))

X_fit, X_eval, y_fit, y_eval = train_test_split(X, y, test_size=0.30, random_state=2)

features = ['Predicted Precipitation', 'Total Miles Plowed']

dt_file = open('output.txt', 'w')

#DTrees
dtree = tree.DecisionTreeRegressor().fit(X_fit, y_fit)
accuracy = dtree.score(X_eval, y_eval)
dt_file.write(f'Single Dtree: {accuracy}\n')

for feature, imp in zip(features, dtree.feature_importances_):
    dt_file.write("\tFeature %s: %s\n" % (feature, imp))

#Random Forest Trees
rf_dtree = RandomForestRegressor(n_estimators=8).fit(X_fit,y_fit)
accuracy = rf_dtree.score(X_eval,y_eval)
dt_file.write(f'Random Forest Dtrees: {accuracy}\n')

#Extremely Randomized Trees
extra_rf_dtree = RandomForestRegressor(n_estimators=8).fit(X_fit,y_fit)
accuracy = rf_dtree.score(X_eval,y_eval)
dt_file.write(f'Extremely Randomized Dtrees: {accuracy}\n')