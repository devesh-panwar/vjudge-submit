t=int(input())
while(t):
    t-=1
    x=int(input())
    l=list(map(int,input().split()))
    
    m1=max(l)
    l.remove(m1)
    
    while(max(l)==m1):
        l.remove(m1)
        
    m2=max(l)
    print(m1+m2)