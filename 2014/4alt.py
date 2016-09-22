from __future__ import division
import numpy as np

first = raw_input("What is the first word? ")
second = raw_input("What is the second word? ")

list1 = list(first)
list2 = list(second)
def xor(list1, list2):
    outputlist = []
    list3 = list1 + list2
    for i in range(0, len(list3)):
        if ((list3[i] not in list1) or (list3[i] not in list2)) and (list3[i] not in outputlist):
            outputlist[len(outputlist):] = [list3[i]]
    return outputlist

prnt = len(xor(list1, list2))
print "Difference of",prnt,"characters"
