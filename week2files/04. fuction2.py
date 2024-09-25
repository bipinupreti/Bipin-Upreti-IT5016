def fuction2(word1,word2):
    len1=len(word1)
    len2=len(word2)
    shorter_length=min(len1, len2)
    return shorter_length

word1=input("enter word1:")
word2=input("enter word2:")    
print(fuction2(word1,word2))