class ListNode():
    def __init__(self,value,next):
        self.value = value
        self.next = next
def mergsll(l1: ListNode,l2: ListNode):
    dummy = ListNode()
    tail = dummy
    while l1 and l2:
        if l1.value < l2.value:
            tail.next = l1
            l1 = l1.next
            
        else:
            tail.next = l2 
            l2 = l2.next
        tail = tail.next
    if l1:
        tail.next = l1
    elif l2:
        tail.next = l2 
    return dummy.next


"""- Time Complexity: O(n+m)
  n = no of nodes in list1
  m = no of nodes in list2
- Memory Complexity: O(1)
- We have a constant space, since we are just shifting the pointers"""
                
