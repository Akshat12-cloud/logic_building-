#Count how many numbers are divisible by 3 and 5 both.
def count(num):
    count=0
    for i in range(0,len(num)):
        if (num[i]%3==0 and num[i]%5==0):
            count+=1
    return count 
num=[15,50,30,2,35,60,72,75]
result =count(num)
print(f"the number of elements divisible by 3 and 5 is :",result)       
