## Given an array ,you have to sort the array in the wave form
## a1>=a2<=a3>=a4<=a5.......

l=list(map(int,input().split()))

if(len(l)<3):

    print("NOT POSSIBLE")

else:

    l1=sorted(l)

    for i in range(1,len(l1),2):
        
        c=l1[i]
        l1[i]=l1[i-1]
        
        
        l1[i-1]=c
        

print(*l1)

        
