class Matrix:
    def put(self,row,col):
        self.__M=[]
        for i in range(row):
            c=[]
            for j in range(col):
                c.append(int(input("enter the values [{}][{}]:".format(i,j))))
            self.__M.append(c)

    def get(self):
        for r in self.__M:
            for c in r:
                print(c,end=" ")
            print()


    def __add__(self,T):
        R=Matrix()
        R.__M=[]
         for m in range(len(self.__M)):
             C=[]
            for n in range(len(self.__M[m])):
                C.append(self.)



M1=Matrix()
M1.put(3,3)
M1.get()
M2=Matrix()
M2.put(3,3)
M2.get()
M3=M1*M2
M3.get()
