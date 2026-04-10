ingles_a_español = {"red": "rojo", "orange": "naranja", "yellow": "amarillo", "green": "verde", "blue": "azul", "purple": "morado", "violet": "violeta", "indigo": "indigo"}
español_a_ingles = {"rojo": "red", "naranja": "orange", "amarillo": "yellow", "verde": "green", "azul": "blue", "morado": "purple", "violeta": "violet", "indigo": "indigo"}

def SeleccionaTraduccion ():
    traducir = True
    while traducir:
        print("Ingrese la opción deseada")
        opcion = input("Traducir a español (1) Traducir a ingles (2) Dejar de traducir (0): ")
        
        if opcion == "0":
            print("El programa va a finalizar.")
            traducir = False
        elif opcion == "1":
            print("Se traducira de ingles a español.")
            solicitarTexto(int(opcion))
            continue
        elif opcion == "2":
            print("Se va a traducir de español a ingles.")
            solicitarTexto(int(opcion))
            continue
        else :
            print("Se ha ingresado una opción no valida. Intente de nuevo.")
            continue

def solicitarTexto(a_español):
    
    idioma_origen = "ingles" if a_español == 1 else "español"

    frase = input(f"Escribe una frase que cotenga el nombre de un color en {idioma_origen}: ")
    Traductor(a_español, frase)
    

def Traductor (a_español, frase):
    color_traducido = ''
    frase = frase.lower()
    palabras = frase.split()

    for palabra in palabras:
        if a_español == 1:
            if palabra in ingles_a_español:
                color_traducido =  ingles_a_español[palabra]
                print(f"El color {palabra}, en español se escribe: {color_traducido}")
        else:
            if palabra in español_a_ingles:
                color_traducido = español_a_ingles[palabra]
                print(f"El color {palabra}, en ingles se escribe: {color_traducido}")

    if color_traducido == "":
        print("No se encontro ningun color en el texto.")

print("Este programa tiene la funcionalidad de traducir colores en Ingles y Español")
SeleccionaTraduccion()
