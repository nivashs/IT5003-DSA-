# # Name: Nivash Sudalaimani
# # Lab: B1(Jeanette)
# # Student ID:A0280048H
# # Email:e1143861@u.nus.edu
a,b=map(int,input().split())
daen_commands=input().split()
undo_flag=False
log_stack=[]
child_number=0
for command in daen_commands:
    if command!='undo' and not undo_flag:
        log_stack.append(command)
        if int(command)>=0:
            child_number=(child_number+(int(command)%a))%a
        else:
            child_number=child_number-(abs(int(command))%a)
            if child_number<0:child_number=(child_number+a)%a
    elif undo_flag:
        undo_flag=False
        for i in range(int(command)):
            undo_command=int(log_stack.pop())
            undo_command= abs(undo_command) if undo_command<=0 else (-1*undo_command)
            if undo_command >= 0:
                child_number = (child_number + (undo_command % a))%a
            else:
                child_number = child_number - (abs(undo_command) % a)
                if child_number < 0: child_number = (child_number + a)%a
    else:
        undo_flag=True
print(child_number)