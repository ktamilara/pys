r1,s1=map(int,input().split())
l1=list(map(int,input().split()))
r1=[]

l1.insert(0,0)
for x in range(s1):
     q1=[]
     sums=0
     c1,d1=map(int,input().split())
     for i in range(c1,d1+1):
         
         sums^=l1[i]
     
     r1.append(sums)
for x in r1:
    print(x)
