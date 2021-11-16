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

    def transpose(self):
        R=Matrix()
        R.__M=[]
        for m in range(len(self.__M)):
            c=[]
            for n in range(len(self.__M[m])):
                c.append(self.__M[n][m])
            R.__M.append(c)
        return R


M1=Matrix()
M1.put(3,3)
M1.get()
M1=M1.transpose()
M1.get()






