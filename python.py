import datetime
import imaplib #Internet Message Access Protocol (IMAP)
import email
import csv

class EmailScraper:
    def __init__(self):
        self.mail = imaplib.IMAP4_SSL('imap.gmail.com')
        
    def login(self, email_address, password):
        imaplib._MAXLINE = 1000000
        try:
            self.mail.login(email_address, password)
            print("Login successful")
        except:
            print("Login failed")
        

    def extract_folder_names(self):
        mailboxes = self.mail.list()[1] #produces tuple: status + inbox
        #print(mailboxes)
        folder_names = []
        for mailbox in mailboxes:
            name = mailbox.decode().split(' ')[-1].strip('"')
            print(name)
            folder_names.append(name)

        print(folder_names)
        return folder_names


    def fetch_emails(self, folder_name):
        
      
        self.mail.select(folder_name)
        status, email_bytestring_list = self.mail.search('utf-8', 'ALL')

        filename = 'emails_' + datetime.datetime.now().strftime("%Y%m%d-%H%M%S") + '.csv'

        with open(filename, 'w', newline='', encoding='utf-8') as csv_file:
            writer = csv.writer(csv_file, quoting=csv.QUOTE_ALL, quotechar='"', escapechar='\\')
            writer.writerow(['ID', 'From', 'To', 'Subject', 'Body'])

            for bytestring in email_bytestring_list[0].split():
                status, data = self.mail.fetch(bytestring, "(RFC822)")
                message = email.message_from_bytes(data[0][1])
                email_id = bytestring
                email_from = message.get('From')
                email_to = message.get('To')
                email_subject = message.get('Subject')
                email_body = ""

                for part in message.walk():
                    if part.get_content_type() == "text/plain":
                        email_body = part.as_string()

                writer.writerow([email_id, email_from, email_to, email_subject, email_body])

        print("file_created")
        self.mail.close()


emailScraper = EmailScraper()
emailScraper.login('nicolaiaphichat@gmail.com', 'qfvatlxjnagpkqcg')
emailScraper.extract_folder_names()
emailScraper.fetch_emails('[Gmail]/Stjernemarkerede')

# #Define email class
# imaplib._MAXLINE = 1000000
# SERVER = 'imap.gmail.com'
# #Connect to gmail account using special app pw
# mail = imaplib.IMAP4_SSL(SERVER) 
# mail.login('nicolaiaphichat@gmail.com', 'qfvatlxjnagpkqcg')
# # select the box you want emails from
# print(mail.list()) 
# mail.select('INBOX')

# #Search for emails with specificed rows
# #returns a byte string (bytes) list containing messageid of each email that match the search criteria
# status, email_bytestring_list = mail.search('utf-8', 'ALL')

# #print if search was successfull 
# print(status)
# ##print(email_bytestring_list[0].split())

# #Creates emails.csv if doesnt exist
# #'W' overrites the file with new data if already exists
# #newline='' ensures that line endings are suitable for the platform ur using, open() handles it for u
# #encoding makes sures the special characters python can read the files, regardless of character or language in the file
# with open('emails.csv', 'w', newline='', encoding='utf-8') as csv_file:
#     #csv.writer specifies how we want to write to the data, we quote all, escapechar handles commas and quotes chars so we dont split incorrectly
#     writer = csv.writer(csv_file, quoting=csv.QUOTE_ALL, quotechar='"', escapechar='\\')
#     #Create the folowing columns in the headers of the csv_file
#     writer.writerow(['ID', 'From', 'To', 'Subject', 'Body'])

#     #The list only has 1 element (the bytestring), so we only iterate through the 1 [0] element
#     #[b'1 2 3 4 5..]
#     #We then split bytestring to get each element and loop through them all
#     #[b'1', b'2', b'3' b'4', b'5'..]
#     for bytestring in email_bytestring_list[0].split():
#         #we can then fetch specific emails 
#         status, data = mail.fetch(bytestring, "(RFC822)") #RFC822 gets header fields and msgbody
#         #data is not readable atm so we can use the email module to make it readable 
#         message = email.message_from_bytes(data[0][1]) #tuple
#         #returns message object
        
#         #bytestring is the same as id
#         emailId = bytestring
#         emailFrom = message.get('From')
#         emailTo = message.get('To')
#         emailSubject = message.get('Subject')
        
#         # print(f"From: {message.get('From')}")
#         # print(f"To: {message.get('To')}")
#         # print(f"Subject: {message.get('Subject')}")    
        
#         print("Content:")
#         #EMails are multiparts consisting of plaintext, html, attachments
#         #we want to loop through the parts and get the content where its plain/text
#         for part in message.walk(): #Iterates through all parts of a multipart msg
#             if part.get_content_type() == "text/plain":
#                 emailBody = part.as_string()
#                 print(part.as_string())
        
#         writer.writerow([emailId, emailFrom, emailTo, emailSubject, emailBody])
        
#     mail.close()
# #print if search was successfull 
 

#to get the contents of the email, we use mail.fetch()





#Creates emails.csv if doesnt exist
#'W' overrites the file with new data if already exists
#newline='' ensures that line endings are suitable for the platform ur using, open() handles it for u
#encoding makes sures the special characters python can read the files, regardless of character or language in the file
# with open('output_filename', 'w', newline='', encoding='utf-8') as csv_file:
    
#     #create writer object
#     writer = csv.writer(csv_file)
#     writer.writerow()
    
    
# # Loop through each email ID
# # for email_id in data[0].split():

# #     # Retrieve the email message
# #     result, email_data = mail.fetch(email_id, "(RFC822)")
# #     raw_email = email_data[0][1]
# #     email_message = email.message_from_bytes(raw_email)

# #     # Print the email details
# #     print("From:", email_message['From'])
# #     print("Subject:", email_message['Subject'])
# #     print("Body:")
# #     for part in email_message.walk():
# #         if part.get_content_type() == "text/plain":
# #             body = part.get_payload(decode=True)
# #             print(body.decode('utf-8'))

# with open('emails.csv', 'w', newline='', encoding='utf-8') as csvfile:
    
#     writer = csv.writer(csvfile)
#     writer.writerow(['From', 'Subject', 'Body'])

#     # Loop through each email ID
#     for email_id in data[0].split():

#         # Retrieve the email message
#         result, email_data = mail.fetch(email_id, "(RFC822)")
#         raw_email = email_data[0][1]
#         email_message = email.message_from_bytes(raw_email)

#         # Get the email details
#         sender = email_message['From']
#         subject = email_message['Subject']
#         body = ""

#         # Extract the body of the email
#         for part in email_message.walk():
#             if part.get_content_type() == "text/plain":
#                 try:
#                     body = part.get_payload(decode=True).decode('utf-8')
#                 except UnicodeDecodeError:
#                     body = part.get_payload(decode=True).decode('iso-8859-1')

#         # Write the email details to the CSV file
#     writer = csv.writer(csvfile, quoting=csv.QUOTE_ALL, quotechar='"', escapechar='\\')
#     writer.writerow(['From', 'Subject', 'Body'])


import tkinter as tk

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

class Controller:
    def __init__(self, root):
        self.model = Model()
        self.view = View(root, self)

    def add(self):
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
