from heapq import heapify,heappop,heappush
n,k_deletions=map(int,input().split())
my_lst=list(map(int,input().split()))
my_freq={}
for i in my_lst:
    if i in my_freq:
        my_freq[i]+=1
    else:
        my_freq[i]=1
my_freq_list=list(map(lambda x:-x,my_freq.values()))
heapify(my_freq_list)
while(k_deletions>0):
    first_ele=-heappop(my_freq_list)
    second_largest=-my_freq_list[0]
    d=first_ele-second_largest
    if(k_deletions>=d and d!=0):
        k_deletions-=d
        x=first_ele-d
    else:
        x = first_ele - 1
        k_deletions-=1
    heappush(my_freq_list, -x)
print(-my_freq_list[0])

#working code for finding min (of max) ocurrence after k deletions:
# while(k_deletions>0):
#     first_ele=-heappop(my_freq_list)
#     x=first_ele-1
#     heappush(my_freq_list,-x)
#     k_deletions-=1
# print(-my_freq_list[0])