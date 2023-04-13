import pandas as pd
import numpy as np
import string
from nltk.corpus import stopwords
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import classification_report, confusion_matrix, accuracy_score

class NaiveBayesClassifier:

    def __init__(self, filepath, model):
        self.filepath = filepath
        self.model = model
        
    #step 1 preprocess the csv_data
    def read_file_and_tokenization(self, filepath):
        #1 remove columns
        #2 remove missing data
        #1 remove punctuation
        #2 remove stopwords such as ", "an", "the", "this", "that" that dont add much meaning
        #3 return list of clean text words
        
        #read csv
        df = pd.read_csv(filepath)
        df.drop_duplicates(inplace = True)
        df.dropna()
        

        def process_text(text): 
            #1 remove punctuation
            #2 remove stopwords
            #3 return list of clean text words

            nopunc = [char for char in text if char not in string.punctuation] 
            nopunc = ''.join(nopunc) 
            
            #returns csv without punction
            clean_words = [word for word in nopunc.split() if word.lower() not in stopwords.words('english')]

            return clean_words
    
        # print(df['Body'].head(6).apply(process_text))

        #create bag of words to run into model
        message_bow = CountVectorizer(analyzer=process_text).fit_transform(df['Body'])
        
        return message_bow
    
    def predict 
    
        
        
    predict
    


test = NaiveBayesClassifier('emails.csv')
cleandf = test.read_file()


    
