import pandas as pd
import numpy as np
import string
from nltk.corpus import stopwords
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import classification_report, confusion_matrix, accuracy_score
import pickle

class classifier:
    
    def simple_model():
        df = pd.read_csv('spam_ham_dataset.csv')
        df.drop_duplicates(inplace = True)
        df.isna().sum()
        df.dropna()
        
        X_train,X_test,y_train,y_test=train_test_split(df.text,df.label_num,test_size=0.25)
        
        clf=Pipeline([
            ('vectorizer',CountVectorizer()),
            ('nb',MultinomialNB())
        ])
        
        
        clf.fit(X_train,y_train)
        
        
    #step 1 preprocess the csv_data
    def preprocess_and_get_bow(self, filepath, textcolumn):
        
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
    
        print(df[textcolumn].head(6).apply(process_text))

        #create bag of words to run into model
        message_bow = CountVectorizer(analyzer=process_text).fit_transform(df[textcolumn].head(5))
        
        print("message_bow completed")
        return message_bow

    def train_model(self):
        
        ##Train model using kaggle email data
        df = pd.read_csv('spam_ham_dataset.csv')
        
        ## turn text into a bag of words used to represent text data as numerical feature vector
        message_bow = self.preprocess_and_get_bow('spam_ham_dataset.csv', 'text')

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
        
        with open('my_model.pkl', 'wb') as f:
            pickle.dump(classifier, f)
        
        
    def load_model(self):
        # Load the saved model from disk
        with open('my_model.pkl', 'rb') as f:
            model = pickle.load(f)
        
        print("model loaded")
        
        return model
    
    

#create 
test = classifier()
message_bow = test.preprocess_and_get_bow('emails.csv', 'Body') #Test if works
message_bow1 = test.preprocess_and_get_bow('spam_ham_dataset.csv', 'text')
#classifierObject = test.train_model() #finally works
print(message_bow1.shape)
classifier = test.load_model()

emails=[
    'Sounds great! Are you home now?',
    'Will u meet ur dream partner soon? Is ur career off 2 a flyng start? 2 find out free, txt HORO followed by ur star sign, e. g. HORO ARIES'
]

results = classifier.predict(emails)
print(results)
#    classifierObject.predict(message_bow)

# test.predict(message_bow)


    
