class Person:
    
    def GetPerson(self):
        self.__name=input('enter your name')
        self.__age=input('enter your age')
    def PutPerson(self):
        print(self.__name,self.__age)


P1=Person
P1.PutPerson()
P1.GetPerson()


