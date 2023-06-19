def TwoSumsII(a,target):
    start =0 
    end = len(a)-1
    for i in range(len(a)):
        if a[start] + a[end] < target:
            start+=1 
            continue
        if a[start] + a[end] > target:
            end-=1 
            continue
        else:
            return start+1,end+1
    return False
arr = list(map(int,input().split())) 
target = int(input())
print(TwoSumsII(arr,target))   