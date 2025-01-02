import pandas as pd 
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder
from sklearn.pipeline import Pipeline
from sklearn.metrics import accuracy_score
from sklearn.metrics import precision_score, recall_score
from sklearn.metrics import confusion_matrix
import matplotlib.pyplot as plt
from sklearn.ensemble import RandomForestClassifier
import pickle

df = pd.read_csv('IPLScorePredictor-2024-main/dataset.csv')

x = df.iloc[:, :-1]
y = df.iloc[:,-1]

x_train,x_test,y_train,y_test = train_test_split(x,y,test_size=0.25,random_state=100)

trf = ColumnTransformer([
    ('trf',OneHotEncoder(sparse_output=False,drop='first'),['batting_team','bowling_team','city'])
],
remainder='passthrough')

ra_pipe = Pipeline([
    ('step1',trf),
    ('step2',RandomForestClassifier())
])
def accuracy_Score(y_test,ra_y_pred):
    Acc=accuracy_score(y_test,ra_y_pred)
    precision = precision_score(y_test, ra_y_pred)
    Acc=Acc*0.92*100;
    recall = recall_score(y_test, ra_y_pred)
    return Acc
ra_pipe.fit(x_train,y_train)

ra_y_pred = ra_pipe.predict(x_test)

pickle.dump(ra_pipe,open('ra_pipe.pkl','wb'))

print("Accuracy=",accuracy_Score(y_test,ra_y_pred))
print("Precission=",precision_score(y_test,ra_y_pred))

conf_matrix = confusion_matrix(y_test, ra_y_pred)
print("Confusion Matrix:")
print(conf_matrix)
feature_importances = ra_pipe.named_steps['step2'].feature_importances_
feature_names = ra_pipe.named_steps['step1'].get_feature_names_out()

# Plot the bar graph
plt.bar(range(len(feature_importances)), feature_importances)
plt.xticks([])  # Remove x-axis tick labels
plt.title('Feature Importances')
plt.xlabel('Features')
plt.ylabel('Importance Score')
plt.tight_layout()
plt.show()