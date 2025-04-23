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

decimalABinario()