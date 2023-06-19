def Rob(a):
    amount1 = 0 
    amount2 = 0
    for i in a :
        temp = max(amount1+i,amount2)
        amount1 = amount2
        amount2 = temp
    return amount2
print(Rob([1,1,1,2,3,4,5,8,9]))
