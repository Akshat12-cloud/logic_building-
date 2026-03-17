#Take 24-hour time (hours and minutes) and print whether it is AM or PM. 
time=input("enter the time in 24-hour format (hh:mm): ")
hours,minute=time.split(":")
hours=int(hours)
minute=int(minute)
if hours<12:
    print("AM")
else:
    print("PM")