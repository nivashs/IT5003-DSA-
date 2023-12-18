###Brute Force
# t=int(input())
# for k in range(t):
#     n=int(input())
#     A,B,C=map(int,input().split())
#     X,Y=map(int,input().split())
#     S=[A]
#     for i in range(1,n):
#         S.append((S[i-1]*B+A)%C)
#     V = 0
#     for i in range(n):
#         V = (V * X + S[i]) % Y
#     print(V)
# n=int(input())
# A,B,C=map(int,input().split())
# S=[A]
# for i in range(1,n):
#     S.append((S[i-1]*B+A)%C)

###Optimized and working Code:
t = int(input())
for k in range(t):
    n = int(input())
    A, B, C = map(int, input().split())
    X, Y = map(int, input().split())
    max_value = A
    A_i=A
    count = [0] * (10**6)
    count[A] = 1
    for i in range(1, n):
        A=(A * B + A_i) % C
        count[A] += 1
        max_value = max(max_value, A)
    V = 0
    for i in range(max_value + 1):
        while count[i] != 0:
            V = (V * X + i) % Y
            count[i] -= 1
    print(V)












