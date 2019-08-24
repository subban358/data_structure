def heapify(arr,n,i):
    m = i
    l = 2*i+1
    r = 2*i+2
    if l<n and arr[l] < arr[i]:
        m = l
    if r<n and arr[r] < arr[m]:
        m = r    
    if m != i:    
        arr[i],arr[m] = arr[m],arr[i]
        heapify(arr,n,m)    

def heapSort(l,n):
    for i in range(n-1,-1,-1):
        heapify(l,n,i)
    for i in range(n-1, -1, -1): 
        l[i], l[0] = l[0], l[i]    
        heapify(l, i, 0)
if __name__ == "__main__":
    l = [12,11,13,5,6,7]
    n = len(l)
    heapSort(l,n)    
    print(l)