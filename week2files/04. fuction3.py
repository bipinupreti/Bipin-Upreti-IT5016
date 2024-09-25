def fuction3(word):
    first=word[0]
    last=word[len(word) -1]
    combined=last+first
    return combined.upper()
word=input("Enter a word>>")    
print(fuction3(word))