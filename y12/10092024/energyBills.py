def energyRawCost(previous, current, cfv):
    # for cfv just put 39.3 because idiot
    unitsUsed = current - previous
    kWh = (unitsUsed * 1.022 * cfv) / 3.6
    charge = 2.84 * kWh
    return charge

print(f"Raw cost (subject to change upon further calculations): {energyRawCost(float(input('What was the previous meter reading? ')),float(input('What is the current meter reading? ')),39.3)}")