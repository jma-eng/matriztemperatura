def buscar_valor(matriz, valor):
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            if matriz[i][j] == valor:
                return (i, j)
    return None

# Matriz 3x3
matriz = [
    [4, 8, 15],
    [16, 23, 42],
    [7, 1, 9]
]

valor_a_buscar = int(input("Ingrese el número que desea buscar: "))
resultado = buscar_valor(matriz, valor_a_buscar)

if resultado:
    print(f"El valor {valor_a_buscar} fue encontrado en la posición: {resultado}")
else:
    print(f"El valor {valor_a_buscar} no se encuentra en la matriz.")
