def Clamp(a,b):
    if a > b:
        return b
    elif b > a:
        return a
    else:
        return a # if theyre the same it doesnt matter lol
    
a = int(input('Enter a number: '))
b = int(input('One more number: '))

print(str(Clamp(a,b)))
    