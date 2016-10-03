base = int(input("Enter length of base: "))
height = int(input("Enter height of base: "))

def math (base, height):
    area = (base * height)/2
    return area / 10

print ("Number of tiles: ",math(base,height))
