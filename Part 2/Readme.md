# Part 2: GUI application
The second part of the project converts the command line script in to a Python app using a simple Graphical User Interface (GUI). With the help of the
code given in the Presentation 4 (in the folder ‘Python Encryption Functions’) and the resources found at [GeeksforGeeks](https://www.google.com/url?sa=t&rct=j&q=&esrc=s&source=web&cd=&cad=rja&uact=8&ved=2ahUKEwjygZfRlfWBAxXCVkEAHbVnBc8QFnoECCUQAQ&url=https%3A%2F%2Fwww.geeksforgeeks.org%2Fpython-gui-tkinter%2F&usg=AOvVaw2jQoquEx80B61h4BcQ_Bpd&opi=89978449). The functionality
and output of the app is the same as the script.

The GUI includes fields to:

    • input the user define password – first text field;
    • output the new password – second text field;
    • state that the new password has been successfully output to file, specifying the (default) name of the file and its (path) location.

below is the GUI code:
    
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

The generate password function was modified in the following way. input_password is not e1.get() which is the input in the first text field. We set folder_path_textfile to the file path of the saved text file with the generated password. We also set password_textfield which will be used to display the newly generated password in the second textfield. Finally we set password_label text to "Password Generated" and the result_label to "Saved at: " + file_path which displays the file path to the user.