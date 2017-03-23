"""
cryptography.py
Author: <your name here>
Credit: <list sources used, if any>

Assignment:

Write and submit a program that encrypts and decrypts user data.

Ideas and plan:
***
I will have three "if" functions for the program, each for the different menu options. 
Turn message into index numbers list(only numbers, probably). 
Turn password into index numbers list. 
Add password index numbers to message index numbers (one by one, probably a "for" function with each variable). 
If password is too short for message, duplicate it (should it be by a length thing to ensure enough length for the message?) and add it to itself enough to make it fit (can have excess, will not matter). 
You will get an encrypted message with the exact number of characters as in the original message (something about if one of the index numbers in the encrypted list is larger than the association list, subtract a given value from it and the system will pick up on it after it subtracts the password and finds it's too small). 
To decrypt it, subtract the key from the encrypted message and you will have the original message plus a few negative numbers at the end possibly, but these can be vetted by a program that checks to see if it is less than zero and removes it accordingly.
***


See the detailed requirements at https://github.com/HHS-IntroProgramming/Cryptography/blob/master/README.md
"""
associations = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789 .,:;'\"/\\<>(){}[]-=_+?!"
mcombination=[] 
kcombination=[]

menu=input("Enter e to encrypt, d to decrypt, or q to quit: ")

if menu is "q":
    print("Goodbye!")

if menu is "e":
    message=input("Message: ")
    key=input("Key: ")
    messagelist=list(message)
    keylist=list(key)
    for m in messagelist:
        mindexnumber=associations.find(m)
        mcombination.append(mindexnumber)
    for k in keylist:
        kindexnumber=associations.find(k)
        kcombination.append(kindexnumber)
    if len(keylist) < len(messagelist):
        
        
print(mcombination)
print(kcombination)
        

    


if menu is "d":
    message1=input("Message: ")
    key1=input("Key: ")
    