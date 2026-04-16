#Swap the first and last elements of the array.
def swaplastfirst(num):
    temp=0
    temp=num[0]
    num[0]=num[len(num)-1]
    num[len(num)-1]=temp
    return num
    

num=[1,2,3,4,5,6,7,8,9]
result=swaplastfirst(num)
print(f"the new array is :",result)      