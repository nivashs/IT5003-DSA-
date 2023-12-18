# # Name: Nivash Sudalaimani
# # Lab: B1(Jeanette)
# # Student ID:A0280048H
# # Email:e1143861@u.nus.edu

## Gives runtime error for someunknown reason:

from collections import deque
t=int(input())
for i in range(t):
    reverse_flag,error_flag = False,False
    operations=input()
    n=int(input())
    integers=deque(input().strip('[]').split(',')) if n!=0 else deque([])
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
    print("["+",".join(integers)+"]" if not error_flag else 'error')

integers = []
result = ",".join(integers)
# This will result in a TypeError


