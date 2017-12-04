class Customer:
    name = 'Raj'
    balance = 100000

    def Debit(self, balance, amount):
        self.amount = amount
        self.balance = balance
        if amount<= balance:
            balance = balance - amount
            print("Thank you for the transaction. Your Balance is ", balance)
        else:
            print("Sorry! We can not process the transaction. Debit amount exceeds balance. Your current balance is ", balance)

    def Credit(self, balance, amount):
        self.amount = amount
        self.balance = balance
        balance = balance + amount
        print("Thank you for Depositing money. Your Balance is ", balance)

a = Customer()
amount = int(input("Enter money for transaction : "))
n = int(input("Enter 1 for depositing and 2 for withdrawal : "))
if(n==1):
    a.Credit(a.balance, amount)
else:
    a.Debit(a.balance, amount)

