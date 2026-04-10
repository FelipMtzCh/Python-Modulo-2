# Función para capturar y validar la contraseña inicial
def Captura_Password() :
    # Variable que indica si la contraseña cumple las condiciones
    passTrue = False

    while not passTrue :
        password = input("Ingrese una contraseña: ");
        # Elimina espacios al inicio y final
        password = password.strip();

        # Verifica que la contraseña no esté vacía
        if not password :
            print("La contraseña no puede ir vacia");
        else :
            # Verifica que el primer caracter sea un número
            if password[0].isnumeric() :
                # Variable para validar que no haya espacios
                letterConfirm = True;
                # Recorre cada caracter de la contraseña
                for i in password :
                    # Verifica que no haya espacios dentro de la contraseña
                    if i == " " :
                        print("La contraseña no puede tener espacios");
                        letterConfirm = False;
                        break;
                # Si pasa todas las validaciones
                if letterConfirm :
                    passTrue = True;
                    # Llama a la función de confirmación
                    Confirma_Password(password);
            
            else :
                print("La contraseña debe de conenzar con un número");

# Función para confirmar la contraseña ingresada
def Confirma_Password(password) :
    # Variable que indica si la confirmación fue correcta
    confim = False;

    # Permite hasta 3 intentos para confirmar la contraseña
    for i in range(3) :
        passConfirm = input("Ingrese la contraseña nuevamente: ");
        password = password.strip();

        # Compara la contraseña original con la ingresada
        if password == passConfirm :
            print("Contraseña correcta.");
            confim = True;
            break;
        else :
            print("Las contraseñas no coinciden");
            continue;
    
    # Mensaje final si falló los 3 intentos
    if not confim :
        print("Error: Has ingresado la contraseña incorrecta 3 veces.");

# Llamada a la función principal
Captura_Password();
# Mensaje final del programa
print("Fin del Programa");

