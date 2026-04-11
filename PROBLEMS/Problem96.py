#Find the sum of odd elements only. 
def sum(num):
    sum=0
    for i in range(0,len(num)):
        if(num[i]%2!=0):
            sum=num[i]+sum
    return sum
num=[1,2,3,4,5,6,7,8,9,10]  
result=sum(num)
print(f"the sum of odd number is: ",result)      