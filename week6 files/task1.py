class Car():
    def __init__(self,colour,model,year):
        self.colour=colour 
        self.model=model
        self.year=year
    def drive(self):
        print(f"The {self.colour} {self.model} was driving.")
   
    def stop(self):    
        print(f"The {self.colour} {self.model} stopped.")
    def display_infor(self):
        print(f"Car Info; {self.year} {self.colour} {self.model}")
class ElectricCar(Car):
    def __init__(self, colour,model, year, battery_capacity):
        super().__init__(colour,model,year)
        self.battery_capacity=battery_capacity
    def display_infor(self):
        super().display_infor()
        print(f"Battery Capacity: {self.battery_capacity} KWH")
my_electrice_car=ElectricCar("Wehite", "Tesla Model 3", 2022,75)
my_electrice_car.drive()
my_electrice_car.stop()
my_electrice_car.display_infor()