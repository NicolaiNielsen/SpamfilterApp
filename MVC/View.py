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
        self.login_button = ttk.Button(self, text="Login")
        self.login_button.grid(column=0, row=3, sticky=tk.W, padx=5, pady=5)

        # folder combobox
        self.folder_label = ttk.Label(self, text="Select inbox to clean")
        self.folder_label.grid(column=0, row=4, sticky=tk.W, columnspan=2, padx=5, pady=5)
        self.folder_combobox = ttk.Combobox(self, values = ['test', 'test2'])
        self.folder_combobox.grid(column=0, row=5, columnspan=2, sticky=tk.W, padx=5, pady=5)

        # Find spam
        self.find_button = ttk.Button(self, text="Search")
        self.find_button.grid(column=0, row=6, sticky=tk.W, padx=5, pady=5)

        # move to spam folder
        self.move_spam_button = ttk.Button(self, text="Move spam")
        self.move_spam_button.grid(column=0, row=7, padx=5, pady=5)

        # output log
        self.text_log = tkst.ScrolledText(self)
        self.text_log.grid(column=2, row=0,rowspan=8, sticky=tk.W, padx=5, pady=5)
        

    def main(self):
        self.mainloop() #Runs the gui
            
    
    def get_email()
            

