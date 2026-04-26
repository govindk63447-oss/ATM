import data

def create():
    name = input("enter your name :") 
    print(f"CONGRATS !! YOU HAVE CREATED YOUR ACCOUNT.\n YOUR ACCOUNT NUMBER IS : {id(name)}")
    data.account_number.append(id(name))
    # print(data.account_number)
    data.customer_data.append(name)
    pin = int(input("Set your pin (in natural numbers only) :"))
    data.pin_data.append(pin)
    
    with open("customer_data.txt","w") as f:
        f.write(f"name = {name}, pin = {pin}")
