class bank:

    def __init__(self,account_no,holder_name,balance,deposit,withdrawl,checkbalance):
        self.account_no =account_no
        self.holder_name = holder_name
        self.balance = balance
        self.deposit = deposit
        self.withdrawl = withdrawl
        self.checkbalance = checkbalance

    def display_det(self):
        print(f"Account No-{self.account_no}")
        print(f"Holder-Name-{self.holder_name}")
        print(f"Balance-{self.balance}")
    
    def display_deposit(self):
        print(f"Deposit-{self.deposit}")
    
    def display_withdrawl(self):
        print(f"Withdrawl-{self.withdrawl}")
    
    def display_checkbalance(self):
        print(f"Check-Balance-{self.checkbalance}")

emp_det = bank(1234567890,"Hitesh",1000,1500,500,1000)

emp_det.display_det();
emp_det.display_deposit();
emp_det.display_withdrawl();
emp_det.display_checkbalance();


