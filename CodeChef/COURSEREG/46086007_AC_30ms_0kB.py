t=int(input())
while(t):
    x,y,z=map(int,input().split())
    t-=1
    if(y>=x+z):
        print('Yes')
    else:
        print('No')