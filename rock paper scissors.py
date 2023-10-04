from random import choice
objects = ["rock", "paper", "scissors"]
computer = choice(objects)
rps = input("What will you choose? Rock, Paper, or Scissors?").lower().strip()
if rps == computer:
  print("It is a tie! :p")
if rps == ("rock"):
  if computer == ("scissors"):
    print("Yay! You won! :)")
if rps == ("paper"):
  if computer == ("rock"):
    print("Yay! You won! :)")
if rps == ("scissors"):
  if computer == ("paper"):
    print("Yay! You won! :)")
if computer == ("scissors"):
  if rps == ("paper"):
    print("Nooo You lost :(")
if computer == ("paper"):
  if rps == ("rock"):
    print("Nooo You lost :(")
if computer == ("rock"):
  if rps == ("scissors"):
    print("Nooo You lost :(")
print("Thanks for playing")