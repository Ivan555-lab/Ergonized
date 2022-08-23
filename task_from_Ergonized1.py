#Script for Ergonized
import random

email = input("'Enter email: ")
nik = input("Enter nik: ")

if email and nik:
    token = ' ' 
    for x in range(16): #Количество символов (16)       
        token = token + random.choice(list('1234567890abcdefghigklmnopqrstuvyxwzABCDEFGHIGKLMNOPQRSTUVYXWZ')) #Символы, из которых будет составлен пароль
    print('authorization:' + token)