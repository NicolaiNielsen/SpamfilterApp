import csv
import email
import imaplib
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

class Model:
    
    def __init__(self):
        pass
    
    def predict_and_readCSV(self, filepath, column_name):
        ##quick clean
        df = pd.read_csv(filepath)
        df.isna().sum()
        df.dropna(inplace=True)
         
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
    

    
   # def move_spam_mails_to_spam_folder(self, labeled_filepath):
        df = pd.read_csv(labeled_filepath)

        
        
    #     #read csv file file
    #     #compare current body to emails body
    #     #if same, then move to trash
    



with open('labeled_emails.csv', 'r') as file:
    reader = csv.reader(file)
    headers = next(reader)
    #print(headers)
    
    #login
    mail = imaplib.IMAP4_SSL('imap.gmail.com')
    mail.login('Nicolaiaphichat@gmail.com', 'qfvatlxjnagpkqcg')
    mailboxes = mail.list()[1] 
    #print(mailboxes)
    
    mail.select('[Gmail]/Spam')
    #get all emails from inbox
    status, data = mail.search(None, 'ALL')
    print(status)
    print(data) #data is a single bytestring containing containing msg_id based on the search criteri
    print(data[0]) # gives you the first (and only) element of the tuple, which is the bytes string containing the message IDs
    message_ids = data[0].split() #split the bytestring at every whitespace character and return a list of individual message IDs as strings
    
    for row in reader:
        print(row[0])
        if row[5] == '0':
            print("not spam")
            #print(row[0])
            #print(row[4])

    
    #print(data)
    #print(message_ids)
    for message_id in message_ids: #loop through all messages in in the email
        
        typ, msg_data = mail.fetch(message_id, '(UID)')
        msg_uid = msg_data[0].split()[2].decode('utf-8')
        print("message_id")
        print(message_ids)
        
        status, data = mail.fetch(message_id, '(RFC822)') #Uses iMAP4 protocol to fetch email with the given id
        #RFC822 retrives the entire raw message data as a bytes, including header and body
        #data is a tuple containing message identifier and messagepart, we only need message part
        raw_message = data[0][1] 
        #the raw msg is a bytes, which needs to converted into a email object
        message = email.message_from_bytes(raw_message)
        #from the email object we can then access the subject, header, sender, body etc of the email
        #Get the part of the body thats in "text/plain"
        
      
        print("message id")
        
        for part in message.walk():
            if part.get_content_type() == "text/plain":
                email_body = part.as_string()
                #print("EMAIL-BODY: " + email_body)
                
                for row in reader:
                    if row[5] == '1':
                       # print("ROOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOW")
                        #print(row[4])
                        if email_body == row[4]:
                            print("True mf")

        
             

    #Loop through csv file
    #for row in reader:
    #if labeled as spam, which is 1
        #if row[5] == '0':
            
            
        #then compare the csv_body to the gmail emails in that inbox
            
            
        
            #print()

