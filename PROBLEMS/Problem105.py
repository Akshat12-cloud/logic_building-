#Reverse an array (without using built-in reverse). 
def reverse(num):
    start=0
    end=len(num)-1
    while (start < end):
       num[start],num[end]=num[end],num[start]
       start+=1
       end-=1
    return num   
num=[1,2,3,4,5,6,7,8,9,10] 
result=reverse(num)
print(f'the reversed array is :',result)       