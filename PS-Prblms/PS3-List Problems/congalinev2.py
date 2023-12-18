class my_vertex:
    def __init__(self, data):
        self.item = data
        self.next = None
        self.prev = None#Modification to convert to custom doubly linked list
        self.partner = None
class custom_DLL:
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
    def append_new_item(self, v):
        newvtx = my_vertex(v)
        if self._head is None:
            self._head = newvtx
            self._tail = newvtx
        else:
            newvtx.prev = self._tail#Modification to convert to custom doubly linked list
            self._tail.next = newvtx
            self._tail = newvtx
    def make_pairs(self):#only call if 2 elements are already there
        self._tail.prev.partner=self._tail
        self._tail.partner=self._tail.prev
    def print_partner_of_mikeholder(self):
        if self._mic is None:
            return None
        return self._mic.partner.item
    def is_mic_at_tail(self):
        if self._mic is None:
            return False
        return self._mic == self._tail
    def operation_R(self):
        if self.is_mic_at_tail():
            self._mic=self._head
        else:
            if self._mic==self._head:#when mic holder is first
                next_mic=self._mic.next
                self._tail.next=self._mic
                self._mic.prev =self._tail
                self._tail=self._mic
                self._mic.next=None
                self._mic=next_mic
                self._head=self._mic
                self._mic.prev=None
            else:#when is inbetween
                next_mic = self._mic.next
                next_mic.prev = self._mic.prev
                self._mic.prev.next = next_mic
                self._mic.next = None
                self._mic.prev = self._tail
                self._tail.next = self._mic
                self._tail = self._mic
                self._mic = next_mic
#Need to check if already behind partner
# Need to do similarly for when opp partner is in the end
# When both are in-between: Done
# Need to check when mic holder not in start and partner at end: Done
# Need to check for when mic holder is in the start and partner not at end:Done
# Need to check for when mic holder is in the start and partner at end :Done
    def operation_C(self):
        if self.is_mic_at_tail():
            self._mic=self._head
        else:
            if self._mic.prev==self._mic.partner:
                self._mic = self._mic.next
            elif self._mic.partner==self._tail and self._mic==self._head:#when mic holder is in the start and partner at end
                next_mic=self._mic.next
                self._mic.prev=self._mic.partner
                self._mic.partner.next=self._mic
                self._tail=self._mic
                self._mic.next=None
                self._mic=next_mic
                self._head=self._mic
                self._mic.prev=None
            # elif self._mic==self._head and self._mic.next==self._mic.partner:
            #     pass
            #when mic holder is in the start and partner not at end and to check further if this :partner is not second is valid
            #Havent check below
            elif self._mic==self._head and self._mic.partner!=self._tail:
                next_mic=self._mic.next
                self._head=self._mic.next
                self._mic.next.prev=None##Condition could be added inbetween to check if mic is head to optimize
                next_ele=self._mic.partner.next#Y
                self._mic.partner.next=self._mic
                self._mic.prev=self._mic.partner
                next_ele.prev=self._mic
                self._mic.next=next_ele
                self._mic=next_mic
            #when mic holder not in start and partner at end
            #Havent checked
            elif self._mic!=self._head and self._mic.partner==self._tail:
                next_mic = self._mic.next
                self._mic.prev.next=self._mic.next
                self._mic.next.prev=self._mic.prev
                self._mic.partner.next=self._mic
                self._mic.prev=self._mic.partner
                self._mic.next=None
                self._tail=self._mic
                self._mic=next_mic
            else:#Mic and partner are in between
                next_mic = self._mic.next
                before_mic = self._mic.prev
                partner = self._mic.partner
                next_ele = partner.next
                partner.next = self._mic
                self._mic.prev = partner
                self._mic.next = next_ele
                next_ele.prev = self._mic
                before_mic.next = next_mic
                next_mic.prev = before_mic
                self._mic = next_mic
    def show_custom_DLL(self):
        initial=self._head
        while initial:
            print(initial.item)
            initial=initial.next
import sys
a, b = map(int, input().split())
conga_line=custom_DLL()
for i in range(a):
    s = sys.stdin.readline().split()
    for name in s:
        conga_line.append_new_item(name)
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
    elif instruction=='C':
        conga_line.operation_C()
    elif instruction=='P':
        print(conga_line.print_partner_of_mikeholder())
object_contents = vars(conga_line)
print()
conga_line.show_custom_DLL()
