#!/usr/bin/python

list =[4, 5, 7, 8, 9, 1, 0, 7, 4]
list.sort()
prev=list[0]
del list[0]
for item in list:
    if prev == item:
        print("Dupliacte of " ,prev, " Fond")
    prev = item
