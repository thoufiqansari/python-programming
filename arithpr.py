def sumOfAP( N, A,D) : 
    sum = 0
    p =0
    while p< N : 
        sum = sum + A 
        A = A + D 
        p= p+ 1
    return sum
      

N=int(input())
A=int(input())
D=int(input())
print (sumOfAP(N, A, D)) 
