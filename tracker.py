from expense_tracker import Balance
import pickle
import os
operations=['s','a','e','c']
def close():
   with open('data.pickle','wb') as file:
       pickle.dump(balance,file)
if __name__=='__main__':
    if not os.path.exists('data.pickle'):
        balance=Balance()
    else:
        with open('data.pickle','rb')as file:
            balance=pickle.load(file)
    while True:
        a=''
        while a not in operations:
            a=input('Choose operation: s-status a-add e-expense c-close')
        if a=='s':
            balance.status()
        if a=='a':
            balance.add()
        if a=='e':
            balance.expense()
        if a=='c':
            close()
            break