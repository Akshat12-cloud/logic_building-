'''Take time (hours and minutes) and print the smaller angle between the hour and 
minute hands'''

hours=int(input("enter the number of hours:"))
minutes=int(input("enter the number of minutes:"))

hour_angle=(hours*30) + (minutes*0.5)

minutes_angle= minutes*6

angle=abs(hour_angle - minutes_angle)

smallest_angle= min(angle,360-angle)

print(f"The smaller angle between the hour and minute hands is: {smallest_angle} degrees")