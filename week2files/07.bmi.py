#Extercise2
def bmi(height,weight):
    bmi=weight/(height/100)**2
    return bmi
height=float(input("enter the height"))
weight=float(input("enter the weight"))    
print(bmi(height,weight))