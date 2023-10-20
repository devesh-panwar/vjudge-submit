n=int(input())
c=0
while(n):
    n-=1
    x,y,z=map(int,input().split())
    if((x+y)%2==1 or (x+z)%2==1 or (y+z)%2==1):
        print('YES')
    else:
        print('NO')