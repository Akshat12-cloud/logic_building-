# Count how many elements are perfect squares. 
def countperfectsqr(num):
    count =0
    for i in range (0,len(num)):
        if num[i]>=0:
            root=int(num[i]**(1/2))
            if (root*root==num[i]):
                count+=1
    return count
num=[10,25,30,36,42,84,144] 
result=countperfectsqr(num)
print(f"the number of element perfect square is :",result)           