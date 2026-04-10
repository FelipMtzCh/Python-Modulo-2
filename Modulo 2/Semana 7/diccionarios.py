# Diccionario donde:
# - la clave es el nombre del piloto
# - el valor es su tiempo registrado
tiempos = {
    'Hamilton': '1:49.8',
    'Bottas': '1:56.4',
    'Perez': '1:53.8',
    'Verstappen': '1:52.6'
}

# Muestra todos los elementos del diccionario en pares (clave, valor)
print(tiempos.items())

# Muestra solo las claves del diccionario (los nombres)
print(tiempos.keys())

# Muestra solo los valores del diccionario (los tiempos)
print(tiempos.values())

# Obtiene el valor asociado a la clave 'Hamilton'
print(tiempos.get('Hamilton'))

# Intenta obtener el valor de 'hamilton' (con minúscula)
# Como no existe, devuelve el mensaje por defecto 'No encontrado'
print(tiempos.get('hamilton', 'No encontrado'))

