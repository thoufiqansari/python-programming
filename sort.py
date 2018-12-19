k=int(input())
x=k
lst =raw_input()
lst =[int(k) for k in lst.split(' ')]
lst.sort()
for k in range(len(lst)): 
    print(lst[k]) 
    print(" ")
