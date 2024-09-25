"""
program to calclulate the age
"""
personname=str(input( " enter the name of person " ))
year_of_birth=int(input( " enter the birth year of person " ))
current_year=int(input( ' enter the cureent year ' ))
personage=current_year-year_of_birth
print( "hello", personname , "you are now" , personage , "year old." , "Wow!!!" )

a=42
b=3.14
c="hello world"
d=[1,2,3]
e=(1,2,3)
f={"name":"john","age":30}
print(type(a))
print(type(b))
print(type(c))
print(type(d))
print(type(e))
print(type(f))
import math
print(math.exp(b))
print(math.modf(a))
print(math.modf(b))
add=a+5
print(add)
sub=a-10
print(sub)
multi=a*2
print(multi)
charanpreet=a//7
print(charanpreet)
print(c.upper())
print(a+b)
