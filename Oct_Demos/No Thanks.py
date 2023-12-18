n,deck_of_cards=int(input()),list(sorted(map(int,input().split())))
print(deck_of_cards[0]+sum([deck_of_cards[i] for i in range(1,n) if deck_of_cards[i-1]+1!=deck_of_cards[i]]))

#Without List Comprehension:
# sum=cards[0]
# for i in range(1,len(cards)):
#     if cards[i-1]+1!=cards[i]:
#         sum+=cards[i]
#print(sum)