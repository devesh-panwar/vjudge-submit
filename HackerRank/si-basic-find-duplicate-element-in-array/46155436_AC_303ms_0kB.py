n=int(input())
l=list(map(int,input().split()))

l.sort()

for x in range(len(l)-1):
    if(l[x]==l[x+1]):
        print(l[x])
        break