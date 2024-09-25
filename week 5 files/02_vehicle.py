class Vehicle:
    def __init__(self) -> None:
        pass
        
    def drive(self):
        print(f"The vehicle started.")
    def stop(self):
        print("The vehicle stopped.")
class Car(Vehicle):
    def honk(self):
        print(f"Honk! honk!")
my_car=Car()
my_car.drive()
my_car.honk()
my_car.stop()
