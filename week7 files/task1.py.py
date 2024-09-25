class Whitecliffe:
    def __init__(self):
       
        self.studentlist = [] 
        self.membershipcounter = 1000
        self.withdrawnstudentcounter = 400
        self.registeredstudentscounter = 600
        self.bachelorstudents = 500
        self.diplomastudents = 500

    def add_student(self):
        try:
            studentID = int(input("Enter the Student ID: "))
            lastname = input("Enter the last name of the Student: ")
            program = input("Enter the program (Bachelor/Diploma): ").strip()

           
            self.studentlist.append((lastname, studentID, program))
            self.membershipcounter += 1
            print(f"Hi {lastname}, your membership ID is: {self.membershipcounter}")

           
            if program.lower() == "bachelor":
                self.bachelorstudents += 1
            elif program.lower() == "diploma":
                self.diplomastudents += 1
            else:
                print("Unknown program. No student added to Bachelor or Diploma counts.")
        except ValueError:
            print("Invalid input for Student ID. Please enter a valid number.")

    def withdraw_student(self):
        try:
            studentID = int(input("Enter the Student ID: "))
            lastname = input("Enter the last name of the Student: ")
            program = input("Enter the program (Bachelor/Diploma): ").strip()

            student = (lastname, studentID, program)
            if student in self.studentlist:
                self.studentlist.remove(student)
                self.withdrawnstudentcounter += 1
                self.registeredstudentscounter -= 1
                print(f"Student {lastname} has been withdrawn.")
                
              
                if program.lower() == "bachelor":
                    self.bachelorstudents = max(0, self.bachelorstudents - 1)
                elif program.lower() == "diploma":
                    self.diplomastudents = max(0, self.diplomastudents - 1)
            else:
                print("Student not found in the system.")
        except ValueError:
            print("Invalid input for Student ID. Please enter a valid number.")

      
        print(f"Registered Students: {self.registeredstudentscounter}")
        print(f"Withdrawn students: {self.withdrawnstudentcounter}")

    def statistics(self):
        print(f"Number of registered students: {self.registeredstudentscounter}")
        print(f"Students in Diploma Program: {self.diplomastudents}")
        print(f"Students in Bachelor Program: {self.bachelorstudents}")
        print(f"Number of students who have withdrawn: {self.withdrawnstudentcounter}")

def main():
    system = Whitecliffe()
    while True:
      
        choice = input("\n1. New membership \n2. Withdraw Membership \n3. Statistics \n4. Exit \nChoose an option: ")
        if choice == "1":
            system.add_student()
        elif choice == "2":
            system.withdraw_student()
        elif choice == "3":
            system.statistics()
        elif choice == "4":
            print("Exiting Program...")
            break
        else:
            print("Invalid option. Please choose again.")

if __name__ == "__main__":
    main()