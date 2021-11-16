class Matrix:
    def Get(self,row,col):
        self.__M=[]
        for i in range(row):
            C=[]
            for j in range(col):
                C.append(int(input("Enter Value [{}][{}]:".format(i,j))))
            self.__M.append(C)
    def Put(self):
         for r in self.__M:
             for c in r:
                 print(c,end=' ')
             print()
    def __add__(self, T):
        R=Matrix()
        R.__M=[]
        for i in range(len(self.__M)):
            C=[]
            for j in range(len(self.__M[i])):
                C.append(self.__M[i][j]+T.__M[i][j])
            R.__M.append(C)
        return R

M1=Matrix()
M1.Get(3,3)
M1.Put()
M2=Matrix()
M2.Get(3,3)
M2.Put()
M3=M1+M2
M3.Put()




