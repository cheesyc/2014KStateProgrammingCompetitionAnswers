from __future__ import division
from decimal import Decimal
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

sf = Decimal(first - second)
fs = Decimal(second - first)

first != second

def ifstatements (first,second,fs,sf):
    if first < second:
        print "1 is the best; difference is ",fs," euroes. 2 converts to ",first," euroes."
    elif first > second:
        print "2 is the best; difference is",sf," euroes. 2 converts to", second," euroes."

ifstatements(first, second, fs, sf)
