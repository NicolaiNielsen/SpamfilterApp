from Email_scraper import EmailScraper
from Model import Model
from View import View


class Controller: # in controller.py
    
    def __init__(self): #init model and view
        self.model = Model() 
        self.view = View(self) #parse controller into view, so the controller can access interface values
        self.email = EmailScraper()
        
    def main(self):
        self.view.main()
    
    
    def extract_folder_names_insert_combobox(self):
        folders = self.email.extract_folder_names()
        self.view.set_folder_combobox(folders)
        
    def login(self):
        email = self.view.get_email()
        pw = self.view.get_pw()
        
        self.view.log(email)
        self.view.log(pw)
        
        if self.email.login(email, pw) == True:
            self.view.log("Login success")
            self.extract_folder_names_insert_combobox()
            self.view.log("Combobox initialized")
            
        else:
            self.view.log("Login failed check credentials")


    def 
        

if __name__ == '__main__':
    run = Controller()
    run.main()