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


The softwareDesign principle for this code include following principles:-
 
1. KISS (Keep It Simple, Stupid)
Application: The code is relatively straightforward, with each method serving a clear purpose. However, the `add_student` and `withdraw_student` methods can be further simplified by extracting repetitive logic into helper methods.

 2. DRY (Don't Repeat Yourself)
       Application: The program type checks (`program.lower()`) are repeated in both the `add_student` and `  withdraw_student` methods. This can be centralized to reduce redundancy.

 3. Open/Closed Principle
    Application: The code is not easily extendable to accommodate new programs (like "Masters"). Consider using     a more flexible design, such as a class hierarchy or a dictionary to manage different program types, allowing for future expansion without modifying existing code.

 4. Composition
 Application: The single `Whitecliffe` class currently manages all aspects of student registration. You could use composition by creating separate classes for `Student`, `Program`, and perhaps a `RegistrationManager`, which would encapsulate related behaviors and data.

 5. Single Responsibility Principle
   Application: The `Whitecliffe` class handles multiple responsibilities, such as student registration, withdrawal, and statistics. Breaking these into smaller, focused classes would enhance clarity and maintainability.

 6. Separation of Concerns
    Application: There is a mix of responsibilities in the `Whitecliffe` class. Consider separating user interaction (input/output) from data management (student records) for better modularity.

 7. YAGNI (You Aren't Gonna Need It)
  Application: The code focuses on current functionalities without implementing unnecessary features, adhering to this principle effectively.

 8. Avoid Premature Optimization
   Application: The current implementation is clear and understandable, avoiding unnecessary optimizations. Focus should remain on clarity before performance.

 9. Refactor
 Application: The code can benefit from refactoring to improve structure and readability. For example, creating a method for checking and updating program counts would simplify the `add_student` and `withdraw_student` methods.

10. Clean Code vs. Clever Code
 Application: The code prioritizes readability, with clear variable names and structured input prompts. However, some logic could be made clearer by using helper methods or more descriptive names.

