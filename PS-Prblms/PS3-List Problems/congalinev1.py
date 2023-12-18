# # Name: Nivash Sudalaimani
# # Lab: B1(Jeanette)
# # Student ID:A0280048H
# # Email:e1143861@u.nus.edu
class Vertex:
    def __init__(self, data):
        self.item = data
        self.next = None
        self.prev = None#Modification to convert to doubly linked
        self.partner = None
class DLL:
    def __init__(self):
        self._head = None
        self._tail = None
        self._mic = None
    def ini_mic(self):
        self._mic = self._head
    def shiftmikeholder_front_by_one(self):
        self._mic = self._mic.next
    def shiftmikeholder_back_by_one(self):
        self._mic = self._mic.prev
    def appendleft(self, v):
        vtx = Vertex(v)
        if self._head is None:
            self._head = vtx
            self._tail = vtx
        else:
            vtx.next = self._head
            self._head.prev = vtx#Modification to convert to doubly linked
            self._head = vtx

    def append(self, v):
        vtx = Vertex(v)
        if self._head is None:
            self._head = vtx
            self._tail = vtx
        else:
            vtx.prev = self._tail#Modification to convert to doubly linked
            self._tail.next = vtx
            self._tail = vtx

    def front(self):
        if self._head is None:
            return None
        return self._head.item

    def back(self):
        if self._tail is None:
            return None
        return self._tail.item

    def popleft(self):
        if self._head is None:
            return
        if self._head == self._tail:
            self._head = None
            self._tail = None
        else:
            self._head = self._head.next
            self._head.prev = None#Modification to convert to doubly linked
    def print_mic_holder(self):
        if self._mic is None:
            return None
        return self._mic.item
###My code:
    def make_pairs(self):#only call if 2 elements are already there
        self._tail.prev.partner=self._tail
        self._tail.partner=self._tail.prev

    def print_partner_of_mikeholder(self):
        if self._mic is None:
            return None
        return self._mic.partner.item

    def is_mic_at_tail(self):
        if self._mic is None:
            return False  # If mic is not set, it cannot be at the tail
        return self._mic == self._tail  # Check if mic is the same as the tail

    def operation_R(self):
        if self.is_mic_at_tail():
            self._mic=self._head
        else:
            if self._mic==self._head:
                next_mic=self._mic.next
                self._tail.next=self._mic
                self._mic.prev =self._tail
                self._tail=self._mic
                self._mic.next=None
                self._mic=next_mic
                self._head=self._mic
                self._mic.prev=None
            else:
                next_mic = self._mic.next
                next_mic.prev = self._mic.prev
                self._mic.prev.next = next_mic
                self._mic.next = None
                self._mic.prev = self._tail
                self._tail.next = self._mic
                self._tail = self._mic
                self._mic = next_mic
    def show_DLL(self):
        initial=self._head
        while initial:
            print(initial.item)
            initial=initial.next
# check=DLL()
# check.append('amelia')
# check.append('bubba')
# check.make_pairs()
# check.append('star')
# check.append('boy')
# check.make_pairs()
# check.ini_mic()
# check.shiftmikeholder_front_by_one()#Bubba has mic
# check.operation_R()#mic should move to star and bubba becomes at end

# #print(check.print_mic_holder())
# check.shiftmikeholder_front_by_one()
# #print(check.print_mic_holder())
# check.shiftmikeholder_front_by_one()
# check.shiftmikeholder_back_by_one()
# check.shiftmikeholder_back_by_one()
# print(check.print_mic_holder())
# print(check.print_partner_of_mikeholder())


# check._head.partner = check._head.next
# check._head.next.partner = check._head
# check.append('star')
# check.append('boy')
# check._head.partner = check._head.next
# check._head.next.partner = check._head



import sys
a, b = map(int, input().split())
conga_line=DLL()
for i in range(a):
    s = sys.stdin.readline().split()
    for name in s:
        conga_line.append(name)
    conga_line.make_pairs()
instructions = input()
conga_line.ini_mic()
for instruction in instructions:
    if instruction=='F':
        conga_line.shiftmikeholder_back_by_one()
    elif instruction=='B':
        conga_line.shiftmikeholder_front_by_one()
    elif instruction=='R':
        conga_line.operation_R()
    elif instruction=='P':
        print(conga_line.print_partner_of_mikeholder())
object_contents = vars(conga_line)
print()
conga_line.show_DLL()
# for key, value in object_contents.items():
#     print(f"{key}: {value}")


###Good example of delete:
# def delete_node(self, item_to_delete):
#     current = self._head
#
#     while current:
#         if current.item == item_to_delete:
#             # Update the 'prev' and 'next' pointers to bypass the node to be deleted
#             if current.prev:
#                 current.prev.next = current.next
#             else:
#                 self._head = current.next
#
#             if current.next:
#                 current.next.prev = current.prev
#             else:
#                 self._tail = current.prev
#
#             # Set 'mic' to the next node if 'mic' is the node to be deleted
#             if self._mic == current:
#                 self._mic = current.next
#
#             # Remove 'next' and 'prev' pointers from the node to be deleted
#             current.next = None
#             current.prev = None
#
#             return True  # Node found and deleted
#
#         current = current.next
#
#     return False  # Node not found