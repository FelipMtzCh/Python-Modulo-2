# Se crea una lista llamada "pila" (funciona como una pila: último en entrar, primero en salir)
pila = [3, 6, 7]

# Mientras la pila tenga 3 o más elementos, el ciclo se sigue ejecutando
while len(pila) >= 3 :
    # pila[-1] obtiene el último elemento de la lista
    # Se verifica si NO es múltiplo de 3
    # (si el residuo de dividir entre 3 es diferente de 0)
    if pila[-1] % 3 :
        # Se extrae (elimina) el último elemento de la pila
        extraido = pila.pop()
        # Se vuelve a agregar ese elemento pero aumentado en 1
        pila.append(extraido + 1)
        # Se imprime el estado actual de la pila
        print(pila)
    else :
        # Si el último elemento SÍ es múltiplo de 3,
        # se muestra este mensaje
        print("Todos los elementos de la pila son múltiplos de 3")
        # Se rompe el ciclo (termina el while)
        break
