t = int(input())

p=t
sum=0
mul=1
while(p):
    rem=p%10
    mul*=rem
    sum+=rem
    p//=10
    
print(sum,mul)