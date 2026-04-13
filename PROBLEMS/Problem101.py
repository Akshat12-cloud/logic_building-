#Create a new array containing only even elements. 
def evenarray(num):
    arr=[]
    for i in range(0,len(num)):
        if num[i]%2==0:
            arr.append(num[i])
    return arr
num= [1,2,3,4,5,6,7,8,9,10]
result=evenarray(num)
print(f"the new array of even numbers only is :",result)      
