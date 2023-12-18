t=int(input())
my_dict={}
for i in range(t):
    index=int(input())
    if index in my_dict:
        x=index*((my_dict[index]//index)+1)
        while(x in my_dict):
            x=index*((my_dict[index]//index)+1)
            my_dict[index]=x
        my_dict[index]=x
        my_dict[x]=x
        print(my_dict[index])
    else:
        my_dict[index]=index
        print(my_dict[index])
'''
Working Code,as its optimized by keeping track of repetation
'''