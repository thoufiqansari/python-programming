p,q=map(int,input().split(" "))
m,n=map(int,input().split(" "))
if(p<m or q<n):
    a=m-p
    b=n-q
    print("a b-> %d %d" % (a,b))
else:    
    a=p-m
    b=q-n
    print("a b-> %d %d" % (a,b))
