p,q=map(int,input().split())
ans=set(input().split())
for i in range(p-1):ans=ans.intersection(set(input().split()))
print(len(ans))
for item in sorted(list(ans)):
    print(item)