import tkinter as tk
from tkinter import ttk #submodule of tkinter 
import tkinter.scrolledtext as tkst
from Predict import Predict



class View(tk.Tk): #to make view inherit form tk.tk
    
    PAD = 10
    
    def __init__(self, controller):
        super().__init__() #allows us to call tk methods
        self.controller = controller #init controller
        self.title("Find spam emails")
        self.value_var = tk.StringVar()
        self._make_main_frame()
        self._make_entry()
        self._make_buttons()
         
    def main(self):
        self.mainloop()
        print("in main of view")
        
    def _make_main_frame(self):
        self.main_frame = ttk.Frame(self)
        self.main_frame.pack(padx=self.PAD, pady=self.PAD) #creates padding
        
    def _make_entry(self): #__ for private methods
        ent = ttk.Entry(self.main_frame, textvariable=self.value_var)
        ent.pack()
        
    def _make_buttons(self):
        frame = ttk.Frame(self.main_frame)
        frame.pack()

    def create_widgets(self):
        # create label and text field for email
        self.email_label = tk.Label(self, text="Email:")
        self.email_label.pack(side="top")
        self.email_entry = tk.Entry(self, width=40)
        self.email_entry.pack(side="top")

        # create label and text field for password
        self.password_label = tk.Label(self, text="Password:")
        self.password_label.pack(side="top")
        self.password_entry = tk.Entry(self, show="*", width=40)
        self.password_entry.pack(side="top")

        # create button to login
        self.login_button = tk.Button(self, text="Login", command=self.login)
        self.login_button.pack(side="top")

        # create text log
        self.text_log = tkst.ScrolledText(self, width=60, height=20)
        self.text_log.pack(side="bottom")
        
        # Create a Combobox widget
        self.combo_box = ttk.Combobox(self.master)
        self.combo_box['values'] = ('Option 1', 'Option 2', 'Option 3')
        # Set the default value of the Combobox
        self.combo_box.current(0)
        # Pack the Combobox widget onto the window
        self.combo_box.pack(side="top")
        
    def combobox_get():
        return combo_box.get()
        

    def login(self):
        # get email and password from text fields
        email = self.email_entry.get()
        password = self.password_entry.get()

        # perform email login using email and password
        # ...

        # add output to text log
        self.text_log.insert(tk.END, "Login successful\n")

class Controller:
    
    def __init__(self):
        self.model = Predict()
        self.view = View(self.model)
        
    
    def main(self):
        self.view.main()
        


if __name__ == "__main__":
    controller = Controller()
    controller.main()

