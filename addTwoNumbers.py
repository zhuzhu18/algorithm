# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

def addTwoNumbers(l1: ListNode, l2: ListNode) -> ListNode:
    if l1 == None:
        return l2
    if l2 == None:
        return l1
    dummy = ListNode(0)
    current = dummy
    carray = 0

    while l1 or l2 or carray:
        dig = 0
        dig += 0 if l1 == None else l1.val
        dig += 0 if l2 == None else l2.val
        dig += carray
        current.next = ListNode(dig % 10)
        carray = int(dig / 10)
        current = current.next
        l1 = None if l1 == None else l1.next
        l2 = None if l2 == None else l2.next

    return dummy.next

def create(ls: list):
    current = ListNode(0)
    head = current
    for i in range(len(ls)):
        current.next = ListNode(ls[i])
        current = current.next
    return head

def display(node: ListNode):
    while node.next:
        current = node.next
        print(current.val)
        node = node.next
a = [2, 4, 3]
b = [5, 6, 4, 9]
ans = addTwoNumbers(create(a), create(b))
display(ans)
