k=int(input())
Array =raw_input()
Array =[int(k) for k in Array.split(' ')]
low = 0
up = len(Array) - 1

def partition(Array,low,up):
    i = low+1
    j = up
    pivot = Array[low]
    while(i<=j):
        while(Array[i]<pivot and i<up):
            i = i+1
        while(Array[j]>pivot):
            j = j-1
        if(i<j):
            Array[i],Array[j] = Array[j],Array[i]
            i = i+1
            j = j-1
        else:
            i = i+1
    Array[low] = Array[j]
    Array[j] = pivot
    return j
 
def quick(Array,low,up):
    if(low>=up):
        return
    piv_loc = partition(Array,low,up)
    quick(Array,low,piv_loc-1)
    quick(Array,piv_loc+1,up)
 
quick(Array,low,up)
 
for i in Array:
    print i,
