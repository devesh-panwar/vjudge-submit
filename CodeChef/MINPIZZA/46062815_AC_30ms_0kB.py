t=int(input())

while(t):
    t-=1
    x,y=map(int,input().split())
    
    ans=(x*y)//4
    if((x*y)%4):
        ans+=1
        
    print(ans)