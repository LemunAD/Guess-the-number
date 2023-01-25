# importing libraries
import random
# Input for the player name and int for the number of guesses, generating random number and difficulty

print("1. Easy 1-10")
print("2. Medium 1-100")
print("3. Hard 1-1000")

MAX_NUM = 0
attempts = 0

difficulty = input("Please select a level")


if difficulty == "1":
    MAX_NUM = 10
    attempts = 5
elif difficulty == "2":
    MAX_NUM = 100
    attempts = 10
elif difficulty == "3":
    MAX_NUM = 1000
    attempts = 15


number = random.randint(1, MAX_NUM)
# print(number)

player_name = input("Hello, What's your name?")
number_of_guesses = 0



# Game Loop___________________________________________________________
print('okay! ' + player_name +
      ' I am Guessing a number between 1 and ' + str(MAX_NUM) + ' you have '+ str(attempts) + ' chances')
while number_of_guesses < attempts:
    guess = int(input())
    number_of_guesses += 1
    if guess < number:
        print('Your guess is too low')
        print("                         ")
        print("you have guessed "+str(number_of_guesses)+" times")
    if guess > number:
        print('Your guess is too high')
        print("                         ")
        print("you have guessed "+str(number_of_guesses)+" times")
    if guess == number:
        break


# IF THE PLAYER WINS
if guess == number:
    print('Congratulations ! You guessed the number in ' +
          str(number_of_guesses) + ' tries!')
    print('the number was ' + str(number))

else:
    print('You did not guess the number, The number was ' + str(number))
if difficulty == "69" and number_of_guesses == attempts:
    print("You lost, how unfortunate :3")
    print("Maybe you should be punished ?")
    print("Better luck next time")
if guess == number and difficulty == "69":
    print("YOU WON !!!")
    print("You may take revenge upon the game master or be free from the torture")
    print("you choose :) ")
