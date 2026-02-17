print("===== WELCOME TO MOBILE RECHARGE =====")

number = input("Enter your mobile number: ")

if len(number) == 10:
    print("Number Accepted")

    print("\nChoose the operator")
    print("1. Jio")
    print("2. Airtel")
    print("3. BSNL")

    op = int(input("Enter your option: "))

    # ---------------- JIO ----------------
    if op == 1:
        print("\nJio Plans")
        print("1. 199 for 1GB data")
        print("2. 300 for 2GB data")
        print("3. 400 for 3GB data")

        choice = input("Enter your choice: ")

        if choice == "1":
            print("₹199 Jio recharge successful")
        else:
            if choice == "2":
                print("₹300 Jio recharge successful")
            else:
                if choice == "3":
                    print("₹400 Jio recharge successful")
                else:
                    print("Invalid Plan")

    else:
        # ---------------- AIRTEL ----------------
        if op == 2:
            print("\nAirtel Plans")
            print("1. 299 for 1.5GB data")
            print("2. 359 for 2.5GB data")
            print("3. 400 for 3.5GB data")

            choice = input("Enter your choice: ")

            if choice == "1":
                print("₹299 Airtel recharge successful")
            else:
                if choice == "2":
                    print("₹359 Airtel recharge successful")
                else:
                    if choice == "3":
                        print("₹400 Airtel recharge successful")
                    else:
                        print("Invalid Plan")

        else:
            # ---------------- BSNL ----------------
            if op == 3:
                print("\nBSNL Plans")
                print("1. 100 for 1GB data")
                print("2. 200 for 2GB data")
                print("3. 300 for 3GB data")

                choice = input("Enter your choice: ")

                if choice == "1":
                    print("₹100 BSNL recharge successful")
                else:
                    if choice == "2":
                        print("₹200 BSNL recharge successful")
                    else:
                        if choice == "3":
                            print("₹300 BSNL recharge successful")
                        else:
                            print("Invalid Plan")

            else:
                print("Choose a valid operator")

else:
    print("Invalid mobile number")
