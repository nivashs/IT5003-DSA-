###Need to Optimize:
n=int(input())
cards=list(map(int,input().split()))
q=int(input())
ranges=[list(map(int,input().split())) for i in range(q)]
cards.sort()
def find_index(l,ele,mode):
    left, right = 0, len(l) - 1
    ans = -1
    while left <= right:
        mid = left + (right - left) // 2
        if l[mid] == ele:
            ans = mid
            if mode==1:right = mid - 1##right for getting last index of duplicate
            else:left = mid + 1##left for getting first index of duplicate
        elif l[mid] < ele:
            left = mid + 1
        else:
            right = mid - 1
    return ans
def find_next_greatest_element(l, ele):
    left, right = 0, len(l) - 1
    next_greatest = -1
    while left <= right:
        mid = left + (right - left) // 2
        if l[mid] > ele:
            next_greatest = mid
            right = mid - 1
        else:
            left = mid + 1
    return next_greatest
for a,b in ranges:
    if a==b:
        print(cards.count(a))
        continue
    index_a=find_index(cards,a,1)
    index_b=find_index(cards,b,0)
    if index_a==index_b==-1 and a<cards[0] and b>cards[-1]:
        print(len(cards))
        continue
    elif index_a==index_b==-1 and a>cards[-1] and b>cards[-1]:
        print(0)
        continue
    elif index_a == index_b == -1 and a < cards[0] and b < cards[0]:
        print(0)
        continue
    elif index_a == index_b == -1 and a>cards[0] and a<cards[-1] and not (cards[0] < b < cards[-1]):
        index_a,index_b=find_next_greatest_element(cards,a),len(cards)-1
    elif index_a == index_b == -1 and b > cards[0] and b < cards[-1] and not (cards[0] < a < cards[-1]):
        index_b, index_a = find_next_greatest_element(cards, b)-1, 0
    elif cards[0] < a < cards[-1] and cards[0] < b < cards[-1] and index_a == index_b == -1:
        index_a,index_b=find_next_greatest_element(cards,a),find_next_greatest_element(cards, b)-1
    elif index_a == -1 and index_b!=-1 and a<cards[0]:
        index_a=0
    elif index_a != -1 and index_b == -1 and b>cards[-1]:
        index_b=len(cards)-1
    elif index_a != -1 and index_b == -1 and cards[0] < b < cards[-1]:
        index_b=find_next_greatest_element(cards, b)-1
    elif index_a == -1 and index_b != -1 and cards[0] < a < cards[-1]:
        index_a=find_next_greatest_element(cards, a)
    print(index_b-index_a+1)