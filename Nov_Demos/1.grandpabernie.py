from collections import defaultdict
mydict=defaultdict(list)
for i in range(int(input())):
    place=input().split()
    mydict[place[0]].append(int(place[1]))
for v in mydict.values():
    v.sort()
for j in range(int(input())):
    place_number=input().split()
    print(mydict[place_number[0]][int(place_number[1])-1])