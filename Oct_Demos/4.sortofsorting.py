ans=[]
while True:
    n = int(input())
    if not n:break
    l=[input() for i in range(n)]
    l=sorted(l,key=lambda x:x[:2])
    ans.append(l)
for i in range(len(ans)):
    for j in ans[i]:
        print(j)
    if i!=len(ans)-1:print()