coin1 = float(input("Coin 1: "))
coin2 = float(input("Coin 2: "))
coin3 = float(input("Coin 3: "))
coin4 = float(input("Coin 4: "))
cost = float(input("Cost: "))
paid = float(input("Paid: "))
sort = []
sort.append(coin1)
sort.append(coin2)
sort.append(coin3)
sort.append(coin4)
list.sort(sort)
truepaid = paid
truecost = cost - truepaid

while truepaid > truecost:
    if sort[0] <= truecost:
        while sort[0] <= truecost:
            truepaid += sort[0]
    if sort[1] <= truecost:
        while sort[1] <= truecost:
            truepaid += sort[1]
    if sort[2] <= truecost:
        while sort[2] <= truecost:
            truepaid += sort[2]
    if sort[3] <= truecost:
        while sort[3] <= truecost:
            truepaid += sort[3]
print (truepaid)
