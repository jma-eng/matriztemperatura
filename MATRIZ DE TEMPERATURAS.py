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

# Calcular promedios semanales por ciudad
for i, ciudad in enumerate(ciudades):  # Recorremos ciudades
    print(f"\nCiudad: {ciudad}")
    for semana in range(semanas):  # Recorremos semanas
        suma = 0
        for dia in range(len(dias)):  # Recorremos días
            suma += temperaturas[i][semana][dia]
        promedio = suma / len(dias)
        print(f"  Semana {semana + 1}: Promedio = {promedio:.2f} °C")
