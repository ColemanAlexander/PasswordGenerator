#Python program to generate a strong password.
#=============================================================
#Import required libraries - random and os (operating system).
#Importing tkinter for GUI implementation

import sys
from tkinter import *
import random
import os



#modified to generate password based on input seed
def generate_password():
    #Define characters to be used in the construction of the password.
    characters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!@#$%^&*()_+"
    password = ""
    input_password = e1.get()
    random.seed(input_password)
    #Apply a for loop to implement the iteration: 
    # password = password + random choice 
    #of defined characters using function random.
    for i in range(len(input_password)):
        password += random.choice(characters)

#Write the result to file in 'Documents'.

#Set the path.
    documents_path = os.path.expanduser("~/Documents")
#Write the password in file 'password.txt'.
    file_path = os.path.join(documents_path, "password.txt")
#Open file and write result.
    with open(file_path, "w") as file:
        file.write(password)
#State where file has been saved.
    
    folder_path_textfile.set(file_path)
    password_textfield.set(password)
    password_label.config(text="Password Generated ")
    result_label.config(text="Saved at: " + file_path)
     #Return the result



m = Tk()
folder_path_textfile = StringVar()
password_textfield = StringVar()
m.title("Password generator")
input_word = Label(m, text='Enter password seed')
input_word.pack()
e1 = Entry(m)
e1.pack()



button = Button(m, text='Generate', width=25, command=generate_password) 
button.pack()

password_label = Label(m, text="")
password_label.pack()

e2 = Entry(m, textvariable=password_textfield)
e2.pack() 

result_label = Label(m, text="")
result_label.pack()


def on_closing():
    sys.exit(0)

m.protocol("WM_DELETE_WINDOW", on_closing)
m.mainloop()