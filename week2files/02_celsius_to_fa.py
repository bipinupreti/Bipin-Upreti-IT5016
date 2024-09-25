def celsius_to_f(celsius):
    fahrenheit=celsius*9/5+32
    return fahrenheit
celsius=float(input("enter the celsius:"))
print(celsius_to_f(celsius))