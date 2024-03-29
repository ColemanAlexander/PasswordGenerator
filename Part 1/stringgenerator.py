#Python program to generate a strong password of a given length.
#=============================================================
#Import required libraries - random and os (operating system).
import random
import os
import time

#modified to generate password based on input seed
def generate_password(input_password):
    #Define characters to be used in the construction of the password.
    characters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!@#$%^&*()_+"
    password = ""
    random.seed(input_password)


    for i in range(len(input_password)):
        password += random.choice(characters)
    return password #Return the result
#
#Define the length of the password specified by the user.
#modified to ask user for seed
seed = input("Enter a password seed: ")
#
#Generate password using password generating function
password = generate_password(seed)
#and print the password on the screen.
print("Your new password is:", password)
#
#Write the result to file in 'Documents'.
#
#Set the path.
documents_path = os.path.expanduser("~/Documents")
#Write the password in file 'password.txt'.
file_path = os.path.join(documents_path, "password.txt")
#Open file and write result.
with open(file_path, "w") as file:
    file.write(password)
#State where file has been saved.
print("Password saved to:", file_path)



while True:
    time.sleep(20)  # You can adjust the sleep duration as needed
