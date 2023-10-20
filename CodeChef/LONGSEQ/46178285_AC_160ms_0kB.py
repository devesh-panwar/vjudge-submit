t=int(input())
while(t):
    t-=1
    n=input()
    ze=0
    on=0
    orignal=n
    for x in n:
        if(x=='0'):
            ze+=1
        if(x=='1'):
            on+=1
    ans=False       
    if(on==1 or ze==1):
        if(on==1):
            st=n.replace('1','0',1)
           # print(n)
            if('0'*len(orignal)==st):
                ans=True
        else:
            st=n.replace('0','1',1)
            #print(n)
            if('1'*len(orignal)==st):
                ans=True
                
    if(ans):
        print('Yes')
    else:
        print('No')
            
            
            
            