class BankAccount:
    #AccountNumber = Student
    #pin = 9625951674160
    #AccountName = Kesh
    # = 
    def __init__(self,accountNumber,accountName,pin):
        self.accountNumber = accountNumber
        self.accountName = accountName
        self.pin = pin
        
    def run (self):
        return  f"my {self.accountNumber }  is very long,my name is {self.accountName }, how can I be helped with the {self.pin}?"

    def deposit (self):
        return f"I am {self.accountName },my pin is {self.pin },and my account number is {self.accountNumber } please deposit on that account" 

    def withdraw (self):
        return f"I do have an account number and it's pin is {self.pin}"