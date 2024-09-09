def convertFtoC(fahrenheight):
    x = fahrenheight - 32
    celcius = x / 1.8
    return celcius

def convertCtoF(celcius):
    x = celcius * 1.8
    fahrenheight = x + 32
    return fahrenheight

def main():
    C = 30
    F = convertCtoF(C)
    print(f'{C}°C is {F}°F')

main()