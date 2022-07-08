"""
Problem: https://www.codingninjas.com/codestudio/problems/count-inversions_615
"""
def merge(ar1,ar2,n1,n2,cntInv):
    tarr = []
    i = 0
    j = 0
    while i<n1 and j<n2:
        if ar1[i] <= ar2[j]:
            tarr.append(ar1[i])
            i+=1
        else:
            tarr.append(ar2[j])
            cntInv += n1-i
            j+=1
    if i<n1:
        tarr += ar1[i:]
    else:tarr += ar2[j:]
    return tarr, cntInv
            

def mergeSort(arr,n,cntInv):
    if n<=1:return arr,cntInv
    mid = n//2
    arr[:mid],cntInv = mergeSort(arr[:mid],mid,cntInv)
    arr[mid:],cntInv = mergeSort(arr[mid:],n-mid,cntInv)
    arr[:],cntInv = merge(arr[:mid],arr[mid:],mid,n-mid, cntInv)
    return arr,cntInv


def getInversions(arr, n) :
    _ , ans = mergeSort(arr,n,0)
    return ans 
