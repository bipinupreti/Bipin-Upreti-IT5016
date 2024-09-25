def total_user_numbers():
    total= 0
    numbers=int(input("Enter a number(0 to end ):"))
    while numbers != 0:
        total+=numbers
        numbers=int(input("Enter a number(0 to end ):"))
    print("Total:", total)

def main():
    total_user_numbers()
main()