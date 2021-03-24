import random
class Account:
    print("WELCOME TO SBI ATM")
    print("please wait your transaction:")
    #accountObj 
    
    def __init__(self, id, balance = 0, annualInterestRate = 1.4,):
            self.id = id
            self.balance = balance
            self.annualInterestRate = annualInterestRate
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
    accountObj = None
    for i in range(1000, 9999):
        account = Account(i, 0)
        accounts.append(account)
    #return accounts
    while True:
        id = getPin()
        for acc in accounts:
            if acc.getId() == id:
                accountObj = acc
                break
        while True:
            print("\n1 - View Balance \t 2 - Withdraw \t 3 - Deposit \t 4 - Exit ")
            option = int(input("\nEnter your selection: "))
            isExit = process(option,accountObj)
            if isExit:
                break

def process(option,accountObj):
    isExit = False
    if option == 1:
        viewbalance(accountObj)
    elif option == 2:
        withdraw(accountObj)
    elif option == 3:
        deposit(accountObj)
    elif option == 4:
        exit1(accountObj)
        isExit = True
    else:
        print("invalid option")
    return isExit
def getPin():
  pin = int(input("\nEnter account Pin: "))  
  while pin < 1000 or pin > 9999:
    pin = int(input("\nInvalid Pin.. Re-enter : "))
  return pin


def viewbalance(accountObj):
    print(accountObj.getBalance())
    return

def withdraw(accountObj):
    #if selection == 2:
        amt = float(input("\nEnter amount to withdraw: "))
        ver_withdraw = input("Is this the correct amount, Yes or No ? " + str(amt) + " ")
        if ver_withdraw == "Yes" or ver_withdraw == "yes":
            print("Verify withdraw")
            if amt < accountObj.getBalance():
                accountObj.withdraw(amt)
                print("\nUpdated Balance: " + str(accountObj.getBalance()) + " \n")
            else:
                print("\nYou're balance is less than withdrawl amount: " + str(accountObj.getBalance()) + " \n")
                print("\nPlease make a deposit.")
      
 
def deposit(accountObj):
    #if  selection == 3:
        amt = float(input("\nEnter amount to deposit: "))
        ver_deposit = input("Is this the correct amount, Yes, or No ? " + str(amt) + " ")
        if ver_deposit == "Yes" or ver_deposit == "yes":
            accountObj.deposit(amt)
            print("\nUpdated Balance: " + str(accountObj.getBalance()))

def exit1(accountObj):
   # if  selection == 4:
        print("nTransaction is now complete.")
        print("Transaction number: ", random.randint(10000, 1000000))
        print("Current Interest Rate: ", accountObj.annualInterestRate)
        print("Monthly Interest Rate: ", accountObj.annualInterestRate / 12)
        print("Thanks for choosing us as your bank")
    #else:
    #    print("nThat's an invalid choice.")
if __name__ == "__main__":
    main()
    #deposit()
    #pin()
    #withdraw()
    #exit1()