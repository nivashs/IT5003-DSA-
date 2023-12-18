# # Name: Nivash Sudalaimani
# # Lab: B1(Jeanette)
# # Student ID:A0280048H
# # Email:e1143861@u.nus.edu
###Note:Need to check if there is any other alternative way
#Psuedo code:
'''
Backtrack from index to find the path,then compute value based on index if its left child or right child
'''
# t=int(input())
# for _ in range(t):
#     k,m=map(int,input().split())
#     def get_path(first, last):
#         my_path = []
#         while last >= first:
#             my_path.append(last)
#             if first == last:
#                 break
#             if last % 2 == 0:
#                 last //= 2
#             else:
#                 last = (last - 1) // 2
#         my_path.reverse()
#         return my_path
#     x = get_path(1, m)
#     n = len(x)
#     p, q = 1, 1
#     for i in range(n - 1):
#         if x[i + 1] == x[i] << 1:
#             p, q = p, p + q
#         else:
#             p, q = p + q, q
#     print(str(k)+' '+str(p) + '/' + str(q))

###Alternative way:
for t in range(int(input())):
    k,n = map(int, input().split())
    path = (bin(n)[3:])
    p,q = 1,1
    for ele in path:
        if ele == '0':q += p
        else:p += q
    print(str(k) + ' ' + str(p) + '/' + str(q))