n=int(input())
l=[input() for i in range(n)]
if l==sorted(l):print('INCREASING')
elif l==sorted(l,reverse=True):print('DECREASING')
else:print('NEITHER')