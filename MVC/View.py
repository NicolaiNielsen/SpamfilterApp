import tkinter as tk
from tkinter import ttk #submodule of tkinter 
import tkinter.scrolledtext as tkst

class View(ttk.frame):

    def __init__(self, controller):
        super().__init__()
        self.controller = controller

    def main(self):
        self.mainloop()


# username
username_label = ttk.Label(root, text="Username:")
username_label.grid(column=0, row=0, sticky=tk.W, padx=5, pady=5)

username_entry = ttk.Entry(root)
username_entry.grid(column=1, row=0, sticky=tk.W, padx=5, pady=5)

# password
password_label = ttk.Label(root, text="Password:")
password_label.grid(column=0, row=1, sticky=tk.W, padx=5, pady=5)

password_entry = ttk.Entry(root,  show="*")
password_entry.grid(column=1, row=1, sticky=tk.W, padx=5, pady=5)

# login button
login_button = ttk.Button(root, text="Login")
login_button.grid(column=0, row=3, sticky=tk.W, padx=5, pady=5)

# folder combobox
folder_label = ttk.Label(root, text="Select inbox to clean")
folder_label.grid(column=0, row=4, sticky=tk.W, columnspan=2, padx=5, pady=5)
folder_combobox = ttk.Combobox(root, values = ['test', 'test2'])
folder_combobox.grid(column=0, row=5, columnspan=2, sticky=tk.W, padx=5, pady=5)

# Find spam
find_button = ttk.Button(root, text="Search")
find_button.grid(column=0, row=6, sticky=tk.W, padx=5, pady=5)

# move to spam folder
move_spam_button = ttk.Button(root, text="Move spam")
move_spam_button.grid(column=0, row=7, padx=5, pady=5)

# output log
text_log = tkst.ScrolledText(root)
text_log.grid(column=2, row=0,rowspan=8, sticky=tk.W, padx=5, pady=5)



root.mainloop()