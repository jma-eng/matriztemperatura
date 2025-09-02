def bubble_sort(fila):
    n = len(fila)
    for i in range(n):
        for j in range(0, n-i-1):
            if fila[j] > fila[j+1]:
                fila[j], fila[j+1] = fila[j+1], fila[j]
    return fila

# Matriz 3x3
matriz = [
    [12, 5, 7],
    [3, 8, 1],
    [9, 4, 6]
]

print("Matriz original:")
for fila in matriz:
    print(fila)

fila_a_ordenar = int(input("Ingrese el índice de la fila que desea ordenar (0-2): "))

if 0 <= fila_a_ordenar < len(matriz):
    matriz[fila_a_ordenar] = bubble_sort(matriz[fila_a_ordenar])
    print("\nMatriz con la fila ordenada:")
    for fila in matriz:
        print(fila)
else:
    print("Índice de fila inválido.")
