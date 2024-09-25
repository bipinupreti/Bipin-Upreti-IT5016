# class car
class Car():
    def __init__(self,model,colour,year):
        self.model=model
        self.colour=colour
        self.year=year
    def drive(self):
        print(f"The {self.colour} {self.model} was driving by.")
   
    def stop(self):    
        print(f"The {self.colour} {self.model} stopped.")
    def cardetails(self):
        print(self.colour) 
        print(self.model)  
        print(self.year)
    def carinfo(self):
        print(F"Car Info: {self.colour} {self.year} {self.model}")

Car1=Car("GTR","Black",2024)             
Car1.drive()
Car1.stop()
Car1.carinfo()

Car1.cardetails()