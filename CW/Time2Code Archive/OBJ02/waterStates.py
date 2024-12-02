def stateCalc(temp):
    if temp >= 100:
        return "Gaseous"
    elif temp < 99 and temp >= 0:
        return "Liquid"
    elif temp < 0:
        return "Solid"
    
print(f"Current state of water: {stateCalc(float(input('Enter the temperature of the water: ')))}")1