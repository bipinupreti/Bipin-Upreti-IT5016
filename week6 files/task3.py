class Car():
    def __init__(self,model,colour,year):
        self.model=model
        self.colour=colour
        self.year=year
    def cardetails(self):
        print(f"{self.colour}") 
        print(f"{self.model}")  
        print(f"{self.year}")
Car1=Car("GTR","Black",2024)  
Car1.cardetails()