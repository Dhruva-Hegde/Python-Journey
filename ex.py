name=input("Enter your name: ")
item=input("Enter your item: ")
price=int(input("Enter the price of the item: "))
quantity=int(input("Enter the quantity of the item: "))

total=quantity*price

print("\n-----BILL-----")

print(f"Name: {name}")
print(f"Item: {item}")
print(f"Price: {price}")
print(f"Quantity: {quantity}")
print(f"Total: {total}")

