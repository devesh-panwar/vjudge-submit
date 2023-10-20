t=int(input())
while(t):
    x,y=map(int,input().split())
    t-=1
    if(1.07*x<y):
        print('NO')
    else:
        print('YES')