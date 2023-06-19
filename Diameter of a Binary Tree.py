class TreeNode():
    def __init__(self,value,left,right):
        self.value = value
        self.right = right
        self.left = left

def finddiameter(root:TreeNode) :
    result =[0]
    def dfs(root:TreeNode):
        if not root:
            return -1
        left = dfs(root.left)
        right = dfs(root.right)
        result = max(result[0], 2+ left+right)
        return  1 + max(left,right)
    dfs(root)
    return result[0]
