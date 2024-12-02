# Q6: Age check program

def check(age):
    if age < 18:
        print('You are a child.')
    elif age >= 18 and age <= 69:
        print('You are a working age adult')
    elif age > 69:
        print('You are a pension age adult.')

check(int(input('How old are you?')))