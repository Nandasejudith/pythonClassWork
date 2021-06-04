class Account:
    #AccountNumber = Student
    #pin = 9625951674160
    #AccountName = Kesh
    # = 
    def __init__(self,name,phoneNumber, transaction):
        self.name = name
        self.phoneNumber = phoneNumber
        self.balance = 0
        self.transaction = transactionfee = 70
        self.loan =0
        self.loan_limit = 40000
        
    def deposit (self, amount):
        if amount <=0:
            return "Amount must be greater than Zero"
        else:
            self.balance+= amount
            return f"Dear {self.name} your {self.balance} is valid"
            
    def withdraw (self, withdraw_amount):
        total = withdraw_amount + self.transaction
        if withdraw_amount<=0:
            return "Input valid amount"
        elif total > self.balance:
            return "Insuficient balance"
        else:
            self.balance -= total
            return f"Hello {self.name} you have successfully withdrew {self.withdraw} account balance is {self.balance}"  

    def borrow (self,amount):
        if amount>=self.loan_limit:
            return f"you cannot be given a loarn"
        elif amount<0:
            return f"You can't borrow loan"
        elif self.loan>0:
            return f"you still have an existing loan"
        else:
            loan_fee = amount*0.06
            self.loan=loan_fee+amount
            return f"Hello {self.name} you have recieved {amount} and you will pay {self.loan}"        