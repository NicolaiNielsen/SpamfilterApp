import pandas as pd
import numpy as np
import string
from nltk.corpus import stopwords
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import classification_report, confusion_matrix, accuracy_score

class NaiveBayesClassifier:

    def __init__(self, filepath):
        self.filepath = filepath
        
    #step 1 preprocess the csv_data
    #
    def read_file(self):
        #1 remove columns
        #2 remove missing data
        #1 remove punctuation
        #2 remove stopwords such as ", "an", "the", "this", "that" that dont add much meaning
        #3 return list of clean text words
        
        #read csv
        df = pd.read_csv(self.filepath)
        #print head for inspection
        print(df.head(5))
        #print num of rows + columns
        print(df.shape)
        #print columns
        print(df.columns) 
        #drop duplicates in df
        df.drop_duplicates(inplace = True)
        #check and drop any completely empty emails
        print(df.isnull().sum()) 
        df.dropna()
        
        return df
    
    def process_text(self, df): 
    #1 remove punctuation
    #2 remove stopwords
    #3 return list of clean text words
        
        for each in df
            nopunc = [char for char in text if char not in string.punctuation] 
            nopunc = ''.join(nopunc) 
            
            #returns csv without punction
            clean_words = [word for word in nopunc.split() if word.lower() not in stopwords.words('english')]

            return clean_words

    
    def preprocess_data(self, df):
        #clean body email
        processed = df['Body'].head(5).apply(test.process_text) ##apply for each body row, refactor later

        return processed

    
    def predict(self, filepath):
        df = self.read_file(filepath)
        self.preprocess_data(df)
    
    def modeltrained(self, df):
        ## turn text into a bag of words used to represent text data as numerical feature vector
        message_bow = CountVectorizer(analyser=self.preprocess_data().fit_transform([df]))
        # splits the data into 80% training and 20% testing
        # split into training set and test set; 
        # x_train and x_test represents the characteristic such as text on which we be able to predict if its spam
        # y_train and y_test are the spam/ham columns
        # so x_train + y_train will be 80% of the dataset
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
        
    def predict(self, dataset)
    
        bow = CountVectorizer(analyser=self.preprocess_data().fit_transform([dataset]))
        classifier.predict(bow)

        
test = NaiveBayesClassifier('emails.csv')
cleandf = test.read_file()
print(test.preprocess_data(cleandf))




