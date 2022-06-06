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
                break
            #  to terminate
            elif self.input_num == self.input_trail:
                print("""
Sorry the program got terminated
Thanks for using Hephzi Bank.
                                                """)
                sys.exit()
            else:
                print(f'You have {self.input_trail} chances')
                print("Phone number should be 11 digits e.g 09012345678")

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
        self.deposit()
        self.transfer()

    def create_pin(self):
        while True:
            self.pin = input("Create pin: ")
            confirm_pin = input("Confirm pin: ")
            if len(self.pin) == 4:
                try:
                    new_pin = int(self.pin)
                    confirm = int(confirm_pin)
                    if new_pin == confirm:
                        print("Pin Created")
                        print("Creating pin ..............")
                        print(f"Your pin is {confirm}")
                        break
                    else:
                        print("Pin do not match")
                except ValueError:
                    print("Your pin should be 4digit not alphabets or alphanumeric")

            else:
                print("Your pin should be 4 digits")

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
                else:
                    print("Pin is wrong")

            except ValueError:
                print("Your pin should be 4digit not alphabets or alphanumeric")

        self.mainBalance = new_balance
        print(f"""
Money has been successfully added  ....
Amount sent: {amount}
Account Balance: {self.mainBalance}
Account Name: {self.full_name} 
Account No: {self.account_number}
Date: {self.time}
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
                print("Account Number must be 11 digits")
        new_balance = self.mainBalance - valid_amount
        self.mainBalance = new_balance
        while True:
            validate_pin = input("Pin: ")
            try:
                validate = int(validate_pin)
                if validate_pin == self.pin:
                    print("Pin ok")
                    break
                else:
                    print("Pin is wrong")

            except ValueError:
                print("Your pin should be 4digit not alphabets or alphanumeric")
        print(f"""
Money has been successfully sent  ....
Amount sent: {amount}
Account Balance: {self.mainBalance}
Receiver Name: {sender_name} 
Receiver Bank: {bank_name}
Receiver Account No: {sender_account_no}
Date: {self.time}
""")
