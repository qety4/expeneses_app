class Balance:
    def __init__(self):
        self.expenses=[]
        self.balance=0
        self.additions=[]
    def status(self):
        print(f'Your balance is at {self.balance}')
        print(f'Your expenses are {self.expenses}')
        print(f'your additions are {self.additions}')
    def add(self):
        while True:
            try:
                a=int(input('Enter addition to balance:'))
                self.balance += a
                b=str((input('Enter details of addition:')))
                self.additions.append([a,b])
                print(f'amount {a} added')
                print(f'your balance is at {self.balance}')
                print(f'your additions are {self.additions}')
                break
            except:
                print('Enter a valid number')
    def expense(self):
        while True:
            try:
                a=int(input('Eneter your expense:'))
                if a > self.balance:
                    print("exceeding current funds")
                else:
                    self.balance-=a
                    b=str(input('Enter details of expense: '))
                    self.expenses.append([a,b])
                    print(f'Your expenses are {self.expenses}')
                    print(f'Your balance is at {self.balance}')
                    break
            except:
                print('Enter a valid number')
