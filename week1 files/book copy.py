"""
program which calcluate the total value of books.
Author: Bipin
"""
# input

bookprice=24.95
discount= 40/100
copies =60
# discount = float(input("enter your discount here:"))

# process

bookpriceaterdiscount=bookprice-(bookprice*discount)

shippingcost=3+((copies -1)*0.75)
total=(bookpriceaterdiscount*copies)+shippingcost


# output
print(total)


