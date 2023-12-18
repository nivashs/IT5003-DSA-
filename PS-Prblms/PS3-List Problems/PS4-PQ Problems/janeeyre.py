from heapq import heapify,heappush,heappop
n,m,total_jane_pages=map(int,input().split())
unread_books,friends_books=[],[]
for i in range(n):
    t=input().split('"')[1:]
    t[1]=int(t[1])
    unread_books.append(t)
fav_book=['Jane Eyre',total_jane_pages]
unread_books.append(fav_book)
for i in range(m):
    k = input().split('"')
    k[0],k[2] = int(k[0]),int(k[2])
    friends_books.append(k)
heapify(unread_books)
heapify(friends_books)
time=0
check=None
while check!='Jane Eyre':
    if len(friends_books)>0:
        fr1 = friends_books[0]
        while fr1[0] <= time:  # To check condition to add many books from unread and what if unread books come before
            heappush(unread_books, fr1[1:])#need to check if fr1 works properly as its updating
            heappop(friends_books)
            if len(friends_books)>0:
                fr1=friends_books[0]
            else:
                break
    ele = heappop(unread_books)  # Read the first book
    check = ele[0]
    time += ele[1]
print(time)


# unread_books=[input().split('"')[1:] for i in range(m)]
# friends_books=[input().split('"') for j in range(m)]
#friends_books_heap=[friends_books[k][1:] for k in range(m)]
# fav_book=['Jane Eyre',total_jane_pages]
# unread_books.append(fav_book)
# heapify(unread_books)
# heapify(friends_books)
# for i in range(m):
#     heappop()

# print(unread_books)
# print(friends_books)
# print(int(unread_books[0][1]))
