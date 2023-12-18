n=int(input())
domdict,katdict,ans={},{},0
for i in range(n):
    text=input()
    if text in domdict:domdict[text]+=1
    else:domdict[text]=1
for j in range(n):
    text=input()
    if text in katdict:katdict[text]+=1
    else:katdict[text]=1
for k in domdict.keys():ans+=min(domdict.get(k,0),katdict.get(k,0))
print(ans)

#Need to check why sorting does not work:
# n=int(input())
# print(sum(1 for a,b in zip(sorted([input() for i in range(n)]),sorted([input() for j in range(n)])) if a==b))
# a=['correct','correct','correct','wronganswer','timelimit']
# b=['wronganswer','timelimit','timelimit','correct','correct']
# print(sorted(a))
# print(sorted(b))

#Need to solve using list,sorting(intersection of lists using binary search)