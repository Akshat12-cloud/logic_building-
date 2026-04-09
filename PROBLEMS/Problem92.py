#Count how many times a given element appears. 
def countelement(num):
    count=0
    for i in range(0,len(num)):
        if num[i]==target:
            count+=1
    print(f"the no. of elements {target} is {count}")        
num=[2,1,6,3,2,7,9,1,4,4]
target=int(input('enter the element'))
countelement(num)            