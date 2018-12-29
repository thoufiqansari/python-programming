s = "~`!@#$%^&*()_-+={}[]:>;',</?*-+"
n =str(input())
m=0
for i in n:
    if i in s:
        m+=1
print(m)
