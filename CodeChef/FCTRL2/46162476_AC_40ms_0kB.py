t=int(input())
while(t):
    t-=1
    x=int(input())
    fact=1
    if(x==1):
        print(1)
    else:
        while(x):
            fact*=x
            x-=1
            
        print(fact)