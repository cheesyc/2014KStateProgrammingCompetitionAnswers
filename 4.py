first = raw_input("What is the first word? ")
second = raw_input("What is the second word? ")

list1 = list(first)
list2 = list(second)
prnt = len([i for i, j in zip(list1, list2) if i ==j])

print "Has",prnt,"characters in common"
