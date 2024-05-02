from time import sleep

total = float(input('what is the total amount on this bill: £'))
remaining = total
people = int(input('how many people are with you?'))

for i in range(0,people):
    paying = float(input('how much are you putting towards the bill: £'))

    remaining = remaining - paying

    print(f'amount remaining: £{str(remaining)}')

    if int(remaining) == 0 or int(remaining) < 0:
        print('All has been paid for.')
        break
    print(f'amount remaining: {str(remaining)}')
    print('please pass along to the next person.')
    sleep(2)
