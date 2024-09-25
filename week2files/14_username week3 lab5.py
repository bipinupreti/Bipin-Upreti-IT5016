def username():
    studentID=str(input("Enter the student ID: "))
    First_name=str(input("Enter the First name: "))
    Last_name=str(input("Enter the last name: "))
    University=str(input("What is the name of your university: "))

    #if "Whitecliffe" in university and "COLLEGE" in university :
    username= studentID[0:2]+Last_name[0:3]
    print(f"welcome to the whitecliffe college. Your username is {username} ")
    #else:
    print("please enter your university and generate your username. ")

def main():
     print(username())
main()