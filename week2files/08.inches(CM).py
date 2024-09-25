#Extercise2
def inches_cm(inc,cm):
    inches=cm/inc
    return inches
def cminches(inc,cm):
    cm=inc*cm
    return cm
inches=float(input("enter the inches:"))    
cm=float(input("enter the cm:"))
print(inches_cm(inches,cm))
print(cminches(inches,cm))