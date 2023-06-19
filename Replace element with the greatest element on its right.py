"""def rewtgeoir(l:list[int]):
    for i in range(len(l)-1):
        l[i] = max(l[i+1:])
    l[-1] = -1    
    return l
    # O(n^2) time complexity 
    
def rewtgeoir(l:list[int]): 
    temp = -1 
    for i in reversed(range(len(l))):
        new_temp = max(temp,l[i])
        l[i] = temp 
        temp = new_temp    
    return l      
    # O(n) time complexity 
   



l =[1,2,3]
print(rewtgeoir(l))       """