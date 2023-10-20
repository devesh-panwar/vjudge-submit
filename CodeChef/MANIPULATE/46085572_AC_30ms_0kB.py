t=int(input())
while(t):
    x,y=map(int,input().split())
    t-=1
    if(x>=y):
        print('YES')
    else:
        print('NO')