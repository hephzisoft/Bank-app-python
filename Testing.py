pinno=123456789

flag=True

enter_pin=int(input("Enter your pin number: "))
while flag:
    if enter_pin!=pinno:
       if enter_pin<0:
        print("Your have entered a wrong pin")
        break
       print("Your Pin no incorrect")
       enter_pin=int(input("RE-Enter your pin number: "))
    else:
        print("Your Have Access ATM ")
        break