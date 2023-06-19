class TreeNode():
    def __init__(self,value,right, left):
        self.right = right 
        self.left = left 
        self.value = value
"""def ovrlap(n1:TreeNode,n2:TreeNode):
    n = TreeNode(n1.value + n2.value,None,None)
    if not n1 and not n2:
        return None
    if not n1 :
        return n2 
    if not n2 :
        return n1      
    n.right = ovrlap(n1.right,n2.right)
    n.left = ovrlap(n1.left,n2.left)
    return n 
    #possible solution
    """



"""def ovrlap(n1:TreeNode,n2:TreeNode):
    if not n1 and not n2: 
        return None 
    n1value = n1.value if n1 else 0
    n2value = n2.value if n2 else 0 
    n = TreeNode(n1value+n2value,None, None )
    n.right = ovrlap(n1.right if n1 else None ,n2.right if n2 else None )
    n.left = ovrlap(n1.left if n1 else None ,n2.left if n2 else None) 
    return n 
    #    the right solution 
    """