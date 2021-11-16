class Bank:
    def GetInfo(self):
        self.__acno = input('enter your account no')
        self.__name = input('enter your name')
        self.__balance = input('enter your balance')

    def ShowInfo(self):
        print('your acno is:', self.__acno)
        print('your name is:', self.__name)
        print('your available balance is:', self.__balance)
        print()

    def Search(self,acno):
        if(acno==self.__acno):
            return True
        else:
            return False

    def Deposit(self,d):
        self.__balance= d + self.__balance

    def Withdraw(self,w):
        if(self.__balance > d):
            self.__balance = self.__balance-d
        else:
            print('withdrawl not possible,balance is less...')



while(True):
 print('Menu')
 print('1.Add New Customer')
 print('2.Display all customer')
 print('3.Search by acno.')
 print('4.Deposit')
 print('5.Withdrawl')
 print('6.Exit')
 choice = int(input('Enter your choice number:'))
 L = list()
 if (choice==1):

  while(True):
    b = Bank()
    b.GetInfo()
    L.append(b)
    ch = input('Do you want to enter another ac no??')
    if (ch=='n'):
     break

 elif (choice==2):
    for x in L:
        x.ShowInfo()

 elif (choice==3):
    acno=int(input('enter the acno you want to search:'))
    found = False
    for x in L:
        found =x.Search(acno)
        if(found):
            x.ShowInfo()
        if(not found):
            print('acno doesnot exist.....',acno)


 elif (choice==4):
    acno = int(input('enter the acno into which you want to deposit your money..'))
    found = False
    for x in L:
        found = x.Search(acno)
        if (found):
            x.ShowInfo()
            d = int(input('enter the amount you want to deposit'))
            x.Deposit(d)
            x.ShowInfo()
        if (not found):
            print('acno doesnot exist.....', acno)


 elif (choice==5):
    acno = int(input('enter the acno from which you want to withdraw money..'))
    found = False
    for x in L:
        found = x.Search()
        if (found):
            x.ShowInfo()
            w = int(input('enter the amount you want to withdraw'))
            x.Withdraw()
            x.ShowInfo()
        if (not found):
            print('acount doesnot exist',acno)

 elif (choice==6):
     break