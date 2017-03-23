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

#all the lists that need to be made for the program:
mcombination=[] 
kcombination=[]
encryption=[]
encryptedmessage=[]
mcombination1=[]
kcombination1=[]
answertolife=[]
answermessage=[]
length=len(associations)

#menu options:
menu=input("Enter e to encrypt, d to decrypt, or q to quit: ")

#q to quit option:
if menu is "q":
    print("Goodbye!")


#e to encrypt option:
if menu is "e":
    message=input("Message: ")
    key=input("Key: ")
    messagelist=list(message)
    keylist=list(key)
    for m in messagelist:                  #turns the message into a list of index numbers
        mindexnumber=associations.find(m)
        mcombination.append(mindexnumber)
    for k in keylist:                      #turns the key into a list of index numbers
        kindexnumber=associations.find(k)
        kcombination.append(kindexnumber)
    keylength=len(keylist)                  #finds the length of the key and message lists, respectively
    messagelength=len(messagelist)
    if keylength < messagelength:           #if the length of the key list is less than that of the message list, multiply the key list by the difference, rounded up
        difference=round((messagelength/keylength)+0.5)
        kcombination=kcombination*difference
    for k in kcombination:                  #creates the encryption from the key and message lists
        for m in mcombination:
            encryption=[k + m for k, m in zip(kcombination, mcombination)] 
    for n, a in enumerate(encryption):      #erases numbers post-addition that are too large to turn into characters in the index 
        if a > 85:
            encryption[n]=(a-85)
    for x in encryption:                    #turns the encryption into actual letters
        finallyletters=associations[x]
        encryptedmessage.append(finallyletters)
    encryptedmessage="".join(encryptedmessage)  #turns it from a list to a string
    print(encryptedmessage)                     #prints string
    
"""
print(mcombination)
print(kcombination)
print(encryption)
"""


#d to decrypt option
if menu is "d":
    message1=input("Message: ")
    key1=input("Key: ")
    messagelist1=list(message1)
    keylist1=list(key1)
    for m in messagelist1:          #turns encrypted message list into appropriate index numbers
        mindexnumber1=associations.find(m)
        mcombination1.append(mindexnumber1)
    for k in keylist1:              #turns key list into appropriate index numbers
        kindexnumber1=associations.find(k)
        kcombination1.append(kindexnumber1)
    keylength1=len(keylist1)        #takes the key list length
    messagelength1=len(messagelist1)  #takes the encrypted message list length
    if keylength1 < messagelength1: #if the key list length is less than the encrypted message list length, find the multiplication difference through division and multiply the answer to the key
        difference1=round((messagelength1/keylength1)+0.5)
        kcombination1=kcombination1*difference1
    answertolife=[m-k for m, k in zip(mcombination1, kcombination1)]    #creates the message from the key and the message lists by subtracting the numbers
    for n, a in enumerate(answertolife):
        if a < 0:
            answertolife[n]=(a+85)
    for x in answertolife:                              #turns the index numbers into letters and adds them to a list
        finallyletters1=associations[x]
        answermessage.append(finallyletters1)
    answermessage="".join(answermessage)        #turns it from a list into a string
    print(answermessage)

   
   


   
   
   
   

        
        
    