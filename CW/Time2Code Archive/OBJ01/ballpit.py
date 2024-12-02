def pitVolume(rad,height):
    return 3.14 * (rad*rad) * height

def ballVolume(rad):
    return (4/3) * 3.14 * (rad*rad*rad)

print(f"The amount of balls needed to fit this pit is {int(pitVolume(float(input('what is the radius of the ball pit? ')),float(input('whar is the height of the ball pit? ')))/ballVolume(float(input('what is the radius of the balls? '))))}")