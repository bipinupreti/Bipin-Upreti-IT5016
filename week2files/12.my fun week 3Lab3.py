def myfun(a,b):
    sum=a+b
    return sum
def function1(a,b):
    addition=a+b
    return addition
def function2(a,b):
    subtraction=a-b
    return subtraction
def function3(a,b):
    multiply=a*b
    return multiply
def function4(a,b):
    divide=a/b
    return divide
def main():
    a=int(input("Enter the value for a: "))
    b=int(input("Enter the value for b: "))

    choice=int(input("Enter the function name "))
    if choice==1:
        print(function1(a,b))
    elif choice==2:
        print(function2(a,b))
    else:
        print(function4(a,b))
main()