class TreeNode():
    def __init__(self,value,right,left):
        self.value = value 
        self.right = right 
        self.left= left 
"""def findLCA(n:TreeNode,q:TreeNode,p:TreeNode):
    if q.value > n.value and p.value>n.value: 
        return findLCA(n.right,q,p)
    elif q.value<n.value and p.value<n.value: 
        return findLCA(n.left,q,p)
    else:
        return n
        
        # My solution : Time Complexity of O(n)
        """
     
def findLCA2(n:TreeNode,q:TreeNode,p:TreeNode):
    current = n 
    while current:
        if q.value > n.value and p.value>n.value: 
            current = current.right
        elif q.value < n.value and p.value<n.value: 
            current = current.left
        else:
            return current
    return None 

# Neet code solution which has a O(log(n)) time complexity     