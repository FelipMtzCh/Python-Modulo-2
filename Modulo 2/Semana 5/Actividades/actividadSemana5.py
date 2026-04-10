def capturaAño (año_Actual):
    año = 0;
    while año == 0:
        if (año_Actual):
            entrada = input("Introduce el año actual: ");
        else:
            entrada = input("Introduce otro año para calcular: ");
        
        if entrada.isnumeric():
            if int(entrada) <= 1000:
                print("Por favor introduce un año mayor a 1000");
            elif int(entrada) >= 3000:
                print("Por favor introduce un año menor a 3000");
            else:
                año = int(entrada);
        else:
            print("Dato incorrecto. Debes de introducir un numero.");
    return año;

def mensajeFinal (actual, año):
    if actual > año:
        diferencia = actual - año;
        if diferencia > 1:
            print(f"Han pasado {diferencia} años desde el año que has introducio");
        else:
            print(f"Desde el año {año} ha pasado 1 año");
    elif actual < año:
        diferencia = año - actual;
        if diferencia > 1:
            print(f"Faltan {diferencia} años para llegar al año que has introducido");
        else:
            print(f"Para llegar a {año} hace falta 1 año");
    else:
        print("Has introducido el mismo año que el actual");


año_Actual = capturaAño(True);
año = capturaAño(False);
mensajeFinal(año_Actual, año);

