t=int(input())

while(t):
    t-=1
    x=int(input())
    
    ls=list(map(int,input().split()))
    mul=1
    for x in ls:
        mul*=x
        
    print(mul)