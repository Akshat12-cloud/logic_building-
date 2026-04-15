#Replace every negative number with 0. 
def replace(num):
    for i in range(0,len(num)):
        if (num[i]<0):
            num[i]=0
    return num
num=[1,2,-3,4,-5,6,-4,-5]
result=replace(num)
print("the new array is :",result)        