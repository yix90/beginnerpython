#Guess a number!
#import random for number generation
import random

#Generate number first before all the drama happens
b = random.randint(0,9)
n = 0

while True:
#Input here
    inp = input("Enter a number from 0-9: ")
    
#Give an option for exit
    if inp == "quit":
        print ("Goodbye!")
        break
        
#This part checks for genuine entry
    try:
        number = int(inp)
    except:
        print ("Invalid entry!")
        continue
    if number < 0:
        print ("The number is wayyyy too small!")
        continue
    elif number > 9:
        print ("The number is wayyyy too big!")
        continue
    else:
    
#This part tests if the number is smaller or bigger than randomly generated number
        n = n+1
        if number > b:
            print ("The number is too big, try again.")
            continue
        elif number < b:
            print ("The number is too small, try again.")
            continue
        else:
            print ("Congratulations! Number of attempts made:", n)
#Generate again from here within the loop, only upon a correct guess
            b = random.randint(0,9)
            n = 0
