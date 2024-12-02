def saveTheChange(cost):
    if (round(cost) - cost) < 0:
        change = 1 + (round(cost) - cost) # adding a negative number is equivalent to subtracting the positive counterpart
        return change
    elif (round(cost) - cost) == 0:
        return 0
    else:
        return round(cost) - cost

cost = float(input("Enter the const of the item: £"))
change = saveTheChange(cost)
if change > 0:
    print(f'The change is £{change:.2f}: This will be credited to your savings account')
else:
    print('No change available to credit')