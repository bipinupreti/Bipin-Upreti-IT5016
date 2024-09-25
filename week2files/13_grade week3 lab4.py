def grade_calculator():
    assessment_grade=float(input("Enter the assessment grade: "))
    exam_grade=float(input("Enter the exam grade: "))
    avg=assessment_grade+exam_grade
    avg_grade=avg*0.5
    return print(avg_grade,"%")

def main():
    print(grade_calculator())

    avg_grade=float(input("Enter the average grade"))

    if 90<=avg_grade:
        print("Your final grade is A.")
    elif 80<=avg_grade:
        print("Your grade is B.")
    elif 70<=avg_grade:
        print("Your grade is C.")
    elif 60<=avg_grade:
        print("Your grade is D.")
    else:
        print("Your are fail.")

main()
