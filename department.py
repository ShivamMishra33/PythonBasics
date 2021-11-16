from abc import ABC,abstractmethod
class Dept(ABC):
    @abstractmethod
    def Get(self):
        pass
    @abstractmethod
    def Put(self):
        pass

class Perm(Dept):
    def Get(self):
        self._ID=input("Enter the id:")
        self._Name=input("Enter the name:")
        self._Sal=int(input("Enter the salary:"))


    def Sal(self):
        self._da=self.Sal()*0.25
        self._hra=self.Sal()*0.30
        self._totsal=self._Sal+self._da+self._hra


    def Put(self):
        print("ID-",self._ID,"Name-",self._Name)
        print("Salary-",self._Sal,"DA-",self._da,"HRA-",self._hra,"Total Salary-",self._totsal)

class Temp(Dept):
    def Get(self):
        self._ID = input("Enter the id:")
        self._Name = input("Enter the name:")
        self._Sal = int(input("Enter the salary:"))
    def Put(self):
        print("ID-", self._ID, "Name-", self._Name)
        print("Salary-", self._Sal)