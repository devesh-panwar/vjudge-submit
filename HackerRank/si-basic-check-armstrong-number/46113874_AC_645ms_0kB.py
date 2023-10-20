def solve(n):
    num=n
    res=0
    while(n):
        rem=n%10
        res+=pow(rem,3)
        n//=10
        
    if(res==num):
        print('Yes')
    else:
        print('No')
n=int(input())

solve(n)