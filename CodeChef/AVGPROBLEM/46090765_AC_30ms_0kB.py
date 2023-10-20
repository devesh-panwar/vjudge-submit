n=int(input())

while(n):
    n-=1
    x,y,z=map(int,input().split())
    if((x+y)/2>z):
        print('YES')
    else:
        print('NO')