def function( n1 , n2 ,n3 ):
    sum= n1 + n2+ n3
    minimum=min(n1,n2,n3)
    return sum-minimum
n1=int(input("number 1:"))
n2=int(input("number 2:"))
n3=int(input("number 3:"))
print(function(n1,n2,n3))


