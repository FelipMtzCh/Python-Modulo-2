entrada = input("¡Hola! Introduce tu edad: ");
edad = 0;

if entrada.isnumeric():
    edad = int(entrada);
else:
    print("Dato incorrecto. Debes introducir un número.");
    exit();

if edad <= 0:
    print("WOOOOOW!!! Que joven eres. Pero, lo siento, eso no es posible.");
elif edad > 115:
    print("VAYA!!! ¿Cómo le haces para vivir tanto? No te creo, mejor intenta de nuevo.");
elif edad < 18:
    print("Eres menor de edad así que no puedes comprar tu cigarro.");
else:
    print("Eres mayor de edad. Aquí tienes tu cigarro.");

