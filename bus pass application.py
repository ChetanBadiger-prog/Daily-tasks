print("===== BUS PASS APPLICATION =====")

name = input("Enter your name: ")
age = int(input("Enter your age: "))

print("\nSelect Category")
print("1. Student")
print("2. Working Professional")
print("3. Senior Citizen")

category = int(input("Enter category number: "))

distance = int(input("Enter distance in KM: "))

print("\nSelect Pass Type")
print("1. Monthly Pass")
print("2. Yearly Pass")

pass_type = int(input("Enter pass type: "))

# Base price per km
price_per_km = 5

# Calculate base amount
base_amount = distance * price_per_km

# Category discount
if category == 1:  # Student
    discount = base_amount * 0.50

elif category == 2:  # Working
    discount = base_amount * 0.10

elif category == 3:  # Senior
    discount = base_amount * 0.60

else:
    discount = 0

amount_after_discount = base_amount - discount

# Pass type calculation
if pass_type == 1:
    final_amount = amount_after_discount

elif pass_type == 2:
    final_amount = amount_after_discount * 10  # yearly offer

else:
    final_amount = -1

# Final Output
if final_amount == -1:
    print("Invalid pass type selected")

else:
    print("\n===== BUS PASS DETAILS =====")
    print("Name:", name)
    print("Age:", age)
    print("Distance:", distance, "KM")
    print("Base Amount:", base_amount)
    print("Discount:", discount)
    print("Final Amount to Pay:", final_amount)
    print("Bus Pass Application Successful ✅")