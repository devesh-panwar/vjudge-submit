n=int(input())
c=0
while(n):
    n-=1
    
    x,y,z=map(int,input().split())
    if((x==1 and y==1) or (x==1 and z==1) or (y==1 and z==1)):
        c+=1
        
print(c)