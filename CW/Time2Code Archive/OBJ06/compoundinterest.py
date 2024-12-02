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

interest_rate = 1.02 # using the actual (nov24) rates from HSBC MySavings

def determineYearlyBalance(current, intAER, desired):
    bal = current
    year = 0
    while bal < desired:
        year = year+1
        sys.stdout.write(f'Balance after {year} year(s): £')
        time.sleep(0.5)
        sys.stdout.flush()
        bal = bal * intAER
        printTyping(f'{bal:.2f}', True)
        time.sleep(0.1)

printTyping(f'Enter your current balance: £', False)
balance = float(input())
printTyping(f'Enter your desired balance: £', False)
target = float(input())

determineYearlyBalance(balance, interest_rate, target)