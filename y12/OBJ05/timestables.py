# well isnt this beginner level

import time
import sys

def printTyping(text, newline):
    for character in text:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.025)
    if newline:
        sys.stdout.write('\n')
        sys.stdout.flush()

printTyping('Enter a number between 1 and 12: ', False)
integer = int(input())

for i in range(1,13):
    printTyping(f'{integer} x {i} = {integer*i}', True)
    time.sleep(0.2)