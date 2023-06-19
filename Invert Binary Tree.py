class TreeNode ():
    def __init__(self,value,left,right):
        self.value = value 
        self.right = right 
        self.left  = left 
"""def inverbitree(n:TreeNode):
    if not n : 
        return None 
    temp = n.left 
    n.left = n.right 
    n.right = temp 

    inverbitree(n.left)

    inverbitree(n.right)
    return n       
                             """
     
#solution 2 

"""def invertbitree(n:TreeNode):
    if not n : 
        return None 
    n.left , n.right = invertbitree(n.right),invertbitree(n.left)
    return n """