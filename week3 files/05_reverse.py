def reversed_string(s):
    reverse_string =""
    for char in s:
        reverse_string=char + reverse_string
    return reverse_string
      

def main():
    original_string=input("Enter a string:")
    reverse_string=reversed_string(original_string)
    print(f"original: {original_string}")
    print(f"reversed: {reverse_string}")

main()