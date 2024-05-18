def bubble_sort(arr):
    n = len(arr)
    trocas = 0
    comparacoes = 0
    varreduras_completas = 0
    
    if n <= 1:
        print("Array já ordenado:", arr)
        return
    
    for i in range(n):
        swapped = False 
        for j in range(0, n-i-1):
            comparacoes += 1
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                trocas += 1
                swapped = True
        if not swapped: 
            break
        else:
            varreduras_completas += 1
    
    print("Comparações:", comparacoes)
    print("Trocas:", trocas)
    print("Varreduras completas:", varreduras_completas)

# Exemplo de uso
arr = [5, 1, 8, 3, 9, 2]
print("Array original:", arr)
bubble_sort(arr)
print("Array ordenado:", arr)
