print("welcome to indian railway")

name = input("enter your name :")
age = int(input("enter your age :"))

print("select the coach")
print("1. AC coach = rs 800")
print("2. sleeper coach = rs 600")
print("3. general coach = rs 400")

coach = input("choose the coach :")
if coach == "1":
    ticket_price=800
elif coach == "2":
    ticket_price=600
elif coach == "3":
    ticket_price=400
else:
    ticket_price=-1

if ticket_price == -1:
    print("invalid credentials")
else:
    if age<5:
        ticket_price = 0
    elif age>60:
        ticket_price = ticket_price-100
    else:
        ticket_price = ticket_price
print("your name", name)
print("your age", age)
print("your ticket price", ticket_price)
print("your booking is sucessful")