from random import randint
from time import sleep

sides = int(input('How many sides are on the dice? '))

print('Rolling dice...')
sleep(1)
print(f'The dice landed on: {randint(1,sides)}')