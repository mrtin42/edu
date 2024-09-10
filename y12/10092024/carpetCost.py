underlayPPM = 3
fittingFee = 50

def carpetCost(width, length, ppm):
    metresSquared = width * length
    carpetPrice = metresSquared * ppm
    gripperCost = (width * 2) + (length * 2)
    totalCost = carpetPrice + gripperCost + fittingFee + (underlayPPM * metresSquared)
    return totalCost

print(f"The price of this carpet is £{carpetCost(int(input('What is the width of the room? ')), int(input('What is the length of this room? ')), int(input('What is the price of this carpet per metre? ')))}.")
