t = int(input())
while(t):
    t-=1
    x,y=map(int,input().split())
    l=list(map(int,input().split()))
    c=0
    for x in l:
        if(x>y):
            c+=1
            
    print(c)