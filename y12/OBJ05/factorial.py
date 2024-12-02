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

def fact(num):
    result = num
    for i in range(num-1, num-num, -1):
        printTyping(f'{result} x {i} = {result*i}', True)
        result = result * i
    return result

printTyping('Enter a number: ', False)
num = int(input())
printTyping(f'The factorial of {num} is {fact(num)}', False)
