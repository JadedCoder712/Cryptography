"""
cryptography.py
Author: <your name here>
Credit: <list sources used, if any>

Assignment:

Write and submit a program that encrypts and decrypts user data.

Ideas: I will have three "if" functions for the program, each for the different menu options. Wrong: The "key" will be made the name of a lambda function with general parameters, but which uses a randomly sorted list (using the random function) will put inputs into the lambda function.

See the detailed requirements at https://github.com/HHS-IntroProgramming/Cryptography/blob/master/README.md
"""
associations = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789 .,:;'\"/\\<>(){}[]-=_+?!"

menu=input("Enter e to encrypt, d to decrypt, or q to quit: ")

if menu is "q":
    print("Goodbye!")

if menu is "e":
    message=input("Message: ")
    key=input("Key: ")
    
    
    
    


if menu is "d":
    message1=input("Message: ")
    key1=input("Key: ")
    