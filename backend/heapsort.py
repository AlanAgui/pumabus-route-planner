import math

def hIzq(i):
    return 2*i+1

def hDer(i):
    return 2*i+2

def intercambia(A,x,y):
    tmp=A[x]
    A[x]=A[y]
    A[y]=tmp

def maxHeapify(A,i,tamanoHeap):
    L=hIzq(i)
    R=hDer(i)
    if(L<=(tamanoHeap-1) and A[L]>A[i]):
        posMax=L
    else:
        posMax=i
    if(R<=(tamanoHeap-1) and A[R]>A[posMax]):
        posMax=R
    if(posMax != i):
        intercambia(A,i,posMax)
        maxHeapify(A,posMax,tamanoHeap)

def construirHeapMaxIni(A,tamanoHeap):
    for i in range(math.ceil((tamanoHeap-1)/2),-1,-1):
        maxHeapify(A,i,tamanoHeap)

def ordenacionHeapSort(A,tamanoHeap):
    A = A.copy()
    construirHeapMaxIni(A,tamanoHeap)
    for i in range(len(A)-1,0,-1):
        intercambia(A,0,i)
        tamanoHeap -= 1
        maxHeapify(A,0,tamanoHeap)
    
    return A


lista = [56,89,12,7,4,32,9]
ordenada = ordenacionHeapSort(lista,len(lista))
print(ordenada)