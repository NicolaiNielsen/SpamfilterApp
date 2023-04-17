import tkinter as tk
from tkinter import ttk #submodule of tkinter 
import tkinter.scrolledtext as tkst

class View(tk.Tk): #Inherits from ttk.frame, so u have access to ttk.frame attr + methods
    #could have created an a root object instead
    #Ttt.frame calls super().__init__()

    def __init__(self, controller):
        super().__init__() #creates instance of ttk.frame, which allows us to call mainloop()
        self.controller = controller #View needs to have access to the controller, 
        # The view needs access to the controller in order to respond to user actions and update the model
        # thin of lambda functions, whenever buttons click happens = run method from controller
        
        #self.varname allows us access the varaibles from other methods in the class
        # username
        self.username_label = ttk.Label(self, text="Username:")
        self.username_label.grid(column=0, row=0, sticky=tk.W, padx=5, pady=5)

        self.username_entry = ttk.Entry(self)
        self.username_entry.grid(column=1, row=0, sticky=tk.W, padx=5, pady=5)

        # password
        self.password_label = ttk.Label(self, text="Password:")
        self.password_label.grid(column=0, row=1, sticky=tk.W, padx=5, pady=5)

        self.password_entry = ttk.Entry(self,  show="*")
        self.password_entry.grid(column=1, row=1, sticky=tk.W, padx=5, pady=5)

        # login button
        self.login_button = ttk.Button(self, text="Login", command=self.controller.login)
        self.login_button.grid(column=0, row=3, sticky=tk.W, padx=5, pady=5)

        # folder combobox
        self.folder_label = ttk.Label(self, text="Select inbox to clean")
        self.folder_label.grid(column=0, row=4, sticky=tk.W, columnspan=2, padx=5, pady=5)
        self.folder_combobox = ttk.Combobox(self, values=['Not initalized'])
        self.folder_combobox.grid(column=0, row=5, columnspan=2, sticky=tk.W, padx=5, pady=5)

        # Find spam
        self.find_button = ttk.Button(self, text="Detect spam mails in folder", command=self.controller.fetch_emails)
        self.find_button.grid(column=0, row=6, sticky=tk.W, padx=5, pady=5)

        # move to spam folder
        self.move_spam_button = ttk.Button(self, text="Move spam to spam folder", command=self.controller.move_emails)
        self.move_spam_button.grid(column=0, row=7, padx=5, pady=5, sticky=tk.W)

        # output log
        self.text_log = tkst.ScrolledText(self)
        self.text_log.grid(column=2, row=0,rowspan=8, sticky=tk.W, padx=5, pady=5)
        

    def main(self):
        
        is_logged_in = False
        self.mainloop() #Runs the gui
            
    #get email
    def get_email(self):
        email = str(self.username_entry.get())
        return email
    
    def get_pw(self):
        pw = str(self.password_entry.get())
        return pw
    
    def set_folder_combobox(self, folder):
        self.folder_combobox['values'] = folder
        
    def get_folder(self):
        return self.folder_combobox.get() #returns selected combobox value
        
    def write(self, str):
        self.text_log.insert(tk.END, str + "\n")
        self.text_log.see("end")
            

