print("Welcome to Python Pizza Development")
size = input("What size pizza do you want to? S,M or L ")
pepperoni = input("Do you want pepperoni on your pizza? Y or N ")
cheese = input("Do you want extra cheese on your pizza? Y or N ")
price = 0

if size == "M":
    price += 20
    if pepperoni == "Y":
        price += 2
    if cheese == "Y":
        price += 1
if size == "S":
    price += 15
    if pepperoni == "Y":
        price += 2
    if cheese == "Y":
        price += 1
if size == "L":
    price += 25
    if pepperoni == "Y":
        price += 2
    if cheese == "Y":
        price += 1

print(f"The final price will be ${price}")

