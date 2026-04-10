# Se crea un conjunto (set), que no permite elementos repetidos
canasta = {'manzana', 'naranja', 'manzana', 'pera', 'naranja', 'platano'}
# Imprime el conjunto (los elementos repetidos se eliminan automáticamente)
print(canasta)

# Verifica si 'manzana' está dentro del conjunto (True o False)
print('manzana' in canasta)
# Verifica si 'melon' está dentro del conjunto
print('melon' in canasta)


# Lista con vocales (incluye un elemento repetido)
vocales = ['a', 'e', 'i', 'o', 'u', 'a']
print(vocales)

# Convierte la lista en conjunto para eliminar duplicados
# Luego la vuelve a convertir en lista
vocales = list(set(vocales))
print(vocales)


# Conjunto de vocales (los duplicados se eliminan automáticamente)
vocales1 = {'a', 'e', 'i', 'o', 'u', 'a'}
# Otro conjunto con algunas vocales
vocales2 = {'e', 'i', 'o'}

# Verifica si vocales2 es subconjunto de vocales1
# (si todos sus elementos están dentro de vocales1)
print(vocales2.issubset(vocales1))


# Dos conjuntos diferentes (mayúsculas y minúsculas)
vocales_1 = {'a', 'e', 'i', 'o', 'u'}
vocales_2 = {'A', 'E', 'I', 'O', 'u'}

# Diferencia: elementos que están en vocales_1 pero no en vocales_2
print(vocales_1 - vocales_2)

# Unión: combina todos los elementos de ambos conjuntos (sin repetir)
print(vocales_1 | vocales_2)

# Intersección: elementos que están en ambos conjuntos
print(vocales_1 & vocales_2)

# Diferencia simétrica: elementos que están en uno u otro, pero no en ambos
print(vocales_1 ^ vocales_2)

# NOTA: {}  ->  crea un conjunto (set)
