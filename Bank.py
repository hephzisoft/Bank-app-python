import sys
import datetime
import random


class Bank:
    firstName = None
    secondName = None
    middleName = None
    mainBalance = 0.0
    age = None
    gender = None
    phone_number = None
    pin = None
    input_num = 0
    input_trail = 3
    full_name = f"{firstName} {secondName} {middleName}"
    account_number = random.randint(1000000000, 9999999999)
    time = datetime.datetime.now()
    real_time = time.strftime("%d-%a-%b-%Y at %H:%M:%S %p")

    def account_opening(self):
        self.firstName = input("First Name: ").capitalize()
        self.secondName = input("Second Name: ").capitalize()
        self.middleName = input("Middle Name: ").capitalize()
        self.full_name = f"{self.firstName} {self.secondName} {self.middleName}"
        while True:
            self.age = input("Age: ")
            try:
                validate_age = int(self.age)

                if validate_age > 5:
                    break
                elif self.input_num == self.input_trail:
                    print("""
Sorry the program got terminated
Thanks for using Hephzi Bank.
                                    """)
                    sys.exit()
                else:
                    print(f'You have {self.input_trail} chances')
                    print("Age should be greater than 5")
            except ValueError:
                print(f'You have {self.input_trail} chances')
                print("Age should be a number")
            self.input_trail -= 1
        self.input_trail = 3
        while True:
            self.gender = input("Gender: ").capitalize()
            if self.gender == "Male" or self.gender == "Female":
                break
            elif self.input_num == self.input_trail:
                print("""
Sorry the program got terminated
Thanks for using Hephzi Bank.
                                """)
                sys.exit()
            else:
                print(f'You have {self.input_trail} chances')
                print("Gender must be male or female")

            self.input_trail -= 1
        self.input_trail = 3
        while True:
            self.phone_number = input("Phone Number: ")
            if len(self.phone_number) == 11:
                try:
                    validate_phone_number = int(self.phone_number)
                    break
                except ValueError:
                    print(f'You have {self.input_trail} chances')
                    print("Age should be a number")

            if self.input_num == self.input_trail:
                print("""
             Sorry the program got terminated
            Thanks for using Hephzi Bank.
                                                            """)
                sys.exit()
            else:
                print(f'You have {self.input_trail} chances')
                print("Phone number should be 11 digits")
            self.input_trail -= 1
            self.input_trail = 3
        print("""
Your Account is pending to be verified 
==========================
You have been verified
    """)
        self.intro()

    def intro(self):
        print(f"""
Your Details are:
Name: {self.full_name}
Age: {self.age}
Gender: {self.gender}
Phone Number : {self.phone_number}
Account Number: {self.account_number}
Account Balance: ${self.mainBalance}
=========================
Create a pin that will be used for all transactions
        """)
        self.create_pin()
        print("Money has to be added to the account")
        self.deposit()
        while True:
            select = (input("""
1. Deposit 
2. Transfer
3. Change pin
4. Check Account Information  
"""))

            try:
                valid_select = int(select)
                if valid_select == 1:
                    self.deposit()
                elif valid_select == 2:
                    self.transfer()

                elif valid_select == 3:
                    self.change_pin()

                elif valid_select == 4:
                    self.check_account_information()

                else:
                    print("Invalid option")
            except ValueError:
                print("Invalid input")

    def create_pin(self):
        while True:
            self.pin = input("Create pin: ")
            confirm_pin = input("Confirm pin: ")
            if len(self.pin) == 4:
                try:
                    new_pin = int(self.pin)
                    confirm = int(confirm_pin)
                    if new_pin == confirm:
                        print("Creating pin ..............")
                        print("Pin Created")
                        print(f"Your pin is {confirm}")
                        break
                    else:
                        print("Pin do not match")
                except ValueError:
                    print("Your pin should be 4digit not alphabets or alphanumeric")

            else:
                print("Your pin should be 4 digits")

    def change_pin(self):
        while True:
            old_pin = input("Enter Old pin: ")
            new_pin = input("Enter New pin: ")
            confirm_pin = input("Confirm  New pin: ")

            if len(old_pin) == 4:
                try:
                    confirm_old_pin = int(old_pin)
                    confirm_new_pin = int(new_pin)
                    confirming = int(confirm_pin)
                    if self.pin == old_pin and confirming == confirm_new_pin and confirm_old_pin != confirming:

                        print("Changing pin ..............")
                        print("Pin Changed")
                        print(f"Your pin is {confirming}")
                        self.pin = new_pin
                        break
                    elif self.input_num == self.input_trail:
                        print("Sorry this process is terminated")
                        break
                    else:
                        print(f'You have {self.input_trail} chances')
                        print("Pin do not match or Pin is the same as the old one")
                except ValueError:
                    print(f'You have {self.input_trail} chances')
                    print("Your pin should be 4digit not alphabets or alphanumeric")

            else:
                print(f'You have {self.input_trail} chances')
                print("Your pin should be 4 digits")
            self.input_trail -= 1

    def deposit(self):
        while True:
            amount = input("Amount: ")

            try:
                valid_amount = float(amount)
                break
            except ValueError:
                print("Amount should be in digits")

        new_balance = valid_amount + self.mainBalance
        while True:
            validate_pin = input("Pin: ")
            try:
                validate = int(validate_pin)
                if validate_pin == self.pin:
                    print("Pin ok")
                    break
                elif self.input_num == self.input_trail:
                    print("Sorry this process has been terminated")
                    sys.exit()
                else:
                    print(f'You have {self.input_trail} chances')
                    print("Pin is wrong")

            except ValueError:
                print(f'You have {self.input_trail} chances')
                print("Your pin should be 4digit not alphabets or alphanumeric")
            self.input_trail -= 1
        self.mainBalance = new_balance
        print(f"""
Money has been successfully added  ....
Amount sent: {amount}
Account Balance: {self.mainBalance}
Account Name: {self.full_name} 
Account No: {self.account_number}
Date: {self.real_time}
        """)

    def transfer(self):
        bank_name = input("Bank Name: ").capitalize()
        sender_name = input("Sender Name: ").capitalize()
        while True:
            amount = input("Amount: ")

            try:
                valid_amount = float(amount)
                break
            except ValueError:
                print("Amount should be in digits")
        while True:
            sender_account_no = input("Sender Account No: ")
            if len(sender_account_no) == 10:
                try:
                    validate_sender_account_no = int(sender_account_no)
                    break
                except ValueError:
                    print("Account number must be digits and not alphabets")
            else:
                print("Account Number must be 10 digits")
        new_balance = self.mainBalance - valid_amount
        self.mainBalance = new_balance
        while True:
            validate_pin = input("Pin: ")
            try:
                validate = int(validate_pin)
                if validate_pin == self.pin:
                    print("Pin ok")
                    break
                elif self.input_num == self.input_trail:
                    print("Sorry this process has been terminated")
                    sys.exit()
                else:
                    print(f'You have {self.input_trail} chances')
                    print("Pin is wrong")

            except ValueError:
                print(f'You have {self.input_trail} chances')
                print("Your pin should be 4digit not alphabets or alphanumeric")
            self.input_trail -= 1
        print(f"""
Money has been successfully sent  .... 
Amount sent: {amount}
Account Balance: {self.mainBalance}
Receiver Name: {sender_name} 
Receiver Bank: {bank_name}
Receiver Account No: {sender_account_no}
Date: {self.real_time}
""")

    def check_account_information(self):
        print(f"""
Your Details are:
Name: {self.full_name}
Age: {self.age}
Gender: {self.gender}
Phone Number : {self.phone_number}
Account Number: {self.account_number}
Account Balance: ${self.mainBalance}
Bank Name: Hephzi Bank
                """)
