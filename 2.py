from __future__ import division
from decimal import Decimal

probability = float([0.5,0.4,0.6,0.75,0.3,0.83])_

nogames = float(input("Enter number of games "))

if nogames == 0:
    print "Probability: 1"
else:
    userlist = []
    maxLength = 6
    while len(userlist) < maxLength:
        x = 0
        useradd = input("Enter Game Number ")
        if useradd = 1:
            userlist.append(0.4)
        elif useradd = 2:
            userlist.append(0.6)
        elif useradd = 3:
            userlist.append(0.75)
        elif useradd = 4
            userlist.append(0.3)
        elif useradd = 5:
            userlist.append(0.83)
        again = float(raw_input("Do you want to add another number?(y/n) "))
        if again == "n":
            maxLength = 0
        else:
            x + 1
            
