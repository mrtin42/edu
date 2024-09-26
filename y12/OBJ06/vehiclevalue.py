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

def determineValueDepreciation(current, yearNow, resaleValue):
    