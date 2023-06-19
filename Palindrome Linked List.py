class ListNode():
    def __init__(self,value,next):
        self.next = next
        self.value = value 
"""def PLL(n:ListNode):
      lista = []
      lista2 = []
      current = n      
      while current.next:
           lista.append(current.value)
           currnet = current.next
      for i in reversed(range(len(lista))):
            lista2.append(lista[i])
      if lista == lista2 :
           return True 
      return False 
        # this one works for O(n) time and O(n) space due to the list usage. 
"""
"""def PLL(n:ListNode):
    current = n
    lista = []
    while current:
        lista.append(current)
        current = current.next 
    l,r = 0 , len(lista)-1
    while l<=r:
        if lista[l]!=lista[r]:
            return False 
        l+=1
        r-=1
        # more optimised but not enough it still uses O(n)time , O(n)space 
    return True """ 

"""def PLL(n:ListNode):
       slowpointer = n 
       fastpointer = n 
       while fastpointer and fastpointer.next : 
            fastpointer = fastpointer.next.next
            slowpointer = slowpointer.next
       prev = None 
       while slowpointer: 
            temp = slowpointer.next 
            slowpointer.next = prev 
            prev = slowpointer     
            slowpointer = temp
       left , right = n , prev
       while right:
           if left.value != right.value:
                return False 
           left = left.next
           right = right.next     
       return True 
        # this solution is definitely optimal but it's not ethical since you have to re reverse the second half of the linked list because what we
        did here was using to pointer the first while makes the fast pointer point to the last element and the slow point to the middle 
        then we reverse everything starting from the middle of the linked list afeterwards we use two pointers again to scan the linked list in 
        two opposite direction while the 'right' pointer points to the tail and start backwards the left pointer points to the orginal head and go forwards 
        it does actually check if every value and it's semitric other are equal but at the end you have to return the linked list to its original form 
        by reversing the second half again and pointing the last node of the first half to the second half so it can all be one connected linked list 
        as it was before . 
    """