class TollRoad:
    def GetV(self):
        self.__VID=input("Enter the VID:")
        self.__VName=input("Enter the vehicle name:")
    def PutV(self):
        print(self.__VID,self.__VName)

class Vtype(TollRoad):
    __tollcollect=0
    def GetVtype(self):
        self.GetV()
        self.__type=("enter the vehicle type(HV,LV,GV):")
    def PutVtype(self):
        self.PutV()
        if(self.__type=="LV"):
            self.__toll=50
            print(self.__toll)
        elif(self.__type=="HV"):
            self.__toll=200
            print(self.__toll)
        elif(self.__type=="GV"):
            self.__toll=0
            print(self.__toll)
        else:
            print("Enter a valid Vehicle type.......")

class Collection(Vtype):
    def Collection(self):
        while (True):
            self.GetVtype()
            ch=input("Do you want to enter another vehicle info?? Press Y to Continue...")
            if(ch=="n")
                break



    def Total(self):

