class Distance:
    def GetDist(self):
        self.__k=int(input("Enter the kms:"))
        self.__m=int(input("Enter the metres:"))
        self.__c=int(input("Enter the cms:"))
    def PutDist(self):
        print(self.__k,self.__m,self.__c)
    def PutResult(self):
        print("{}:{}:{}".format(self.__k,self.__m,self.__c))

    def __add__(self,T):
        R=Distance()
        R.__k=self.__k+T.__k
        R.__m=self.__m+T.__m
        R.__c=self.__c=T.__c


        R.__k=R.__k+R.__m//1000
        R.__m=R.__m%1000

        R.__m=R.__m+R.__c//100
        R.__c=R.__c%100

        return R

D1=Distance()
D2=Distance()
D1.GetDist()
D2.GetDist()
D1.PutDist()
D2.PutDist()
D3=D1+D2
D3.PutResult()

