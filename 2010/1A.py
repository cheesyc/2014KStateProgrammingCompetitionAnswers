gas = float(input("Cost of gas: "))
numcars = float(input("Amount of cars: "))


if numcars == 1:
    car1cost = float(input("Cost of car 1: "))
    car1miles = float(input("Amount of miles on car 1: "))
    car1gas = float(input("Gallons of gas on car 1: "))
    calc1 = ((car1cost / (car1miles / car1gas)) / gas) / 2
    print ("Car 1 is the best car. Years to pay off:", calc1 )
elif numcars == 2:
    car1cost = float(input("Cost of car 1: "))
    car1miles = float(input("Amount of miles on car 1: "))
    car1gas = float(input("Gallons of gas on car 1: "))
    calc1 = ((car1cost / (car1miles / car1gas)) / gas) / 2

    car2cost = float(input("Cost of car 2: "))
    car2miles = float(input("Amount of miles on car 2: "))
    car2gas = float(input("Gallons of gas on car 2: "))
    calc2 = ((car2cost / (car2miles / car2gas)) / gas) / 2

    if calc1 < calc2:
        print ("Car 1 is the best car. Years to pay off:", calc1)
    else:
        print ("Car 2 is the best car. Years to pay off:", calc2)
elif numcars == 3:
    car1cost = float(input("Cost of car 1: "))
    car1miles = float(input("Amount of miles on car 1: "))
    car1gas = float(input("Gallons of gas on car 1: "))
    calc1 = ((car1cost / (car1miles / car1gas)) / gas) / 2

    car2cost = float(input("Cost of car 2: "))
    car2miles = float(input("Amount of miles on car 2: "))
    car2gas = float(input("Gallons of gas on car 2: "))
    calc2 = ((car2cost / (car2miles / car2gas)) / gas) / 2

    car3cost = float(input("Cost of car 3: "))
    car3miles = float(input("Amount of miles on car 3: "))
    car3gas = float(input("Gallons of gas on car 3: "))
    calc3 = ((car3cost / (car3miles / car3gas)) / gas) / 2

    if calc1 < calc2:
        if calc1 < calc3:
            print ("Car 1 is the best car. Years to pay off:", calc1)
        else:
            print ("Car 3 is the best car. Years to pay off:", calc3)
    elif calc2 < calc1:
        if calc2 < calc3:
            print ("Car 2 is the besst car. Years to pay off:", calc2)
        else:
            print ("Car 3 is the best car. Years to pay off:", calc3)

elif numcars == 4:
    car1cost = float(input("Cost of car 1: "))
    car1miles = float(input("Amount of miles on car 1: "))
    car1gas = float(input("Gallons of gas on car 1: "))
    calc1 = ((car1cost / (car1miles / car1gas)) / gas) / 2

    car2cost = float(input("Cost of car 2: "))
    car2miles = float(input("Amount of miles on car 2: "))
    car2gas = float(input("Gallons of gas on car 2: "))
    calc2 = ((car2cost / (car2miles / car2gas)) / gas) / 2

    car3cost = float(input("Cost of car 3: "))
    car3miles = float(input("Amount of miles on car 3: "))
    car3gas = float(input("Gallons of gas on car 3: "))
    calc3 = ((car3cost / (car3miles / car3gas)) / gas) / 2

    car4cost = float(input("Cost of car 4: "))
    car4miles = float(input("Amount of miles on car 4: "))
    car4gas = float(input("Gallons of gas on car 4: "))
    calc4 = ((car4cost / (car4miles / car4gas)) / gas) / 2

    if calc1 < calc2:
        if calc1 < calc3:
            if calc1 < calc4:
                print ("Car 1 is the best. Years to pay off:", calc1)
            elif calc1 > calc4:
                print ("Car 4 is the best. Years to pay off:", calc4)
        elif calc1 > calc3:
            if calc3 < calc4:
                print ("Car 3 is the best. Years to pay off:", calc3)
            else:
                print ("Car 4 is the best. Years to pay off:", calc4)
    elif calc1 > calc2:
        if calc2 < calc3:
            if calc2 < calc4:
                print ("Car 2 is the best. Years to pay off:", calc2)
            elif calc2 > calc4:
                print ("Car 4 is the best. Years to pay off:", calc4)
        elif calc2 > calc3:
            if calc3 < calc4:
                print ("Car 3 is the best. Years to pay off:", calc3)
            if calc3 > calc4:
                print ("Car 4 is the best. Years to pay off:", calc4)
elif numcars == 5:
    car1cost = float(input("Cost of car 1: "))
    car1miles = float(input("Amount of miles on car 1: "))
    car1gas = float(input("Gallons of gas on car 1: "))
    calc1 = ((car1cost / (car1miles / car1gas)) / gas) / 2

    car2cost = float(input("Cost of car 2: "))
    car2miles = float(input("Amount of miles on car 2: "))
    car2gas = float(input("Gallons of gas on car 2: "))
    calc2 = ((car2cost / (car2miles / car2gas)) / gas) / 2

    car3cost = float(input("Cost of car 3: "))
    car3miles = float(input("Amount of miles on car 3: "))
    car3gas = float(input("Gallons of gas on car 3: "))
    calc3 = ((car3cost / (car3miles / car3gas)) / gas) / 2

    car4cost = float(input("Cost of car 4: "))
    car4miles = float(input("Amount of miles on car 4: "))
    car4gas = float(input("Gallons of gas on car 4: "))
    calc4 = ((car4cost / (car4miles / car4gas)) / gas) / 2

    car5cost = float(input("Cost of car 5: "))
    car5miles = float(input("Amount of miles on car 5: "))
    car5gas = float(input("Gallons of gas on car 5: "))
    calc5 = ((car5cost / (car5miles / car5gas)) / gas) / 2


elif numcars == 6:
    car1cost = float(input("Cost of car 1: "))
    car1miles = float(input("Amount of miles on car 1: "))
    car1gas = float(input("Gallons of gas on car 1: "))

    car2cost = float(input("Cost of car 2: "))
    car2miles = float(input("Amount of miles on car 2: "))
    car2gas = float(input("Gallons of gas on car 2: "))

    car3cost = float(input("Cost of car 3: "))
    car3miles = float(input("Amount of miles on car 3: "))
    car3gas = float(input("Gallons of gas on car 3: "))

    car4cost = float(input("Cost of car 4: "))
    car4miles = float(input("Amount of miles on car 4: "))
    car4gas = float(input("Gallons of gas on car 4: "))

    car5cost = float(input("Cost of car 5: "))
    car5miles = float(input("Amount of miles on car 5: "))
    car5gas = float(input("Gallons of gas on car 5: "))

    car6cost = float(input("Cost of car 6: "))
    car6miles = float(input("Amount of miles on car 6: "))
    car6gas = float(input("Gallons of gas on car 6: "))
elif numcars == 7:
    car1cost = float(input("Cost of car 1: "))
    car1miles = float(input("Amount of miles on car 1: "))
    car1gas = float(input("Gallons of gas on car 1: "))

    car2cost = float(input("Cost of car 2: "))
    car2miles = float(input("Amount of miles on car 2: "))
    car2gas = float(input("Gallons of gas on car 2: "))

    car3cost = float(input("Cost of car 3: "))
    car3miles = float(input("Amount of miles on car 3: "))
    car3gas = float(input("Gallons of gas on car 3: "))

    car4cost = float(input("Cost of car 4: "))
    car4miles = float(input("Amount of miles on car 4: "))
    car4gas = float(input("Gallons of gas on car 4: "))

    car5cost = float(input("Cost of car 5: "))
    car5miles = float(input("Amount of miles on car 5: "))
    car5gas = float(input("Gallons of gas on car 5: "))

    car6cost = float(input("Cost of car 6: "))
    car6miles = float(input("Amount of miles on car 6: "))
    car6gas = float(input("Gallons of gas on car 6: "))

    car7cost = float(input("Cost of car 7: "))
    car7miles = float(input("Amount of miles on car 7: "))
    car7gas = float(input("Gallons of gas on car 7: "))
elif numcars == 8:
    car1cost = float(input("Cost of car 1: "))
    car1miles = float(input("Amount of miles on car 1: "))
    car1gas = float(input("Gallons of gas on car 1: "))

    car2cost = float(input("Cost of car 2: "))
    car2miles = float(input("Amount of miles on car 2: "))
    car2gas = float(input("Gallons of gas on car 2: "))

    car3cost = float(input("Cost of car 3: "))
    car3miles = float(input("Amount of miles on car 3: "))
    car3gas = float(input("Gallons of gas on car 3: "))

    car4cost = float(input("Cost of car 4: "))
    car4miles = float(input("Amount of miles on car 4: "))
    car4gas = float(input("Gallons of gas on car 4: "))

    car5cost = float(input("Cost of car 5: "))
    car5miles = float(input("Amount of miles on car 5: "))
    car5gas = float(input("Gallons of gas on car 5: "))

    car6cost = float(input("Cost of car 6: "))
    car6miles = float(input("Amount of miles on car 6: "))
    car6gas = float(input("Gallons of gas on car 6: "))

    car7cost = float(input("Cost of car 7: "))
    car7miles = float(input("Amount of miles on car 7: "))
    car7gas = float(input("Gallons of gas on car 7: "))

    car8cost = float(input("Cost of car 8: "))
    car8miles = float(input("Amount of miles on car 8: "))
    car8gas = float(input("Gallons of gas on car 8: "))
elif numcars == 9:
    car1cost = float(input("Cost of car 1: "))
    car1miles = float(input("Amount of miles on car 1: "))
    car1gas = float(input("Gallons of gas on car 1: "))

    car2cost = float(input("Cost of car 2: "))
    car2miles = float(input("Amount of miles on car 2: "))
    car2gas = float(input("Gallons of gas on car 2: "))

    car3cost = float(input("Cost of car 3: "))
    car3miles = float(input("Amount of miles on car 3: "))
    car3gas = float(input("Gallons of gas on car 3: "))

    car4cost = float(input("Cost of car 4: "))
    car4miles = float(input("Amount of miles on car 4: "))
    car4gas = float(input("Gallons of gas on car 4: "))

    car5cost = float(input("Cost of car 5: "))
    car5miles = float(input("Amount of miles on car 5: "))
    car5gas = float(input("Gallons of gas on car 5: "))

    car6cost = float(input("Cost of car 6: "))
    car6miles = float(input("Amount of miles on car 6: "))
    car6gas = float(input("Gallons of gas on car 6: "))

    car7cost = float(input("Cost of car 7: "))
    car7miles = float(input("Amount of miles on car 7: "))
    car7gas = float(input("Gallons of gas on car 7: "))

    car8cost = float(input("Cost of car 8: "))
    car8miles = float(input("Amount of miles on car 8: "))
    car8gas = float(input("Gallons of gas on car 8: "))

    car9cost = float(input("Cost of car 9: "))
    car9miles = float(input("Amount of miles on car 9: "))
    car9gas = float(input("Gallons of gas on car 9: "))
elif numcars == 10:
    car1cost = float(input("Cost of car 1: "))
    car1miles = float(input("Amount of miles on car 1: "))
    car1gas = float(input("Gallons of gas on car 1: "))

    car2cost = float(input("Cost of car 2: "))
    car2miles = float(input("Amount of miles on car 2: "))
    car2gas = float(input("Gallons of gas on car 2: "))

    car3cost = float(input("Cost of car 3: "))
    car3miles = float(input("Amount of miles on car 3: "))
    car3gas = float(input("Gallons of gas on car 3: "))

    car4cost = float(input("Cost of car 4: "))
    car4miles = float(input("Amount of miles on car 4: "))
    car4gas = float(input("Gallons of gas on car 4: "))

    car5cost = float(input("Cost of car 5: "))
    car5miles = float(input("Amount of miles on car 5: "))
    car5gas = float(input("Gallons of gas on car 5: "))

    car6cost = float(input("Cost of car 6: "))
    car6miles = float(input("Amount of miles on car 6: "))
    car6gas = float(input("Gallons of gas on car 6: "))

    car7cost = float(input("Cost of car 7: "))
    car7miles = float(input("Amount of miles on car 7: "))
    car7gas = float(input("Gallons of gas on car 7: "))

    car8cost = float(input("Cost of car 8: "))
    car8miles = float(input("Amount of miles on car 8: "))
    car8gas = float(input("Gallons of gas on car 8: "))

    car9cost = float(input("Cost of car 9: "))
    car9miles = float(input("Amount of miles on car 9: "))
    car9gas = float(input("Gallons of gas on car 9: "))

    car10cost = float(input("Cost of car 10: "))
    car10miles = float(input("Amount of miles on car 10: "))
    car10gas = float(input("Gallons of gas on car 10: "))
