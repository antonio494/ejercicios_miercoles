def Punto_numeros(lista_numeros, divisor):
 
    for numero in lista_numeros:
        if numero % divisor == 0:
            return True
    return False

lista_numeros = list(map(int, input("Ingrese una lista de números separados por espacios: ").split()))
divisor = int(input("Ingrese un número entero positivo divisor: "))

if Punto_numeros(lista_numeros, divisor):
    print("Al menos un número de la lista es divisible por el divisor.", lista_numeros)
else:
    print("No hay números en la lista que sean divisibles por el divisor.")
