p = "~`!@#$%^&*()_-+={}[]:>;',</?*-+."
n =str(input())
m=0
for i in n:
    if i in p:
        m+=1
print(m)
