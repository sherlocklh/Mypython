class Caesar:  
    def __init__(self,a,b):#初始化，接受程序需要的类型  
        self.pass1=a  
        self.type1=b  
    def jiami(self,a):#加密的程序  
        z=(ord(a)-97+self.pass1)%26+97#用ascii码值来完成移动  
        return chr(z)  
    def jiemi(self,a):#解密的程序  
        z=(ord(a)-97-self.pass1)%26+97  
        if z<97:  
            z=z+26  
        return chr(z)  
    def show(self,x):#显示结果  
        str=''  
        if self.type1==0:#加密的时候进入  
            for i in range (len(x)):  
                x=x[:i]+self.jiami(x[i])+x[i+1:]  
            for i in range (len(x)):  
                str=str+x[i]  
            print (str)  
        else:#解密的时候进入  
            for i in range (len(x)):  
                x=x[:i]+self.jiemi(x[i])+x[i+1:]  
            for i in range (len(x)):  
                str=str+x[i]  
            print (str)  
if __name__=="__main__":#测试程序  
    a=int(input('please input the pass (小于26！0：结束):'))  
    while a:  
        b=int(input('please input the type （0：加密；1：解密:）'))  
        x=input('please input str:')  
        user=Caesar(a,b)  
        user.show(x)  
        a=int(input('please input the pass (小于26！0：结束):')) 