def checker(a,b):
    if len(a)!= len(b):
        return False
    counta={}
    countb={}
    for i in range(len(a)):
        counta[a[i]] = 1 + counta.get(a[i],0)
        countb[b[i]] = 1 + countb.get(b[i],0)
    for i in counta:
        if counta[i] != countb.get(i,0):
            return False
    return True
a = input()
b = input()
print(checker(a,b))        