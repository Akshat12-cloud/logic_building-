#Create a new array containing squares of all numbers.
def newarray(num):
    arr=[]
    square=0
    for i in range(0,len(num)):
        square=num[i]*num[i]
        arr.append(square)
    return arr    


num=[1,2,3,4,5,6,7,8,9,10]
result=newarray(num)
print(f"the squares of all the number is:",result)    