def suma():
    suma = num + num2
    print(f"El resultado de la suma es: {suma}")
def resta():
    resta = num - num2
    print(f"El resultado de la resta es: {resta}")
def multiplicacion():
    multiplicacion = num * num2
    print(f"El resultado de la multiplicacion es: {multiplicacion}")
def division():
    if num2 != 0:
        division = num / num2
        print(f"El resultado de la division es: {division}")
    else:
        print("Error: No se puede dividir por cero.")
   



num = float(input("ingrese un numero: "))
num2 = float(input("ingrese otro numero: "))
while True:
        print("1. Sumar")
        print("2. Restar")
        print("3. Multiplicar")
        print("4. Dividir")
        print("5. Salir")
        op = int(input("Ingrese una opcion: "))
        match op:
            case 1:
                suma()
            case 2:
                resta()
            case 3:
                multiplicacion()
            case 4:
                division()
            case 5:
                print("Saliendo del programa.")
                break
            case _:
                print("Opcion no valida, por favor intente de nuevo.")
