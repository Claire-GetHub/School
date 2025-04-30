class BankAccount:
    def __init__(self, account_number, balance=0):
        self.account_number = account_number
        self.balance = balance
    
    def deposit(self, amount):
        self.balance += amount
        return f"Deposited {amount}. New balance: {self.balance}"

    def withdraw(self, amount):
        if amount > self.balance:
            return "Insufficient funds"
        self.balance -= amount
        return f"Withdrew {amount}. New balance: {self.balance}"

class SavingsAccount(BankAccount):
    def __init__(self, account_number, balance=0, interest_rate=0.02):
        super().__init__(account_number, balance)
        self.interest_rate = interest_rate
    
    def add_interest(self):
        interest = self.balance * self.interest_rate
        self.balance += interest
        return f"Interest added: {interest}. New balance: {self.balance}"

class CheckingAccount(BankAccount):
    def __init__(self, account_number, balance, fee = .50):
        super().__init__(account_number, balance)
        self.fee = fee

    # def withdraw(self, amount):
    #     if amount + amount * self.fee > self.balance:
    #         return "Insufficient funds"
    #     self.balance -= amount
    #     self.balance -= amount * self.fee
    #     return f"Withdrew {amount}. New balance: {self.balance}"
    
    def withdraw(self, amount):
        if (amount_and_fee := amount + amount * self.fee) > self.balance:
            return "Insufficient funds"
        
        return super().withdraw(amount_and_fee)



checking = CheckingAccount("SA123", 1000)
print(checking.charge(50))  
