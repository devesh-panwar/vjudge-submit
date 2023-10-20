t=int(input())
co=0
ans=0
while(t):
    t-=1
    x,y=map(int,input().split())
    ans=(x*y)//4
    if((x*y)%4>0):
        ans+=1
        
    print(ans)
    ans=0