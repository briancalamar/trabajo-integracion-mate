def decimalABinario ():
    
    while True:
        # Pedimos al usuario que ingrese un numero entero y positivo
        # y lo guardamos en la variable cadenaNumero
        cadenaNumero = input("Ingresa un número entero y positivo: ")
        try:
            # Convertimos la cadena a un entero
            numero = int(cadenaNumero)
            # Si el numero es menor o igual a 0, saltea a la siguiente iteracion
            # y vuelve a pedir el numero
            if numero <= 0:
                print("Debe ingresar un número positivo.")
                continue
            break
        # Si el usuario ingresa un valor que no es un entero, se lanza una excepcion
        # se imprime un mensaje de error y se vuelve a pedir el numero
        except ValueError:
            print(f"Ingresaste un valor que no es valido: {cadenaNumero}.")

    binario = ''
    numeroADividir = numero

    # Hacemos un bucle que se ejecuta mientras el numero a dividir sea mayor o igual a 1
    while numeroADividir >= 1:
        # Obtenemos el resto de la division entre el numero a dividir y 2
        resto = numeroADividir % 2

        # Si el resto es diferente de 0, concatenamos un 1 al binario
        if (resto != 0):
            binario = "1" + binario
        # Sino concatenamos un 0 al binario
        else:
            binario = "0" + binario
        # Dividimos el numero a dividir entre 2 para obtener el siguiente numero
        # a dividir en la siguiente iteracion
        numeroADividir = numeroADividir // 2

    print(f"Su numero ingresado ({cadenaNumero}) en binario es: {binario}")

# Creamos una funcion que nos ayuda a saber si la cadena de texto es un binario 
def esBinario(cadena):

    # Recorremos la cadena en busca de caracteres diferentes a 0 (ceros) o 1 (unos)
    for char in cadena:
        if (char != '0' or char != '1'):
            # Si algun caracter es diferente a 0 o 1, devolvemos False
            return False
    
    # En caso todos los caracteres pertenezcan a 0 o 1, devolvemos True
    return True

def binarioADecimal ():
    cadenaNumero = input("Ingrese un número binario: ")
    # Validamos sea un binario
    esUnBinario = esBinario(cadenaNumero)

    # En caso no sea binario, se genera un bucle hasta que el usuario ingrese un numero binario valido
    while esUnBinario:
        cadenaNumero = input("Por favor, ingrese un número binario valido ( debe contener 0 o 1 ): ")
        esUnBinario = esBinario(cadenaNumero)

    numeroAEvaluar = int(cadenaNumero)
    potencia = 0
    decimal = 0

    while numeroAEvaluar >= 1:
        # Obtenemos el digito menos significativo
        # (el que se encuentra en la posicion menos significativa)
        digito = numeroAEvaluar % 10
        numeroAEvaluar = numeroAEvaluar // 10
        valorDecimalDelDigito = digito * (2 ** potencia)
        decimal += valorDecimalDelDigito
        potencia += 1

    print(f"Su binario ingresado ({cadenaNumero}) en decimal es: {decimal}")

def calculadoraDeDecimalYBinarios ():
    opcion = ''

    print('Bienvenido, por favor seleccione una opcion (Ingrese uno de los siguientes numeros)')

    while opcion == '':
        print('\n')
        print('1. Calculadora de decimal a binario')
        print('2. Calculadora de binario a decimal')
        print('3. Salir')

        opcion = input('Ingrese la opcion elegida: ')

        if opcion == '1':
            decimalABinario()
        elif opcion == '2':
            binarioADecimal()
        elif opcion == '3':
            continue
        opcion = ''

calculadoraDeDecimalYBinarios()
