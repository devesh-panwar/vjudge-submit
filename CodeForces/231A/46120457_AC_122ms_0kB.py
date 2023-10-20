t=int(input())
co=0
while(t):
    t-=1
    x,y,z=map(int,input().split())
    if((x==1 and y==1) or (y==1 and z==1) or (x==1 and z==1)):
        co+=1
        
print(co)