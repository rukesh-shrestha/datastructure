class Selection:
    pass

mylist = [78,53,765,24,13,1,9,66]
print(sorted(mylist))
print(mylist)

idx = None

for x in range(len(mylist)):
    for i in range(x+1,len(mylist)):
        if x < i:
            print(mylist[x])

    # print('x+1',x+1)
