n=int(input())

p=n
su=0
while(p):
    rem=p%10
    su+=pow(rem,3)
    p//=10
    
if(su==n):
    print('Yes')
else:
    print('No')