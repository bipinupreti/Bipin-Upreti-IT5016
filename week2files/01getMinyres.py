def get_minutes(hours, minutes):
    total=hours*60+ minutes
    return total
#total_minutes=get_minutes(3,44)    
#print(total_minutes)
hours=float(input('enter hours:'))
minutes=float(input('enter minutes:'))
total_minutes=get_minutes(hours,minutes)
print(total_minutes)