def decimalABinario ():
    cadenaNumero = input("Ingrese un número entero: ")

    while cadenaNumero == '':
        cadenaNumero = input("Por favor, debe ingresar un numero: ")

    numero = int(cadenaNumero)

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
    
    largoCadena = len(cadenaNumero)
    print(f'largocadena: {largoCadena}')

    for i in range(largoCadena, -1, -1):
        print(f'i: {i}')
        print(f'type: {type(cadenaNumero)}')
        digitoAEvaluar = cadenaNumero[i]
        print(f'DigitoAEvaluar: {digitoAEvaluar}')
        potencia = largoCadena - i
        valor = digitoAEvaluar * 2 ** potencia
        print(f'valor: {valor}')
        print(f'potencia: {potencia}')

binarioADecimal()

'''
decimalABinario()
'''