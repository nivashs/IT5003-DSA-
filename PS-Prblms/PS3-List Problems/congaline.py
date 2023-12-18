# # Name: Nivash Sudalaimani
# # Lab: B1(Jeanette)
# # Student ID:A0280048H
# # Email:e1143861@u.nus.edu
from collections import deque
import sys
a, b = map(int, input().split())
conga_line = deque()
partners={}
for i in range(a):
    s = sys.stdin.readline().split()
    for name in s:
        conga_line.append(name)
    partners[s[0]]=s[1]
    partners[s[1]]=s[0]
instructions=input()
mic_holder=conga_line[0]
mic_holder_index=0
for instruction in instructions:
    if instruction=='F':
        if mic_holder!=conga_line[0]:#not required
            #mic_holder=conga_line[conga_line.index(mic_holder)-1}
            mic_holder_index-=1
            mic_holder=conga_line[mic_holder_index]
    elif instruction=='B':
        mic_holder_index+=1
        mic_holder = conga_line[mic_holder_index]
    elif instruction=='R':
        if(mic_holder!=conga_line[len(conga_line)-1]):
            x=mic_holder
            mic_holder_index+=1
            mic_holder=conga_line[mic_holder_index]
            del conga_line[mic_holder_index-1]
            mic_holder_index-=1###Imp step ,del can cause issues,need to checkXXXXX
            #mic_holder=conga_line[mic_holder_index]
            conga_line.append(x)
        else:#Mic holder is at the back#Meaning of front of the line to check
            mic_holder_index=0
            mic_holder=conga_line[mic_holder_index]
            #mic_holder=conga_line[0] #need to check if front of line means this
    elif instruction=='C':
        if (mic_holder != conga_line[len(conga_line) - 1]):
            mic_holder = conga_line[mic_holder_index + 1]
            partner_index = conga_line.index(partners[mic_holder_index])
            conga_line.insert(partner_index + 1, conga_line[mic_holder_index])
            del conga_line[mic_holder_index]
            mic_holder_index += 1
        else:
            mic_holder_index = 0
            mic_holder = conga_line[mic_holder_index]
    elif instruction=='P':
        print(partners[mic_holder])
print()
for person in conga_line:
    print(person)