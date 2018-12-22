p,q=map(int,input().split(" "))
m,n=map(int,input().split(" "))
if(p<m or q<n):
    x=m-p
    y=n-q
    print("%d %d" % (x,y))
else:    
    x=p-m
    y=q-n
    print("%d %d" % (x,y))
