def parnvalid(l):
    stack = []
    valdic = {')':'(',']':'[','}':'{'}
    if len(l)%2 !=0 or l == '':
        return False 
    for i in l :
        if i in valdic:
            if stack and stack[-1] == valdic[i]:
                stack.pop()

            else :
                return False
        else:
            stack.append(i)
    return True if not stack else False              

print(parnvalid(''))
