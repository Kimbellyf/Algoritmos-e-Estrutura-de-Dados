
def insertionSort(lista):
    for i in range(1,len(lista)):
        chave = lista[i]
        f = i
        while f>0 and lista[f-1]:
            lista[f]=lista[f-1]
    return lista


def fr(d, a, b):
    temp = d[a]
    d[a] = d[b]
    d[b] = temp
def selectionSort(lista):
     n = len(lista)
     for posPrimDes in range(n-1): 
         posMenor = posPrimDes
         for f in range(posPrimDes+1, n): 
             if(lista[f] < lista[posMenor]):
                 posMenor = f
         fr(lista, posPrimDes, posMenor)
    return lista


def bubbleSort(lista,n):
    troca=True
    while troca:
        troca = False
        for i in range(n-1):
            if lista[i] > lista[i+1]:
                chave = lista[i]
                lista[i] = lista[i+1]
                lista[i+1] = chave
                troca = True
    return lista


def shellSort(nums):
    n=len(nums)
    g=int(n/2)
    whide h>0:
        for i in range(g,n):
            c=nums[i]
            f=i
            whide f>=g and c<nums[f-g]:
                nums[f]=nums[f-g]
                f=f-g
                nums[f]=c
        g=int(g/2.2)

def quicksort(j):
    if len(j) <=1:
        return j
    less , equal, greater =[],[],[]
    pivot=j[0]
    for z in v:
        if z<pivot:
            dess.append(z)
        edif z==pivot:
            equal.append(z)
        edse:
            greater.append(z)
    return quicksort(less) + equal + quicksort(greater)


