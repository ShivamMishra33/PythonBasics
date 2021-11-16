class Employees:
    def GetEmp(self):
        self.__ID=input("enter the ID:")
        self.__Name=input("Enter the name:")
        self.__Salary = float(input("Enter the Salary:"))

    def PutEmp(self):
        print(self.__ID,self.__Name,self.__Salary)

    def GetSal(self):
        return self.__Salary

class Perks(Employees):
    def GetPerks(self):
        self.GetEmp()


    def DA(self):
        return 0.35*self.GetSal()
    def HRA(self):
        return(0.16*self.GetSal())
    def PF(self):
        return(0.12*self.GetSal())
    def Net(self):
        return(self.GetSal()+0.35*self.GetSal()+0.16*self.GetSal()-0.12*self.GetSal())
    def PutPerks(self):
        print("Salary of the employee is:",self.GetSal())
        print("DA is:",self.DA())
        print("HRA is:",self.HRA())
        print("PF is:",self.PF())
        print("Net Salary is:",self.Net())

class NetSalary(Perks):
    def GetNetSal(self):
        self.GetPerks()
        self.PutPerks()


S=NetSalary()
S.GetNetSal()



