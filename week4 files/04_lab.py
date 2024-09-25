def collect_user_data(id_counter):
    user_name=input("Please enter your name:")
    user_age=input("Please enter your age :")
    user_email=input("Please enter your email:")

    unique_id = id_counter+1
    id_counter=unique_id
    print("User information: ")
    print(f"Name: {user_name}")
    print(f"Age: {user_age}")
    print(f"Email: {user_email}")
    print(f"Unique_id: {id_counter}")

    return user_age,user_email,user_name,id_counter

def calculate_total_amount():
    total_amt=0.0
    while True:
        price_input=input("Enter the name of an item (or type 'finish' to end):")

        if price_input.lower()=='finish':
            break

        try:
            price=float(input(f"enter the price of item'{price_input}':"))
            total_amt+=price
        except ValueError:
            print("Invalid input, Please enter a value number.")

    return total_amt


def categorize_request(total_amt):
    
    if total_amt<150:
        category="Low"
        recommendation= "Proceed with stanrdard processing"
        print(recommendation)

    else:
        category = " High "
        recommendation = " Review for potential discount "
        print(recommendation,category)

    
    return category,recommendation

        
        
def create_detailed_report(user_age,user_email,user_name,id_counter,total_amt,category, recommendation):
    print("Detailed Report")
    print(f"Unique Id:{id_counter}")
    print(f"User Name:{user_name}")
    print(f"Age:{user_age}")
    print(f"Email:{user_email}")
    print(f"Total Amount:$ {total_amt: .2f}")
    print(f"Category:{category}")
    print(f"Recomendation:{recommendation}")

def main():
    id_counter=5000
    id_counter,user_name,user_age,user_email = collect_user_data(id_counter)
    total_amt=calculate_total_amount()
    category,recommendation=categorize_request(total_amt)
    create_detailed_report(user_age,user_email,user_name,id_counter,total_amt,category, recommendation)
main()



