mylist = list(range(1500,2701))
newlist = []
for i in mylist:
    if ( i%5==0 and i%7==0):
        newlist.append(i)
print(newlist)
