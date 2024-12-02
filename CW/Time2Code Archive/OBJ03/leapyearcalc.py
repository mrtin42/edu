def isLeapYear(year):
    if year % 4 == 0:
        return True
    else:
        return False
    
isIt = isLeapYear(int(input('enter the year: ')))

if isIt:
    print('it is a leap year ')
else:
    print('it is not a leap year :(')