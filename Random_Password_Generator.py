import random

qqq = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
pass_len = int(input("Enter the Desired length of the password : "))
password = ""
for i in range(0,pass_len):
    random_char = random.choice(qqq)
    password = password + random_char
print("Randomly Generated Password is : ", password)
