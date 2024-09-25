"""
Collecting User Information
Author Charanpreet singh
"""
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
    print(f"Unique id: {id_counter}")

    return user_age,user_email,user_name,id_counter
def main():
    id_counter=5000
    id_counter,user_name,user_age,user_email=collect_user_data(id_counter)
main()