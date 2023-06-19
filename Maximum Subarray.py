def maxsub(a):
    total = a[0]
    temp_total = 0
    for i in range(len(a)):
        if temp_total < 0 :
            temp_total = 0
        temp_total+=a[i]
        total = max(total,temp_total)
    return total 
print(maxsub([0,1,-23,100,150]))        