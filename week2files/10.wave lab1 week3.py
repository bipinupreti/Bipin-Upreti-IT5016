def wavelength():
    nm = int(input("enter the nm "))
    if 620< nm <750:
        print("Red")
    elif 590< nm <620:
        print("Orange")
    elif 570< nm <590:
        print("Yellow")
    elif 495< nm <570:
        print("Green")
    elif 450< nm <495:
         print("Blue")
    elif 380< nm <450:
         print("Violet")
    else:
        print("ERROR")
def main():
    wavelength()
main()