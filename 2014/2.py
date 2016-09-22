from __future__ import division
from decimal import Decimal

nogames = float(input("Enter total number of games "))

if nogames == 0:
    print "Probability: 1"
    raise SystemExit
else:
    userlist = []
    while len(userlist) < nogames:
        useradd = input("Enter Game Number ")
        if useradd == 1:
            userlist.append(0.4)
        elif useradd == 2:
            userlist.append(0.6)
        elif useradd == 3:
            userlist.append(0.75)
        elif useradd == 4:
            userlist.append(0.3)
        elif useradd == 5:
            userlist.append(0.83)
        elif useradd == 0:
            userlist.append(0.5)

print "Probability:" + str(reduce(lambda x, y: x*y, userlist))
