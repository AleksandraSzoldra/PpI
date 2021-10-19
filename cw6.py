import random

x=random.randrange(1,6)
y=int(input("Enter a number from 1 to 6: "))

if x==y:
    print ("That's right, congrats!")
else:
    print ("Try again!")