# Continue: omite una sola iteración de la repetición de un ciclo

#Uso de la sentencia continue en un ciclo for
for numero in range(1, 11) :
    if numero % 2 :
        continue
    print(f"{numero} es un numero par")

# Uso de la sentencia continue en un ciclo while
numero = 0
while numero < 11 :
    numero += 1
    if numero % 2 == 0 :
        continue
    print(f"{numero} es un numero impar")

##################################################################
# Break: Interrumpe la ejecución de un ciclo

# Uso de la sentencia Break
numero = int(input("Ingrese un digito: "))
limite_inferior = 0
limite_superior = 10
buscado = 5
intentos = 0

while True :
    intentos += 1
    if numero == buscado :
        print(f"El numero {numero} fue encontrado en {intentos} intentos")
        break
    elif numero < buscado :
        limite_superior = buscado
        buscado = (buscado + limite_inferior) // 2
    else :
        limite_inferior = buscado
        buscado = (buscado + limite_superior) // 2
# NOTA: Doble división (//) o division de piso de vuelve resultado de division en numero entero
print("Fin del programa")

##################################################################################
# Exit(): Cierra completamente el program. (No se ejecuta el codigo siguiente)

# Uso de la función exit()
numero = int(input("Ingrese un digito: "))
limite_inferior = 0
limite_superior = 10
buscado = 5
intentos = 0

while True :
    intentos += 1
    if numero == buscado :
        print(f"El numero {numero} fue encontrado en {intentos} intentos")
        exit()
    elif numero < buscado :
        limite_superior = buscado
        buscado = (buscado + limite_inferior) // 2
    else :
        limite_inferior = buscado
        buscado = (buscado + limite_superior) // 2
# NOTA: Doble división (//) o division de piso de vuelve resultado de division en numero entero
print("Fin del programa")

intentos = 0
while True :
    intentos += 1
    print(f"Intento {intentos}")
    if intentos == 20 :
        print("Fin del programa")
        exit()
print("Impresión despúes de la función exit()")
