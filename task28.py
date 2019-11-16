def function():
    new_list=list([1,2,-1,-2,4,-5])
    itog=[]
    i=0
    while i<len(new_list):
        if new_list[i]<0:
            itog.append(-1)
            i+=1
        elif new_list[i]>0:
            itog.append(1)
            i+=1
        else:
            itog.append(0)
    return itog
x=[1,2,3,-1,-2,-3]
print(function())