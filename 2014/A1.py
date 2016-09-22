from __future__ import division
from decimal import Decimal

while 1==1:
    length = float(input("What is the length of the track(miles) "))
    time = float(input("What is the time of your run?(seconds) "))
    x = float(input("How many times were you passed? "))

    def math1 (length,time):
        secToMin = time/60
        minToHour = secToMin/60
        yourMPH = length/minToHour
        return yourMPH

    def math2 (mph, x):
        otherMPH = mph + x * 2 ** x
        return otherMPH

    mph1 = math1(length,time)
    mph2 = math2(mph1, x)
    y = mph2 - mph1
    print y," miles per hour faster. She was ",mph2," miles per hour, you were ",mph1," miles per hour)"

    answer = raw_input("Do you want to convert again?(y/n) ")
    if answer == "n":
        raise SystemExit
