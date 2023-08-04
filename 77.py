x=int(input())
flag=False
if x>1:
       for i in range(2,1000):
             if(x%i)==0:
                   flag=False

                

if flag:
        print(x,"is a prime")
else:
        print(x,"is not a prime ")

                
