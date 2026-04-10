edad = "";

while not edad:
    edad = input("Ingresa tu edad para saber cuanto pagas por usar transporte: ");

    if edad.isnumeric():
        edad = int(edad);
    else:
        print("Dato incorrecto. Debes introducir tu edad en años.");
        edad = "";

if edad <= 5:
    print("No pagas por usar el transporte.");
elif edad >= 60:
    print("Puedes pagar la mitad del transporte.");
else:
    print("Debes pagar el transporte completo.");
