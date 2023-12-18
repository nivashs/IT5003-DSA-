# Name: Nivash Sudalaimani
# Lab: B1(Jeanette)
# Student ID:A0280048H
# Email:e1143861@u.nus.edu
t=int(input())
s=input()
opening_brackets_string,closing_brackets_string='([{',')]}'
opening_brackets,ans=[],''
for char in s:
    if char in opening_brackets_string:
        opening_brackets.append(char)
    elif char in closing_brackets_string:
        if not opening_brackets:
            ans='Invalid'
            break
        elif opening_brackets_string.index(opening_brackets.pop())!=closing_brackets_string.index(char):
            ans='Invalid'
            break
if opening_brackets:
    print('Invalid')
elif not ans:
    print('Valid')
else:
    print(ans)