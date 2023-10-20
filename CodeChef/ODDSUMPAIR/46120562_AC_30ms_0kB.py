t=int(input())
co=0
while(t):
    t-=1
    x,y,z=map(int,input().split())
    if((x+y)%2==1 or (y+z)%2==1 or (x+z)%2==1):
        print('Yes')
    else:
        print('No')