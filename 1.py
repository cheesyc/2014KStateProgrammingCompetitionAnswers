from __future__ import division

def math (l,t):
    mps = l / t
    mph = mps * 3600
    return mph

ui1 = int(input("How far did you run in miles? "))
ui2 = int(input("How long did you run in seconds? "))

answer = math(ui1, ui2)

print "You ran %s mph!" % answer
