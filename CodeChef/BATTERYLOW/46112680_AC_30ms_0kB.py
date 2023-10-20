def solve(a):
    if(a<=15):
        print('Yes')
    else:
        print('No')
t=int(input())
while(t):
    t-=1
    a=int(input())
    
    solve(a)