from sklearn.metrics import classification_report, confusion_matrix, accuracy_score
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import MultinomialNB
from NaiveBayesClassifier import NaiveBayesClassifier
import string
import pandas as pd
import numpy as np
from nltk.corpus import stopwords

class Model:

    def model(self):
        
        ##Train model using kaggle email data
        df = pd.read_csv('emails.csv')
        
        ## turn text into a bag of words used to represent text data as numerical feature vector
        message_bow = NaiveBayesClassifier.read_file_and_tokenization(df)

    
        # splits the data iinto 80% training and 20% testing
        # split into training set and test set; 
        # x_train and x_test represents the characteristic such as text on which we be able to predict if its spam
        # y_train and y_test are the spam/ham columns
        # so x_train + y_train wll be 80% of the dataset
        # and x_test + y_test will be the 20%
        X_train, X_test, Y_train, Y_test = train_test_split(message_bow, df['label_num'], test_size=0.20, random_state= 0)
        
        #Creat and train the Naive Bayes Classifier
        #MultinomialNB is used to classify text, which is the model used to train our classifier
        classifier = MultinomialNB().fit(X_train, Y_train)
        
        print(classifier.predict(X_train))
        print(Y_train.values)
        pred = classifier.predict(X_train)
        print(classification_report(Y_train, pred))
        print()
        print('Confusion MAtrix: ')
        print(confusion_matrix(Y_train, pred))
        print
        print("Accuracy: ")
        print(accuracy_score(Y_train, pred))
        print(classifier.predict(X_test))

        print(Y_test.values)

        pred = classifier.predict(X_test)
        print(classification_report(Y_test, pred))
        print()
        print('Confusion MAtrix: ')
        print(confusion_matrix(Y_test, pred))
        print
        print("Accuracy: ")
        print(accuracy_score(Y_test, pred))
        
        return classifier
        
model = Model()
classifier = model.model()
        