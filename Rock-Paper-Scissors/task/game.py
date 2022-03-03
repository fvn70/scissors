import random

things = ['rock', 'paper', 'scissors']

while True:
    thing = input()
    if thing == '!exit':
        print("Bye!")
        break
    if thing not in things:
        print("Invalid input")
        continue

    i = things.index(thing)
    j = random.randint(0, 2)
    choice = things[j]
    if i == j:
        print(f"There is a draw ({choice})")
    elif j == (i + 1) % 3:
        print(f"Sorry, but the computer chose {choice}")
    else:
        print(f"Well done. The computer chose {choice} and failed")
