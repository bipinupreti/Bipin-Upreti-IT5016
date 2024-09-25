def earth_quake():
    mng =float(input("Enter the magnitude "))
    if mng<=2.0:
        print("Micro")
    elif 2.0>=mng<=3.0:
        print("Very minor")
    elif 3.0>=mng<=4.0:
        print("Minor")
    elif 4.0>=mng<=5.0:
        print("Light")
    elif 5.0>=mng<=6.0:
        print("Moderate")
    elif 6.0>=mng<=7.0:
        print("Strong")
    elif 7.0>=mng<=8.0:
        print("Major")
    elif 8.0>=mng<=10.0:
        print("Great")
    else:
        print("Meteoric")
def main():
    earth_quake()
main()