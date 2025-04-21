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

decimalABinario()