def TwoSums(numbers:list[int],total:int):
    prevMap = {}
    for i in range(len(numbers)):
        c = total - numbers[i]
        if c not in prevMap:
            prevMap[numbers[i]] = i
        else:
            retlist = []
            retlist.append(prevMap.get(c,0))
            retlist.append(i)
            return retlist
print(TwoSums([1,2,3,5,4,5,6],5))        
