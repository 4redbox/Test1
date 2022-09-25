"""program to guess number"""
import random

print("Welcome to slver studios")
username = input("We need a funny name to address you: ")
print('Aww...' + username + ', welcome')
rnum = random.randint(1, 100)
# print('rnum: ' + str(rnum))
gotit = False

while not gotit:
    num = input(username + " guess a number: ")
    num = int(num)

    if num == rnum:
        print(str(num) + ' is correct, ' + username)
        gotit = True
    elif num > rnum:
        print(username + ' you guessed high')
    else:
        print(username + ' you guessed low')
