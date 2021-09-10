
from sklearn import preprocessing
import joblib


import numpy as np
import pandas as pd

df_train = pd.read_csv('dataset/Training.csv', delimiter=',')
df_test = pd.read_csv('dataset/Testing.csv', delimiter=',')
vocab = df_train.columns.tolist()[:-1]

label = preprocessing.LabelEncoder()
label.fit(pd.concat([df_train['prognosis'], df_test['prognosis']]))
labels = label.fit_transform(df_train['prognosis'])

le_name_mapping = dict(zip(label.classes_, label.transform(label.classes_)))


# model = joblib.load('models/model.pkl')

# model_cardio = joblib.load('cardio.sav')

model_cardio = joblib.load('heart_disease_prediction_using_random_forest_classifier_model.sav')

diabetes_model = joblib.load('models/diabetes_prediction_using_random_forest_classifier_model.sav')

thyroid_model = joblib.load('models/thyroid_prediction_using_navie_bayes_classifer_model.sav')

# model_kidney = joblib.load('models/kidney.sav')
# def predictor(final_symptoms):
#   y_test = np.zeros(132)
#   for final_symptom in final_symptoms:
#       y_test[vocab.index(final_symptom)] = 1
#
#   y_test_in = pd.DataFrame(y_test, vocab).T
#   #y_pred = model.predict(y_test_in)
#
#   ######
#   p = model.predict_log_proba(y_test_in)
#   n = 5 #Top n results
#   top_n = np.argsort(p)[:,:-n-1:-1] # Output Labels
#   y_pred = np.sort(p)[:,:-n-1:-1]
#   ######
#   diseases = []
#   for disease, code in le_name_mapping.items():
#     for top in top_n[0]:
#       if code == top:
#         diseases.append(disease)
#
#   return diseases

def cardio_predict(features):

  vocab = ['age', 'sex', 'cp', 'trestbps', 'chol', 'fbs', 'restecg', 'thalach', 'exang', 'oldpeak', 'slope', 'ca', 'thal']
  y_test_in = pd.DataFrame(features, vocab)
  X_eval = y_test_in.T
  
  y_eval = model_cardio.predict(X_eval)
  return y_eval


def diabetes_predict(features):
  vocab = ['age', 'gender', 'Polyuria', 'Polydipsia', 'sudden_weight_loss', 'weakness', 'Polyphagia', 'Genital_thrush', 'visual_blurring', 'Itching', 'Irritability', 'delayed_healing',
           'partial_paresis', 'muscle_stiffness', 'Alopecia', 'Obesity']
  y_test_in = pd.DataFrame(features, vocab)
  X_eval = y_test_in.T

  y_eval = diabetes_model.predict(X_eval)
  return y_eval

def thyroid_predict(features):
  vocab = ['t3_resin', 'serum_thyroxin', 'serum_triiodothyronine', 'tsh', 'ad_tsh']
  y_test_in = pd.DataFrame(features, vocab)
  X_eval = y_test_in.T

  y_eval = thyroid_model.predict(X_eval)
  return y_eval

# def kidney_predict(features):
#   df2 = pd.read_csv('dataset/kidney.csv')
#
#   X = df2[df2.columns.difference(['class'])]
#   y = df2['class']
#   X = X.drop('Unnamed: 0',axis = 1)
#   vocab = X.columns.tolist()[:]
#   print(vocab)
#   y_test_in = pd.DataFrame(features, vocab)
#   X_eval = y_test_in.T
#
#   y_eval = model_kidney.predict(X_eval)
#   return y_eval


  

