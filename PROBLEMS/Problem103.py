#Replace all even numbers with 1 and all odd with 0.
def replace(num):
    for i in range(0,len(num)):
        if num[i]%2==0:
            num[i]=1
        else:
            num[i]=0
    return num
num=[1,2,3,4,5,6,7,8,9,10]
result=replace(num)
print(f"the new array is :",result)
            