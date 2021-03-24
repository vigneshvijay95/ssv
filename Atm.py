import random
class Account:
    print("WELCOME TO SBI ATM")
    print("please wait your transaction:")
    accounts = []
    #accountObj 
    
    def __init__(self, id, balance = 0, annualInterestRate = 1.4,):
            self.id = id
            self.balance = balance
            self.annualInterestRate = annualIntersestRate
        #self.account = account
 
    def getId(self):
        return self.id
 
    def getBalance(self):
        return self.balance
 
    def getAnnualInterestRate(self):
        return self.annualInterestRate
 
    def getMonthlyInterestRate(self):
        return self.annualInterestRate / 12
 
    def withdraw(self, amount):
        self.balance -= amount
 
    def deposit(self, amount):
        self.balance += amount
 
    def getMonthlyInterest(self):
        return self.balance * self.getMonthlyInterestRate()
def main():
   # Creating accounts
    accounts = []
    for i in range(1000, 9999):
        account = Account(i, 0)
        accounts.append(account)
        return accounts
def pin():

    while True:
        id = int(input("\nEnter account pin: "))
        while id < 1000 or id > 9999:
            id = int(input("\nInvalid Id.. Re-enter: "))
        while True:
            print("\n1 - View Balance \t 2 - Withdraw \t 3 - Deposit \t 4 - Exit ")
            selection = int(input("\nEnter your selection: "))
 
            for acc in accounts:
                if acc.getId() == id:
                    accountObj = acc
                    break
        return selection
def viewbalance():
    if  selection == 1:
        print(accountObj.getBalance())
        return 
def withdraw():
    if selection == 2:
        amt = float(input("\nEnter amount to withdraw: "))
        ver_withdraw = input("Is this the correct amount, Yes or No ? " + str(amt) + " ")
        if ver_withdraw == "Yes":
            print("Verify withdraw")
        else:
            break
        if amt < accountObj.getBalance():
            accountObj.withdraw(amt)
            print("\nUpdated Balance: " + str(accountObj.getBalance()) + " n")
        else:
            print("\nYou're balance is less than withdrawl amount: " + str(accountObj.getBalance()) + " n")
            print("\nPlease make a deposit.")
        
 
def deposit():
    if  selection == 3:
        amt = float(input("\nEnter amount to deposit: "))
        ver_deposit = input("Is this the correct amount, Yes, or No ? " + str(amt) + " ")
        if ver_deposit == "Yes":
            accountObj.deposit(amt)
            print("\nUpdated Balance: " + str(accountObj.getBalance()) + " n")
        else:
            break
def exit1():
    if  selection == 4:
        print("nTransaction is now complete.")
        print("Transaction number: ", random.randint(10000, 1000000))
        print("Current Interest Rate: ", accountObj.annualInterestRate)
        print("Monthly Interest Rate: ", accountObj.annualInterestRate / 12)
        print("Thanks for choosing us as your bank")
        exit()
    else:
        print("nThat's an invalid choice.")
if __name__ == "__main__":
    Acc = Accounts()
    deposit()
    pin()
    withdraw()
    exit1()