from __future__ import division
from decimal import Decimal

game_number = [0,1,2,3,4,5]
probability = float([0.5,0.4,0.6,0.75,0.3,0.83])_

nogames = float(input("Enter number of games "))

if nogames == 0:
    print "Probability: 1"
else:
    userlist = []
    maxLength = 6
    while len(userlist) < maxLength:
        useradd = input("Enter Game Number ")
        userlist.append(useradd)
        again = float(raw_input("Do you want to add another number?(y/n) "))
        if again == "n":
            maxLength = 0
        
