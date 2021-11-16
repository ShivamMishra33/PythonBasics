class Bank:
    def GetInfo(self):
        self.__acno = int(input('enter your account no..'))
        self.__name = input('enter your name..')
        self.__balance = int(input('enter your balance..'))

    def ShowInfo(self):
        print('your acno is:', self.__acno)
        print('your name is:', self.__name)
        print('your available balance is:', self.__balance)
        print()

    def search(self,ac_no):
        if(ac_no==self.__acno):
            return True
        else:
            return False

    def deposit(self):
        d=int(input('enter the amount you want to deposit..'))
        self.__balance= d + self.__balance

    def withdraw(self):
        w=int(input('enter the amount you want to withdraw..'))
        if(self.__balance > w):
            self.__balance = self.__balance-w
        else:
            print('withdrawl not possible,balance is less...')


customerdetails=[]
while(True):
 print('Menu')
 print('1.Add New Customer')
 print('2.Display all customer')
 print('3.Search by acno.')
 print('4.Deposit')
 print('5.Withdrawl')
 print('6.Exit')
 choice = int(input('Enter your choice number:'))

 if (choice==1):

  while(True):
    b = Bank()
    b.GetInfo()
    customerdetails.append(b)
    ch = input('Do you want to enter another ac no??')
    if (ch=='n'):
     break

 elif (choice==2):
    for x in customerdetails:
        x.ShowInfo()

 elif (choice==3):
    ac_no = int(input('enter the acno you want to search:'))
    fl = list(filter(lambda x  : x.search(ac_no) , customerdetails))
    if (len(fl) == 0):
         print('ac_no doesnot exist....')
    else:
        for i in fl:
            i.ShowInfo()

 elif (choice==4):
     ac_no = int(input('enter the acno into which you want to deposit:'))
     fl = list( filter (lambda x : x.search(ac_no), customerdetails) )
     if len(fl) == 0:
         print('acno doesnot exist....')
     else:
         for i in fl:
             i.deposit()
             i.ShowInfo()

 elif (choice==5):
     ac_no = int(input('enter the acno from which you want to withdraw :'))
     fl = list(filter(lambda x: x.search(ac_no), customerdetails))
     if (len(fl) == 0):
         print('acno doesnot exist....')
     else:
         for i in fl:
             i.withdraw()
             i.ShowInfo()



 elif (choice==6):
     break