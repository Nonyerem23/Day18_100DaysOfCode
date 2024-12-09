print("Guess the number")
print("You have 5 tries to guess the number")
print("The number is between 1 and 100000")
import random
number = random.randint(1,100000)
tries = 5
while tries > 0:
  guess = int(input("Enter your guess: "))
  if guess == number:
    print("You guessed the number!")
    break
  elif guess > number:
    print("Your guess is too high")
  else:
    print("Your guess is too low")
  tries -= 1
if tries == 0:
  print("You ran out of tries")
  print("The number was", number)
