"""
Week 7 task 2
Author: Bipin 
Question: Examine the code and assess where the software design principles are lacking.
"""
class UnstructuredCode: 
    def xyzzy(self, a, b): 
        result = a + b 
        print(f"Result: {result}") 
class Calculator:
    def add(self, a, b): 
        result = a + b 
        print(f"Addition Result: {result}")

    def multiply(self, a, b): 
        result = a * b 
        print(f"Multiplication Result: {result}") 
def legacy_function(x, y):
    r = x + y
    print(f"Result: {r}")
class InflexibleShape:
    def calculate_area(self): 
        pass 
class Circle(InflexibleShape): 
    def calculate_area(self):
        pass
class Square(InflexibleShape):
    def calculate_area(self):
        pass 
# Main code
if __name__ == "__main__":
    obj = UnstructuredCode() 
    obj.xyzzy(5, 10)
    calc = Calculator()
    calc.add(5, 10) 
    calc.multiply(5, 10) 
    legacy_function(5, 10)
    circle = Circle()
    square = Square()
