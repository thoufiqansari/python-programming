n=int(input())
p=int(input())
for i in range(n,p+1):
  order=len(str(i))
  s=0
  temp=i
  while temp>0:
    d=temp%10
    s+=d**order
    temp//=10
  if(i==s):
    print(i)
