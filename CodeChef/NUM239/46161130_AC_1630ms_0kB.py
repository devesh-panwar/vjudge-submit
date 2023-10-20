t=int(input())

while(t):
    t-=1
    x,y=map(int,input().split())
    c=0
    for i in range(x,y+1):
        st=str(i)
        if(st[-1]=='2' or st[-1]=='3' or st[-1]=='9' ):
            c+=1
            
    print(c)