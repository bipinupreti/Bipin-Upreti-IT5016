#item1 = 10
#item2 = 20
#item3 = 30
item1 = float(input("enter the price for item1:"))
item2 = float(input("enter the price for item2:"))
item3 = float(input("enter the price for item3:"))
subtotal = (item1+item2+item3)
sale_tax = subtotal * 0.15
total = subtotal + sale_tax
print(total)