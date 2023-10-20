y=int(input())

h=int(y/(60*60))
m=(y-(60*60*h))//60
s=y-(60*60*h)-(60*m)

h=str(h)
m=str(m)
s=str(s)
print(h+':'+m+':'+s)