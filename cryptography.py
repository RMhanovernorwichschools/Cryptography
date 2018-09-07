"""
cryptography.py
Author: <your name here>
Credit: <list sources used, if any>

Assignment:

Write and submit a program that encrypts and decrypts user data.

See the detailed requirements at https://github.com/HHS-IntroProgramming/Cryptography/blob/master/README.md
"""
associations = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789 .,:;'\"/\\<>(){}[]-=_+?!"
assoguide=list(zip(list(associations), range(1,len(associations)+1)))

while True:
    task=input('Enter e to encrypt, d to decrypt, or q to quit: ')
    if task=='q':
        break
    elif task=='e':
        string=input('Message: ')
        key=input('Key: ')