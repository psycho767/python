class bank:

    def __init__(self,account_no,holder_name,balance):
        self.account_no =account_no
        self.holder_name = holder_name
        self.balance = balance

    def display_det(self):
        print(f"Account No-{self.account_no}")
        print(f"Holder-Name-{self.holder_name}")
        print(f"Balance-{self.balance}")
    
    def display_deposit(self,deposit):
        self.balance +=deposit
        print(f"Deposit-{deposit}")
    
    def display_withdrawl(self,withdrawl_amt):
        self.balance -=withdrawl_amt
        print(f"Withdrawl-{withdrawl_amt}")
    
    def display_checkbalance(self):
        print(f"Check-Balance-{self.balance}")

emp_det = bank(1234567890,"Hitesh",1000)


emp_det.display_det();
emp_det.display_deposit(2500);
emp_det.display_withdrawl(500);
emp_det.display_checkbalance();


