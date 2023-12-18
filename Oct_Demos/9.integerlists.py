# # Name: Nivash Sudalaimani
# # Lab: B1(Jeanette)
# # Student ID:A0280048H
# # Email:e1143861@u.nus.edu
from collections import deque
t=int(input())
for i in range(t):
    reverse_flag,error_flag = False,False
    operations=input()
    n,my_list=int(input()),input().strip('[]')
    integers=deque([int(i) for i in my_list.split(',') if i])
    for operation in operations:
        if operation=='R':
            reverse_flag=not reverse_flag
        else:
            if len(integers)==0:
                error_flag=True
                break
            elif reverse_flag:
                integers.pop()
            else:
                integers.popleft()
    if reverse_flag and not error_flag:integers.reverse()
    print(str(list(integers)).replace(' ','') if not error_flag else 'error')


#
#print(str(list(integers)).replace(' ','') if bool(integers) else 'error')