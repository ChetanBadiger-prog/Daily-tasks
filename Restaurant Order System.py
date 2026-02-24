print("===== WELCOME TO FOOD Restaurent =====")

name = input("Enter customer name: ")

print("\nMenu Card")
print("1. Pizza - 250 Rs")
print("2. Burger - 120 Rs")
print("3. Pasta - 180 Rs")
print("4. Coffee - 80 Rs")

choice = int(input("Select your item: "))
qty = int(input("Enter quantity: "))

# Item selection
if choice == 1:
    item = "Pizza"
    price = 250

elif choice == 2:
    item = "Burger"
    price = 120

elif choice == 3:
    item = "Pasta"
    price = 180

elif choice == 4:
    item = "Coffee"
    price = 80

else:
    item = "Invalid"
    price = 0

# Bill calculation
total = price * qty
gst = total * 0.05
final_amount = total + gst

# Output
if item == "Invalid":
    print("Invalid item selected")

else:
    print("\n===== BILL =====")
    print("Customer Name:", name)
    print("Item:", item)
    print("Quantity:", qty)
    print("Subtotal:", total)
    print("GST (5%):", gst)
    print("Final Amount:", final_amount)
    print("Thank You! Visit Again 🍽")