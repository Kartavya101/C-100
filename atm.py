class Atm:
    def __init__(self,cardNumber,pin):
        self.cardnumber = cardNumber
        self.pin = pin

    def withdrawl(self,amount):
        new_amount = 50000 - amount
        print("you have withdrawn "+str(amount) +". Your remaining balance is "+ str(new_amount))
    
    def check_balance(self):
        print("Your balance is 10,00,000")

def main():
    Card_number = input("insert your card number: ")
    pin_number  = input("enter your CVV: ")

    new_user =  Atm(Card_number ,pin_number)

    print("Choose your activity ")
    print("1.Check Balance   2.Withdrawl")
    activity = int(input("enter password: "))

    if (activity == 1):
        new_user.check_balance()
    elif (activity == 2):
        amount = int(input("enter the amount you want to withdraw!: "))
        new_user.withdrawl(amount)
    else:
        print("you dont have that much money lol")


if __name__ == "__main__":
    main()