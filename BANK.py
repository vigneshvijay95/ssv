# bank account details process by using class,function,if or else conditional loop.
class bank:
    def __init__(account):
        account.balance=0
        print("Hello welcome to the sbi bank")
    def deposit(account):
        amount = float(input("Enter amount to be deposited:"))
        if amount>=100000:
            print("Not to deposit in ur account amount is huge")
        elif amount<100000:
            account.balanace +=amount
            print("\n amount deposited:",amount)
    def withdraw(account):
        amount = float(input("Enter amount to be withdraw:"))
        if account.balance>=amount:
            account.balance-=amount
            print("\n you having the balance:",amount)
            else:
                print("\n insufficient balance:",amount)
    def balance(account):
        print("\n account balance=",account.balance)
if __name__ == "__main__":
    a = Bank_account()
    a.deposit()
    a.withdraw()
    a.balance()


