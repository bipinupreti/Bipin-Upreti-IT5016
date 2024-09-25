"""
Collecting User Information
Author Bipin
"""
def calculate_total_amount():
    total_amount=0.0
    while True:
        price_input=input("Enter the name of an item (or type 'finish' to end):")

        if price_input.lower()=='finish':
            break

        try:
            price=float(input(f"enter the price of item'{price_input}':"))
            total_amount+=price
        except ValueError:
            print("Invalid input, Please enter a value number.")

    print(f"The total amount is: ${total_amount:.2f}")
    return total_amount
calculate_total_amount()
