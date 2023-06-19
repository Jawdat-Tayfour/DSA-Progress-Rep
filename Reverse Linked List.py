class ListNode():
    def __init__(self,value,next):
        self.value =value 
        self.next = next
def reversessl(head:ListNode):
    prev,curr = None,head
    while curr:
        temp = curr.next 
        curr.next = prev 
        prev = curr 
        curr = temp
    return prev.value
l1 = ListNode(1,None)
l2 = ListNode(2,None)
l3 = ListNode(3,None)
l4 = ListNode(4,None)
l5 = ListNode(5,None)

l1.next = l2 
l2.next = l3 
l3.next = l4 
l4.next = l5  
print(reversessl(l1))





