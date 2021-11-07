import random

cmds = ('rock', 'paper', 'scissors', '!exit', '!rating')
things = ['rock', 'paper', 'scissors']

name = input("Enter your name: ")
print(f"Hello, {name}")

# read score from file
score = 0
with open('rating.txt', 'r') as file:
    for s in file:
        if s.startswith(name):
            score = int(s.split()[1])

# load all items
cmd = input()
if cmd:
    things = cmd.split(',')

# start game
print("Okay, let's start")
while True:
    thing = input()
    if thing == '!exit':
        print("Bye!")
        break
    if thing == '!rating':
        print(f"Your rating: {score}")
        continue
    if thing not in things:
        print("Invalid input")
        continue
    i = things.index(thing)
    ln = len(things)
    all_t = [things[k] for k in range(i + 1, ln)] + [things[k] for k in range(i)]
    n = len(all_t) // 2
    weak = [all_t[k] for k in range(n, len(all_t))]
    strong = [all_t[k] for k in range(n)]
    j = random.randint(0, ln - 1)
    choice = things[j]
    if i == j:
        print(f"There is a draw ({things[j]})")
        score += 50
    elif choice in strong:
        print(f"Sorry, but the computer chose {choice}")
    else:
        print(f"Well done. The computer chose {choice} and failed")
        score += 100
