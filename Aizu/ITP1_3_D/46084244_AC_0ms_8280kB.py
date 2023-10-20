x,y,z=map(int,input().split())



co=0
for i  in range(x,y+1):
    if(z%i==0):
        co+=1
        
print(co)