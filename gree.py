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
        
        
        import tkinter as tk
import tkinter.scrolledtext as tkst

class Model:
    def __init__(self):
        self.value1 = 0
        self.value2 = 0
        self.result = 0

    def add(self):
        self.result = self.value1 + self.value2

class View(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller
        self.value1_label = tk.Label(self, text="Value 1:")
        self.value1_label.pack(pady=5)
        self.value1_entry = tk.Entry(self)
        self.value1_entry.pack(pady=5)
        self.value2_label = tk.Label(self, text="Value 2:")
        self.value2_label.pack(pady=5)
        self.value2_entry = tk.Entry(self)
        self.value2_entry.pack(pady=5)

        self.log = tkst.ScrolledText(self, height=4, width=50)
        self.log.pack(pady=5)

        self.add_button = tk.Button(self, text="Add", command=self.controller.add)
        self.add_button.pack(pady=5)
        self.result_label = tk.Label(self, text="Result: 0")
        self.result_label.pack(pady=5)

    def update(self, result):
        self.result_label.config(text="Result: " + str(result))

    def get_values(self):
        value1 = int(self.value1_entry.get())
        value2 = int(self.value2_entry.get())
        return value1, value2

    def log_input(self):
        value1, value2 = self.get_values()
        self.log.insert(tk.END, "Value 1: " + str(value1) + "\n")
        self.log.insert(tk.END, "Value 2: " + str(value2) + "\n")
        self.log.insert(tk.END, "------------------------\n")

class Controller:
    def __init__(self, root):
        self.model = Model()
        self.view = View(root, self)

    def add(self):
        self.view.log_input()
        value1, value2 = self.view.get_values()
        self.model.value1 = value1
        self.model.value2 = value2
        self.model.add()
        self.view.update(self.model.result)

if __name__ == "__main__":
    root = tk.Tk()
    controller = Controller(root)
    controller.view.pack()
    root.mainloop()
