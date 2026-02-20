print("welcome to supermarket")

name = input("what is your name : ")

print("available items are")
print("1. Rice - 60 Rs/kg")
print("2. Sugar - 45 Rs/kg")
print("3. Oil - 150 Rs/litre")
print("4. Milk - 30 Rs/packet")

choice = input("enter your choice : ")
qty = int(input("enter quantity : "))

if choice == "1":
    item = "Rice"
    price = 60
elif choice == "2":
    item = "Sugar"
    price = 45
elif choice == "3":
    item = "Oil"
    price = 150
elif choice == "4":
    item = "Milk"
    price = 30
else:
    print("invalid choice")
    price = 0

total = price * qty

if total>=1000:
    discount = total*0.25
else:
    discount = 0

final_bill = total-discount

if item =="invalid":
    print("invalid choice")
else:
    print("=====bill=====")
    print("your name is :",name)
    print("item is :",item)
    print("qty is :",qty)
    print("total is :",total)
    print("discount is :",discount)
    print("final bill", final_bill)



