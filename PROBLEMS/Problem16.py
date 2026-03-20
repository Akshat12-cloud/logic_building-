#Take coordinates (x, y) and check if the point lies on the X-axis, Y-axis, or at the 
#origin.
x= int(input("enter the x coordinate: "))
y=int(input("enter the y coordinate:")) 
if (x==0 and y==0):
    print("point lies at the origin")
elif (x==0):
    print("point lies on the Y-axis")
elif (y==0):
    print("point lies on the X-axis")
else:
    print("point lies in the plane")
    
