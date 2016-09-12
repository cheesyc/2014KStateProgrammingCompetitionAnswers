from __future__ import division
from decimal import Decimal
while 1==1:
    usd = float(input("How much in USD? "))
    cr1 = float(input("What is the convertion rate of the first one? "))
    fee1 = float(input("What is the fee of the first one? "))

    cr2 = float(input("What is the convertion rate of the second one? "))
    fee2 = float(input("What is the fee of the second one? "))

    def convertion (usd, cr, fee):
        usdwfee = usd - fee
        convert = usdwfee * cr
        return convert

    first = convertion(usd, cr1, fee1)
    second = convertion(usd, cr2, fee2)

    sf = first - second
    fs = second - first

    first != second

    def ifstatements (first,second,fs,sf):
        if first < second:
            print "1 is the best; difference is ",fs," euroes. 2 converts to ",first," euroes."
        elif first > second:
            print "2 is the best; difference is",sf," euroes. 2 converts to", second," euroes."

    ifstatements(first, second, fs, sf)

    again = raw_input("Do you want to convert more?(y/n) ")

    if again == "n":
        raise SystemExit
