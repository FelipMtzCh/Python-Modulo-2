# Lista inicial de vocales
vocales = ['a', 'e', 'i', 'o', 'u']

# Reemplaza los elementos desde la posición 1 a la 3 por nuevas letras
vocales[1:4] = ['E', 'I', 'O']
# Imprime la lista y su tamaño
print(vocales, len(vocales))

# Elimina los elementos desde la posición 1 a la 3
vocales[1:4] = []
print(vocales, len(vocales))

# Inserta varios elementos en la posición 1 (reemplaza ese rango)
vocales[1:2] = ['e', 'i', 'o', 'u']
print(vocales, len(vocales))

# Agrega elementos al final de la lista
vocales.extend(['i', 'i'])
print(vocales, len(vocales))

# Devuelve la posición de la primera aparición de 'i'
print(vocales.index('i'))

# Cuenta cuántas veces aparece 'i' en la lista
print(vocales.count('i'))

# Busca 'i' a partir de la posición 6
print(vocales.index('i', 6))

# Invierte el orden de la lista
vocales.reverse()
print(vocales, len(vocales))

# Ordena la lista alfabéticamente
vocales.sort()
print(vocales, len(vocales))


# Lista de marcas de carros
carros = ['Audi', 'Ford', 'BMW', 'VW']

# Ordena la lista según la longitud de cada palabra
carros.sort(key=len)
print(carros)


# Lista que contiene otras listas (lista anidada)
listas = [[0, 1], [2, 3, 4], [5, 6]]

# Imprime la primera lista y luego una parte de la lista principal
print(listas[0], listas[1:3])

# Accede al elemento en la posición 1 de la tercera lista interna
print(listas[2][1])


# Lista original
vocales1 = ['a', 'e', 'i', 'o', 'u']

# vocales2 apunta a la misma lista (no es copia, es referencia)
vocales2 = vocales1
# Imprime ambas listas (son iguales)
print(vocales1, vocales2)
# Imprime las direcciones en memoria (son iguales)
print(id(vocales1), id(vocales2))

# Crea una copia independiente de la lista
vocales3 = vocales1.copy()
# Imprime ambas listas
print(vocales1, vocales3)
# Imprime las direcciones en memoria (son diferentes)
print(id(vocales1), id(vocales3))

# Imprime la dirección en memoria del elemento en la posición 2
# (es la misma porque vocales1 y vocales2 comparten lista)
print(id(vocales1[2]), id(vocales2[2]))

# También coincide porque los elementos individuales pueden compartir memoria
print(id(vocales1[2]), id(vocales3[2]))

# Elimina el elemento en la posición 2 de vocales1
del vocales1[2]

# vocales2 también cambia porque es la misma lista
# vocales3 no cambia porque es copia independiente
print(vocales2, vocales3)

# Compara direcciones de memoria de elementos después del cambio
print(id(vocales1[2]), id(vocales3[3]))

# NOTA: =  ->  misma lista (referencia)
#NOTA: .copy()  ->  nueva lista independiente
