import imaplib #Internet Message Access Protocol (IMAP)
import email
import csv

#Define email class
imaplib._MAXLINE = 1000000
SERVER = 'imap.gmail.com'
#Connect to gmail account using special app pw
mail = imaplib.IMAP4_SSL(SERVER) 
mail.login('nicolaiaphichat@gmail.com', 'qfvatlxjnagpkqcg')

# select the box you want emails from
# print(mail.list()) 
mail.select('INBOX')

#Search for emails with specificed rows
#returns a byte string (bytes) list containing messageid of each email that match the search criteria
status, email_bytestring_list = mail.search('utf-8', 'ALL')

#print if search was successfull 
print(status)
##print(email_bytestring_list[0].split())


#Creates emails.csv if doesnt exist
#'W' overrites the file with new data if already exists
#newline='' ensures that line endings are suitable for the platform ur using, open() handles it for u
#encoding makes sures the special characters python can read the files, regardless of character or language in the file
with open('emails.csv', 'w', newline='', encoding='utf-8') as csv_file:
    #csv.writer specifies how we want to write to the data, we quote all, escapechar handles commas and quotes chars so we dont split incorrectly
    writer = csv.writer(csv_file, quoting=csv.QUOTE_ALL, quotechar='"', escapechar='\\')
    #Create the folowing columns in the headers of the csv_file
    writer.writerow(['ID', 'From', 'To', 'Subject', 'Body'])

    #The list only has 1 element (the bytestring), so we only iterate through the 1 [0] element
    #[b'1 2 3 4 5..]
    #We then split bytestring to get each element and loop through them all
    #[b'1', b'2', b'3' b'4', b'5'..]
    for bytestring in email_bytestring_list[0].split():
        #we can then fetch specific emails 
        status, data = mail.fetch(bytestring, "(RFC822)") #RFC822 gets header fields and msgbody
        #data is not readable atm so we can use the email module to make it readable 
        message = email.message_from_bytes(data[0][1]) #tuple
        #returns message object
        
        #bytestring is the same as id
        emailId = bytestring
        emailFrom = message.get('From')
        emailTo = message.get('To')
        emailSubject = message.get('Subject')
        
        # print(f"From: {message.get('From')}")
        # print(f"To: {message.get('To')}")
        # print(f"Subject: {message.get('Subject')}")    
        
        print("Content:")
        #EMails are multiparts consisting of plaintext, html, attachments
        #we want to loop through the parts and get the content where its plain/text
        for part in message.walk(): #Iterates through all parts of a multipart msg
            if part.get_content_type() == "text/plain":
                emailBody = part.as_string()
                print(part.as_string())
        
        writer.writerow([emailId, emailFrom, emailTo, emailSubject, emailBody])
        
    mail.close()
#print if search was successfull 
 

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