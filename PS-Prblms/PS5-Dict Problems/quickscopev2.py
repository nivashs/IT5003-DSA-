from collections import defaultdict
import sys
t=int(input())
myblocks=[defaultdict(list)]
index=0
mymem=[]
mydict=defaultdict(list)
for i in range(t):
    each_line = sys.stdin.readline().split()
    if each_line[0]=='TYPEOF':
        if not mydict[each_line[1]]:
            print('UNDECLARED')
        else:
            y = mydict[each_line[1]][-1]
            print(myblocks[y][each_line[1]][0])
    elif each_line[0]=='DECLARE':
        myblocks[index][each_line[1]].append(each_line[2])
        mydict[each_line[1]].append(index)
        if len(myblocks[index][each_line[1]]) > 1:
            print('MULTIPLE DECLARATION')
            break
    else:
        if each_line[0]=='{':
            myblocks.append(defaultdict(list))
            mymem.append(each_line[0])
            index+=1
        elif each_line[0] == '}':
            mymem.pop()
            temp=myblocks.pop()
            for k in temp.keys():#to remove from master dict when } occurs
                mydict[k].pop()
            index-=1
        else:
            mymem.pop()
            index-=1

'''
Optimized by using a another dictionary and removed while compared to V1

'''