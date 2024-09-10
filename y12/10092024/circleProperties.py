def calculateRadius(di):
    return di/2

def calculateArea(rad):
    return 3.14*(rad*rad)

def calculateCircum(di):
    return 3.14*di

def calculateArcLength(circ, arcAngle):
    return (circ*arcAngle)/360

diamater = float(input('what is the diameter of the circle???? '))
arcAngle = float(input('what is the arc anglee of the circle?? '))

radius = calculateRadius(diamater)
area = calculateArea(radius)
circ = calculateCircum(diamater)
arc = calculateArcLength(circ, arcAngle)

print(f"Radius: {radius}\nArea: {area}\nCircumference: {circ}\nArc length: {arc}")
