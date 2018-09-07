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
    answer=''
    task=input('Enter e to encrypt, d to decrypt, or q to quit: ')
    if task=='q':
        break
    elif task=='e':
        string=input('Message: ')
        key=input('Key: ')
        kterm=0
        for x in list(string):
            for n in range(len(assoguide)):
                if assoguide[n][0]==x:
                    str_n=assoguide[n][1]
                if assoguide[n][0]==list(key)[kterm]:
                    key_n=assoguide[n][1]
            fin_n=str_n+key_n
            while fin_n>85:
                fin_n -= 85
            kterm+=1
            if kterm==len(key):
                kterm=0
            for n in range(len(assoguide)):
                if assoguide[n][1]==fin_n:
                    piece=assoguide[n][0]
            answer=answer+piece
        print(answer)
    elif task=='d':
        string=input('Message: ')
        key=input('Key: ')
        kterm=0
        for x in list(string):
            for n in range(len(assoguide)):
                if assoguide[n][0]==x:
                    str_n=assoguide[n][1]
                if assoguide[n][0]==list(key)[kterm]:
                    key_n=assoguide[n][1]
            fin_n=str_n-key_n
            while fin_n>85:
                fin_n -= 85
            while fin_n<0:
                fin_n +=85
            kterm+=1
            if kterm==len(key):
                kterm=0
            for n in range(len(assoguide)):
                if assoguide[n][1]==fin_n:
                    piece=assoguide[n][0]
            answer=answer+piece
        print(answer)