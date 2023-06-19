def slide(a):
    l= 0 
    r=0
    current_max_profit =0
    max_profit = 0
    while r<=len(a)-1:
        if a[r]<a[l]:
            l=r
            #current_max_profit = a[r]-a[l]
        elif a[r]>a[l]:
            current_max_profit =a[r] -a[l]     
            max_profit = max(max_profit,current_max_profit)
        r+=1    
    return max_profit 
        

print(slide([7,1,5,4,5,8,1,1]))