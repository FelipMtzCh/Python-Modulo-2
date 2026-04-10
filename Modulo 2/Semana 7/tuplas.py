# Se crea una tupla (estructura similar a lista, pero no se puede modificar)
vocales = ('a', 'e', 'i', 'o', 'u')
# Accede al elemento en la posición 2
print(vocales[2])

# Esto daría error porque las tuplas no se pueden modificar
# vocales[2] = 'I'

# Une dos partes de la tupla:
# - desde el inicio hasta la posición 2 (sin incluirla)
# - desde la posición 2 hasta el final
# Nota: el elemento 'i' se repite
print(vocales[:3] + vocales[2:])
# Busca la posición donde se encuentra la letra 'o'
print(vocales.index('o'))

# Convierte la tupla en lista para poder modificar sus elementos
lista_vocales = list(vocales)
# Cambia el elemento en la posición 2 (ahora sí se puede porque es lista)
lista_vocales[2] = 'I'
print(lista_vocales)

# Convierte la lista nuevamente en tupla
tupla_vocales = tuple(lista_vocales)

# Esto daría error otra vez porque la tupla es inmutable
# tupla_vocales[2] = 'I'

# NOTA: Tupla (())  ->  No se puede modificar
# NOTA: Lista ([])  ->  Sí se puede modificar
