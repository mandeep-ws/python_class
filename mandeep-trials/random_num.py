import random
user_input = ""
num1 = random.randint(1,100)
print("WELCOME TO GUESS ME!")
print("I'm thinking of a number between 1 and 100")
print("If your guess is more than 10 away from my number, I'll tell you you're COLD")
print("If your guess is within 10 of my number, I'll tell you you're WARM")
print("If your guess is farther than your most recent guess, I'll say you're getting COLDER")
print("If your guess is closer than your most recent guess, I'll say you're getting WARMER")
print("LET'S PLAY!")

i = 1

while user_input != 0:
    
    
    user_input = int(input("Guess the number from 1-100:"))
    if user_input > 100 or user_input < 1:
        print("Oud Of Bounf")
        continue
    

    elif user_input == num1:
        print("Guessed in {} tries".format(i))
        num1 = random.randint(1,100)
        print(num1)
        continue
        
    elif user_input in range(num1,num1+10):
        print("Warm")
        i = i + 1
        continue
    
    elif user_input in range(num1+11 , 100):
        i = i + 1
        print("warmer")
        continue

    elif user_input in range(num1-10, num1):
        i = i + 1
        print("cold")
        continue
    else:
        print("colder")
        continue


