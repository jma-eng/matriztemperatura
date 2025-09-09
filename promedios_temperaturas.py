# Registro de temperaturas diarias en ciudades usando una matriz 3D

# Ciudades, semanas y días
ciudades = ["Quito", "Guayaquil", "Cuenca"]
semanas = 2
dias = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo"]

# Inicializamos la matriz 3D con valores de ejemplo
# temperaturas[ciudad][semana][día]
temperaturas = [
    [   # Quito
        [15, 17, 16, 18, 19, 20, 18],  # Semana 1
        [14, 16, 15, 17, 18, 19, 17]   # Semana 2
    ],
    [   # Guayaquil
        [28, 29, 30, 31, 32, 30, 29],  # Semana 1
        [27, 28, 29, 30, 31, 30, 28]   # Semana 2
    ],
    [   # Cuenca
        [12, 13, 14, 15, 14, 13, 12],  # Semana 1
        [11, 12, 13, 14, 15, 14, 13]   # Semana 2
    ]
]

def calcular_promedios_ciudades(ciudades, temperaturas):
    """
    Calcula el promedio general de temperatura para cada ciudad
    a partir de una matriz 3D de temperaturas [ciudad][semana][día].

    Parámetros:
    - ciudades (list): Lista de nombres de ciudades.
    - temperaturas (list): Matriz 3D de temperaturas.

    Retorna:
    - dict: Diccionario con el promedio de temperatura por ciudad.
    """
    promedios = {}

    for i, ciudad in enumerate(ciudades):
        suma_total = 0
        total_dias = 0

        for semana in temperaturas[i]:
            suma_total += sum(semana)
            total_dias += len(semana)

        promedio = suma_total / total_dias
        promedios[ciudad] = round(promedio, 2)

    return promedios

# Llamamos a la función y mostramos los resultados
resultados = calcular_promedios_ciudades(ciudades, temperaturas)

print("\nPromedios generales de temperatura por ciudad:")
for ciudad, promedio in resultados.items():
    print(f"{ciudad}: {promedio} °C")
