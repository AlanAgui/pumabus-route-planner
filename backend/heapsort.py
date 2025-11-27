import math

# Funciones del HeapSort
def hIzq(i):
    return 2 * i + 1

def hDer(i):
    return 2 * i + 2

def intercambia(A, x, y):
    tmp = A[x]
    A[x] = A[y]
    A[y] = tmp

def maxHeapify(A, i, tamanoHeap):
    L = hIzq(i)
    R = hDer(i)
    
    # Comparar los pesos de las aristas y asegurarse de que el mayor esté arriba
    if L <= (tamanoHeap - 1) and A[L][2] > A[i][2]:  # Usamos A[L][2] que es el peso
        posMax = L
    else:
        posMax = i
    if R <= (tamanoHeap - 1) and A[R][2] > A[posMax][2]:
        posMax = R
    if posMax != i:
        intercambia(A, i, posMax)
        maxHeapify(A, posMax, tamanoHeap)

def construirHeapMaxIni(A, tamanoHeap):
    for i in range(math.ceil((tamanoHeap - 1) / 2), -1, -1):
        maxHeapify(A, i, tamanoHeap)

def ordenacionHeapSort(A, tamanoHeap):
    A = A.copy()
    construirHeapMaxIni(A, tamanoHeap)
    for i in range(len(A) - 1, 0, -1):
        intercambia(A, 0, i)
        tamanoHeap -= 1
        maxHeapify(A, 0, tamanoHeap)
    return A
