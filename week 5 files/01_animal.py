class Animal:
    def __init__(self, name):
        self.name=name

    def speak(self):
        print(f"{self.name}makes a sound.")
class Dog(Animal):
    def bark(self):
        print(f"{self.name} barks.")
my_dog=Dog("Buddy")
my_dog.speak()
my_dog.bark()