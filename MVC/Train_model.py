import pandas as pd
import numpy as np
import string
from nltk.corpus import stopwords
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import classification_report, confusion_matrix, accuracy_score
import pickle
from sklearn.pipeline import Pipeline

class Train_model:
    
    def __init__(self):
        pass
    
    def simple_model(self):
        df = pd.read_csv('spam_ham_dataset.csv')
        df.drop_duplicates(inplace = True)
        df.isna().sum()
        df.dropna()
        
        X_train,X_test,y_train,y_test=train_test_split(df.text, df.label_num, test_size=0.20)
        
        #chains processing steps into one
        clf=Pipeline([
            ('vectorizer',CountVectorizer()),
            ('nb',MultinomialNB())
        ])
        
        clf.fit(X_train,y_train)
        print(clf.predict(X_train))
        print(y_train.values)
        
        pred = clf.predict(X_train)
        print(classification_report(y_train, pred))
        print()
        print('Confusion MatrixTrain: ')
        print(confusion_matrix(y_train, pred))
        print
        print("AccuracyTrain: ")
        print(accuracy_score(y_train, pred))
        print(clf.predict(X_test))
        print(y_test.values)
        pred = clf.predict(X_test)
        print(classification_report(y_test, pred))
        print()
        print('Confusion MAtrix Test: ')
        print(confusion_matrix(y_test, pred))
        print
        print("Accuracy Test: ")
        print(accuracy_score(y_test, pred))
        
        with open('simple_model.pkl', 'wb') as f:
            print('Model saved in file')
            pickle.dump(clf, f)
        
        
    def load_model(self):
        # Load the saved model from disk
        with open('simple_model.pkl', 'rb') as f:
            model = pickle.load(f)
        
        print("model loaded")
        
        return model

        
# test = Train_model()
# model = test.load_model()
# df = pd.read_csv('spam_ham_dataset.csv')
# df2 = pd.read_csv('emails.csv')
# print(df2['Body'].head())


# y_pred = model.predict(df2['Body'])

# num_spam_emails = sum(y_pred)

# # print out the total number of spam emails
# print(f'Total number of spam emails: {num_spam_emails}')

# num_ham_emails = len(y_pred) - sum(y_pred)

# # print out the total number of ham emails
# print(f'Total number of ham emails: {num_ham_emails}')

