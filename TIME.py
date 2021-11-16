class Time:
    def GetTime(self):
        self.__h=int(input("Enter  Hrs:"))
        self.__m = int(input("Enter  Min:"))
        self.__s= int(input("Enter  Second:"))
    def PutTime(self):
        print(self.__h,self.__m,self.__s)
    def  PutResult(self):
        print("Days {}     {}:{}:{}".format(self.__d,self.__h, self.__m, self.__s))
    def __add__(self, T):
        R=Time()
        R.__h=self.__h+T.__h
        R.__m=self.__m+T.__m
        R.__s=self.__s+T.__s

        R.__m=R.__m+(R.__s//60)
        R.__s=R.__s%60

        R.__h=R.__h+(R.__m//60)
        R.__m=R.__m%60

        R.__d=R.__h//24
        R.__h=R.__h%24

        return R
T1=Time()
T2=Time()
T1.GetTime()
T2.GetTime()
T1.PutTime()
T2.PutTime()
T3=T1+T2
T3.PutResult()






