num = input("What is the numerator")

dem = input("What is the denominator")

counta = 2
countb = 2

def matha(num):
    b = 1
    while b > 0:
        a = num / counta
        b = num % counta
        counta += 1
    return a
def mathb (dem):
    d = 1
    while d > 0:
        c = dem / countb
        d = dem % countb
        counta += 1
    return b

numer = matha(num)
denom = mathb(dem)

print (numer,"/",denom)
