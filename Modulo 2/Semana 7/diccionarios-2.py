# Se crea un diccionario usando la función dict()
# Cada nombre es una clave y su tiempo es el valor
tiempos = dict (
    Hamilton = '11:49.8',
    Bottas = '1:56.4',
    Perez = '1:53.8',
    Verstappen = '1:52.6'
)

# Se crea nuevamente el diccionario, pero ahora usando llaves {}
# Aquí se repite la clave 'Hamilton' varias veces
tiempos = {
    'Hamilton': '11:49.8',
    'Bottas': '1:56.4',
    'Hamilton': '1:53.8',
    'Hamilton': '1:52.6'
}

# Imprime el diccionario final
# Solo se conserva el último valor asignado a 'Hamilton'
print(tiempos)

# NOTA: En un diccionario NO puede haber claves repetidas
