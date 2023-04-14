import tkinter as tk
from tkinter import ttk #submodule of tkinter for combobox
import tkinter.scrolledtext as tkst


class EmailClientGUI(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.master.title("Email Client")
        self.pack()
        self.create_widgets()
        
    
    

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
    
    
    def init_combobox():
        
        
def main():
    # Add your code here
    print("Hello, world!")

if __name__ == "__main__":
    main()

root = tk.Tk()
app = EmailClientGUI(master=root)
app.mainloop()
