t=int(input())

while(t):
    t-=1
    n1=int(input())
    l1=[]
#     for i in range(n1):
    l1=list(map(int,input().split()))
        
    
    l2=[]
    #for i in range(n1):
    l2=list(map(int,input().split()))
        
    c1=0
    an1=0
    for i in (l1):
        if(i!=0):
            c1+=1
        else:
            c1=0
        if(c1>an1):
            an1=c1
       # an1=max(an1,c1)
            
    c2=0
    an2=0
    for i in (l2):
        if(i!=0):
            c2+=1
        else:
            c2=0
        if(c2>an2):
            an2=c2
       # an2=max(an2,c2)
            
    if(an1>an2):
        print('Om')
    elif(an1==an2):
        print('Draw')
    else:
        print('Addy')