import sys

import pandas as pd
from Email_scraper import EmailScraper
from Model import Model
from View import View
from tqdm import tqdm
import time


class Controller: # in controller.py
    
    def __init__(self): #init model and view
        self.model = Model() 
        self.view = View(self) #parse controller into view, so the controller can access interface values
        self.email = EmailScraper() #to turn emails into csv
        
    def main(self):
        self.view.main()
    
    
    def extract_folder_names_insert_combobox(self):
        folders = self.email.extract_folder_names()
        self.view.set_folder_combobox(folders)
        
    def login(self):
        email = self.view.get_email()
        pw = self.view.get_pw()
        
        self.view.write("email: " + email)
        self.view.write("pw: " + pw)
        
        if self.email.login(email, pw) == True:
            self.view.write("Login success")
            self.extract_folder_names_insert_combobox()
            self.view.write("Combobox initialized")
            
        else:
            self.view.write("Login failed check credentials")

    def fetch_emails(self):
        self.folder = self.view.get_folder()
        self.view.write(self.folder)
        self.view.write("Search has been pressed")
        self.filename = self.email.fetch_emails(self.folder)
        self.view.write("file has been created")
        self.view.write("Labeling spam emails in csv_file")
        self.labeled_file = self.model.predict_and_readCSV(self.filename, 'Body')
        
    def move_emails(self):
        self.view.write(self.labeled_file)
        self.view.write(self.folder)
        self.email.move_spam_mails_to_spam_folder(self.labeled_file, self.folder)
        self.view.write("moving items to 'Moved' folder")
        

if __name__ == '__main__':
    for i in tqdm (range (101),
               desc="Loading…",
               ascii=False, ncols=75):
        time.sleep(0.01)
     
    print("Complete.")
    
    run = Controller()
    run.main()
    
    
    #qfvatlxjnagpkqcg
    #jugrctsxydpxlcpw
