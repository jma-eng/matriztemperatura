# Crear un diccionario llamado 'informacion_personal' con datos ficticios
informacion_personal = {
    "nombre": " MARCELO ALMEIDA",
    "edad": 32,
    "ciudad": "QUITO",
    "profesion": "TECNOLOGIAS DE LA INFORMACION"
}

# Acceder al valor de la clave 'ciudad' y modificarlo
informacion_personal["ciudad"] = "TUMBACO"  # Se cambia la ciudad de Madrid a Barcelona

# Agregar una nueva clave-valor que represente otra profesión (por ejemplo, trabajo secundario)
informacion_personal["profesion_2"] = "CHEF"

# Verificar si la clave 'telefono' existe en el diccionario
if "telefono" not in informacion_personal:
    # Si no existe, agregarla con un número ficticio
    informacion_personal["telefono"] = "09ZZZZZZZ"

# Eliminar la clave 'edad' ya que no es necesaria
informacion_personal.pop("edad", None)  # pop elimina la clave; 'None' evita error si no existe

# Imprimir el diccionario final después de todas las modificaciones
print("Diccionario final, con los datos anteriores:")
print(informacion_personal)
