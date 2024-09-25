class car:
    def __init__(self,color,model):
        self.color=color
        self.model=model
    def drive(self):
        print(F"The {self.color} {self.model} is driving.")
    def stop(self):
        print(F"The {self.color} {self.model} is driving.")
car1=car("Red","Toyota")
car2=car("blue","Honda")

car1.drive()
car1.stop()