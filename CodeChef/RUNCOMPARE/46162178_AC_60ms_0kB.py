t=int(input())
while(t):
    t-=1
    x=int(input())
    a=list(map(int,input().split()))
    b=list(map(int,input().split()))
    
    c=0
    for i in range(len(a)):
        if(not(b[i]>2*a[i] or a[i]>2*b[i])):
            c+=1
            
    print(c)