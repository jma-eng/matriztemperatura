# -----------------------------
# Escritura de Archivo de Texto
# -----------------------------

# Abrimos (o creamos) el archivo en modo escritura ('w')
with open("my_notes.txt", "w") as file:
    # Escribimos tres líneas de notas personales
    file.write("Hoy aprendí a trabajar con archivos en Python.\n")
    file.write("Usamos los métodos write() y readline() para manipular texto.\n")
    file.write("Recordar siempre cerrar el archivo después de usarlo.\n")

# -----------------------------
# Lectura de Archivo de Texto
# -----------------------------

# Abrimos el archivo en modo lectura ('r')
with open("my_notes.txt", "r") as file:
    # Leemos línea por línea usando readline()
    print("Contenido del archivo:")
    linea = file.readline()
    while linea:
        print(linea.strip())  # .strip() para eliminar el salto de línea
        linea = file.readline()

# -----------------------------
# El archivo se cierra automáticamente al salir del bloque 'with'
# -----------------------------
