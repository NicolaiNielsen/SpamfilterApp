import imaplib #Internet Message Access Protocol (IMAP)
import email
import csv

#Define email class
imaplib._MAXLINE = 1000000
SERVER = 'imap.gmail.com'

#Connect to gmail account using special app pw
mail = imaplib.IMAP4_SSL(SERVER) 
mail.login('nicolaiaphichat@gmail.com', 'qfvatlxjnagpkqcg')

# select the box you want to clean
print(mail.list()) 
mail.select('INBOX')

#Search for emails with specificed rows
#returns a byte string (bytes) containing the message numbers that match the search criteria
status, data = mail.search('utf-8', '(UNSEEN)')



#print if search was successfull 
print(status)

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