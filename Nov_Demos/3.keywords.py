# from collections import defaultdict
# mydict=defaultdict(int)
# my_dict={}
# count_unique=0
# t=int(input())
# for i in range(t):
#     word=input().lower()
#     print(word)
#     if not mydict[word]:
#         count_unique+=1
#         mydict[word]=1
# print(count_unique)

my_unique_set=set()
t=int(input())
for i in range(t):
    word=input().lower().replace('-',' ')
    my_unique_set.add(word)
print(len(my_unique_set))