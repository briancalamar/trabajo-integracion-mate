def decimalABinario ():
    
    while True:
        cadenaNumero = input("Ingresa un número entero y positivo: ")
        try:
            numero = int(cadenaNumero)
            if numero <= 0:
                print("Debe ingresar un número positivo.")
                continue
            break
        except ValueError:
            print(f"Ingresaste un valor que no es valido: {cadenaNumero}.")

    binario = ''
    numeroADividir = numero

    while numeroADividir >= 1:
        resto = numeroADividir % 2

        if (resto != 0):
            binario = "1" + binario
        else:
            binario = "0" + binario
        
        numeroADividir = numeroADividir // 2

    print(f"Su numero ingresado ({cadenaNumero}) en binario es: {binario}")

# Creamos una funcion que nos ayuda a saber si la cadena de texto es un binario 
def esBinario(cadena):
    # todo: Podriamos validar que sea una cadena

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
        digito = numeroAEvaluar % 10
        numeroAEvaluar = numeroAEvaluar // 10
        valorDecimalDelDigito = digito * (2 ** potencia)
        decimal += valorDecimalDelDigito
        potencia += 1

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
