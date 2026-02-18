balance=10000
correct_pin = 1234
print("welcome to ATM")
print("please insert the card")

card=input("enter 1, card inserted successfully and 2, insert card properly :")
if card=="1":
    print("card inserted successfully")

    print("select the languages")
    print("1.english, 2.kannada, 3.telugu")
    lang = input("enter the choice :")
    if lang=="1":
        print("continue with english")
        pin = int(input("enter your pin :"))
        if pin==correct_pin:
            print("select the options 1, balance enquiry and 2, to withdraw the money")
            choice = input("enter the choice :")
            if choice=="1":
                print("your balance is",balance)
            elif choice=="2":
                amount = int(input("enter the amount you want to withdraw :"))
                if amount%100==0:
                    if amount<=balance:
                        print("collect cash",amount)
                        print("your remaining balance is",balance)
                    else:
                        print("in sufficient balance")
                else:
                    print("withdraw amt is multiple of 100")
            else:
                print("thank you, please visit agin")
        else:
            print("enter the valid pin number")
    else:
        print("choose english only")
else:
    print("insert the card properly")