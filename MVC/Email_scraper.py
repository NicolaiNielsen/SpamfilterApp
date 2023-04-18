import datetime
import imaplib #Internet Message Access Protocol (IMAP)
import email
import csv
import pandas as pd

from tqdm import tqdm
import time

class EmailScraper:
    def __init__(self):
        self.mail = imaplib.IMAP4_SSL('imap.gmail.com')
        
    def login(self, email_address, password):
        imaplib._MAXLINE = 1000000
        try:
            self.mail.login(email_address, password)
            print("Login successful")
            return True
        except:
            print("Login failed")
            return False
        

    def extract_folder_names(self):
        mailboxes = self.mail.list()[1] #produces tuple: status + inbox
        #print(mailboxes)
        folder_names = []
        for mailbox in mailboxes:
            name = mailbox.decode().split(' ')[-1].strip('"')
            folder_names.append(name)
        return folder_names


    def fetch_emails(self, folder_name): #fetches email from selected folder
        
        self.mail.select(folder_name) #select folder 
        status, email_bytestring_list = self.mail.search('utf-8', 'ALL') #search for all emails in folder, returns tupple with (b'ok', b'1 )
        
        total_emails = len(email_bytestring_list[0].split()) #total emails
        print(f"Fetching {total_emails} emails...") #prints total number of emails

        filename = 'emails_' + datetime.datetime.now().strftime("%Y%m%d-%H%M%S") + '.csv' #generates a new csv_file based on time + date

        with open(filename, 'w', newline='', encoding='utf-8') as csv_file: #open new file
            writer = csv.writer(csv_file, quoting=csv.QUOTE_ALL, quotechar='"', escapechar='\\') #csv_write
            writer.writerow(['UID', 'From', 'To', 'Subject', 'Body']) #csv columns

            for bytestring in tqdm(email_bytestring_list[0].split(), total=total_emails): #with logic to display loadingbar
                #get everything
                status, data = self.mail.fetch(bytestring, "(RFC822)")
                message = email.message_from_bytes(data[0][1])
                #get UID for later comparison
                status, msg_data = self.mail.fetch(bytestring, '(UID)')
                uid = msg_data[0].split()[-1].decode('utf-8')
                uid = uid.rstrip(')') #remove ) from the split 
                
                
                #variables to write to row in csv_file
                msg_uid = uid
                email_from = message.get('From')
                email_to = message.get('To')
                email_subject = message.get('Subject')
                email_body = ""
                
                #get plaintext from the email
                for part in message.walk():
                    if part.get_content_type() == "text/plain":
                        email_body = part.as_string()

                writer.writerow([msg_uid, email_from, email_to, email_subject, email_body])

        print("file_created")
        return filename
    
    
    def move_spam_mails_to_spam_folder(self, labeled_filepath, combobox):
        with open(labeled_filepath, 'r') as file:
            reader = csv.reader(file)
            #login
            # mail = imaplib.IMAP4_SSL('imap.gmail.com')
            # mail.login('Nicolaiaphichat@gmail.com', 'qfvatlxjnagpkqcg')
            # mailboxes = mail.list()[1] 
            # print(mailboxes)
            
            #select folder and allows edits 
            self.mail.select(combobox, readonly=False)
            #get all emails from inbox 
            status, data = self.mail.search(None, 'ALL')
            #print(status)
            #print(data) #data is a single bytestring containing containing msg_id based on the search criteri
            #print(data[0]) # gives you the first (and only) element of the tuple, which is the bytes string containing the message IDs
            bytestrings = data[0].split() #split the bytestring at every whitespace character and return a list of individual message IDs as strings
            
            
            spam_array = [] #create an array for all labeled spam emails in csv_file
            
            for row in reader: ##find all instances where label = 1, which means spam marked by the model
                if row[5] == '1': #if label = 1
                    spam_array.append(row[0]) #adds the uid to array, so we can loop through our inbox and compare
                    
            print(spam_array)
            
            #loop through every bytestring and get the uid
            for bytestring in bytestrings:
                #fetch the message data and the UID from the bytestring
                
                status, msg_data = self.mail.fetch(bytestring, '(UID)') #get the uid of the emails in gmail
                print("msg_data")
                print(msg_data) #returns a list of byte objects [b'44 (UID 8891)'], we can split it to get the uid 8891)
                #we extract the uid by using the split method, splits whitespace, the elements is the last in the last, so we [-1]
                #decode to convert the byte object to string
                
                try:
                    uid = msg_data[0].split()[-1].decode('utf-8')
                    uid = uid.rstrip(')')
                    print(uid)
                except (AttributeError, IndexError):
                    print('Error getting UID for bytestring:', bytestring)

                #we then check if the uid is included in the spam_array 
                if uid in spam_array:
                    #move files to moved folder
                    result = self.mail.uid('COPY', uid, '[Gmail]/Spam') 
                    
                    #if success
                    if result[0] == 'OK':
                        data = self.mail.uid('STORE', uid, '+FLAGS', '(\Deleted)')
                        self.mail.expunge()
                
            self.mail.close()
            self.mail.logout()
            
   
