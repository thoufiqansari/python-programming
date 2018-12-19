
k=int(input())
x=k
lst =raw_input()
lst = [int(k) for k in lst.split(' ')]
lst.sort()
median=0


if(((int(k)%2))==0):
    median= (lst[int((x/2)-1)] + lst[int(x/2)])/2
 else:
    median=(lst[x//2])
    
print (median)
