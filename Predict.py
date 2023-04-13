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

from Train_model import Train_model

class Predict:
    
    def predict_and_readCSV(self, filepath, column_name):
        ##quick clean
        df = pd.read_csv(filepath)
        df.drop_duplicates(inplace = True)
        df.isna().sum()
        df.dropna()
         
        ##init model.pkl
        trained_model = Train_model()
        model = trained_model.load_model()
        
        #use model to predict if spam or not
        y_pred = model.predict(df[column_name])
        
         # add a new column to the dataframe and label each row as spam (1) or ham (0) based on the predictions
        df['label'] = y_pred

        # save the labeled dataframe to a new CSV file
        labeled_filepath = 'labeled_emails.csv'
        df.to_csv(labeled_filepath, index=False)

        # print out the total number of spam emails
        num_spam_emails = sum(y_pred)
        print(f'Total number of spam emails: {num_spam_emails}')
        num_ham_emails = len(y_pred) - sum(y_pred)
        # print out the total number of ham emails
        print(f'Total number of ham emails: {num_ham_emails}')

        return labeled_filepath
    
    def move_spam_mails_to_spam_folder(self, labeled_filepath)
        

p = Predict()
p.predict_and_readCSV('emails.csv', 'Body')