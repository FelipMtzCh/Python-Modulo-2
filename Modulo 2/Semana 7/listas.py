# Lista con diferentes tipos de datos: entero, flotante, string y número complejo
mix = [0, 1.0, "dos", 3 + 4j]

# Recorre cada elemento de la lista
for i in mix :
    # Imprime el valor y su tipo de dato
    print(f"{i:6} - Tipo: {type(i)}");

# Imprime la cantidad de elementos que tiene la lista
print(len(mix));

# Crea una nueva lista eliminando el elemento "dos" (posición 2)
# Toma los primeros 2 elementos y luego desde el índice 3 hasta el final
sin_dos = mix[:2] + mix[3:]

# Imprime la lista original y la nueva lista sin el elemento "dos"
print(mix, sin_dos)

# Duplica la lista 3 veces (repite su contenido)
duplicado = mix * 3
print(duplicado)

# Lista de números cuadrados
cuadrados = [0, 1, 4, 9, 16, 25]
for i in range(len(cuadrados)) :
    # Multiplica cada elemento por su índice
    cuadrados[i] = cuadrados[i] * i
    # Imprime el nuevo valor
    print(f"Ahora estan al cubo {cuadrados[i]}")

# Agrega al final el cubo de 7
cuadrados.append(7 ** 3)
# Inserta en la posición 6 el cubo de 6
cuadrados.insert(6, 6 ** 3)
# Agrega varios elementos al final de la lista
cuadrados.extend([27, 1000, -1])
# Agrega una secuencia de números desde -1 hasta -3
cuadrados.extend(range(-1, -4, -1))
# Imprime la lista completa
print(cuadrados)

# Elimina los elementos desde la posición 9 hasta el final
del cuadrados[9:]
print(cuadrados)

# Elimina el valor 27 de la lista
cuadrados.remove(27)
print(cuadrados)

# Elimina y guarda el elemento en la posición 2
valor_removido = cuadrados.pop(2)
# Imprime el valor eliminado
print(valor_removido)
# Imprime la lista después de eliminar ese valor
print(cuadrados)

# Elimina todos los elementos de la lista (la deja vacía)
cuadrados.clear()
print(cuadrados)
