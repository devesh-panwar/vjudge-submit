t=int(input())
while(t):
    t-=1
    x,y=map(int,input().split())
    a=list(map(int,input().split()))
    b=list(map(int,input().split()))
    cost=0
    for i in range (len(a)):
        if(a[i]>=y):
            cost+=b[i]
            
    print(cost)