things = ['rock', 'paper', 'scissors']

thing = input()
choice = things[(things.index(thing) + 1) % 3]
print(f'Sorry, but the computer chose {choice}')

