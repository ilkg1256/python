## Lab: 은행 계좌

class Account:
    def __init__(self):
        self.__balance = 0
    
    def withdraw(self, Amount):
        self.__balance -= Amount
        print(f"통장에 {Amount}가 입급되었음")
        return self.__balance
    
    def deposit(self, Amount):
        self.__balance += Amount
        print(f"통장에 {Amount}가 출금되었음")
        return self.__balance

Account1 = Account()

Account1.deposit(100)
Account1.withdraw(10)