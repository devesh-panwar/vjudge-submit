a=set(map(int,input().split()))
n=int(input())
flag=True
while(n):
    n-=1
    b=set(map(int,input().split()))
    
    if(not (a.issuperset(b))):
       flag=False
       break
       
if(flag):
       print(flag)
else:
       print(flag)
       
       
       
        