mylist=[-9,2,-8,-12]
minimum=mylist[0]
for i in mylist:
    if ( i <= minimum ):
        minimum = i
mylist.remove(minimum)
second_min=mylist[0]
for i in mylist:
    if ( i <= second_min):
        second_min = i
print("Minimum:",minimum)
print("Second Minimum:",second_min)
