import random 

print("number guessing game")

number = random.randint(1,9)
chances=0

print("guess a number between 1 , 9")

while chances < 5 :
    guess=int(input("enter your guess:"))
    if guess == number:
        print("congratulations you won")
        break
    elif guess < number:
        print("guess is too low")
    else:
        print("guess is too high")
    chances+=1
if not chances < 5:
    print("you lose,the actual number was ",number)        