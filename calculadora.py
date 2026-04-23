
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
            total = num + num2
            print(f"El resultado de la suma es: {total}")
        case 2:
            total = num - num2
            print(f"El resultado de la resta es: {total}")
        case 3:
            total = num * num2
            print(f"El resultado de la multiplicacion es: {total}")
        case 4:
            if num2 != 0:
                total = num / num2
                print(f"El resultado de la division es: {total}")
            else:
                print("Error: No se puede dividir por cero.")
        case 5:
            print("Saliendo del programa.")

        case _:
            print("Opcion no valida, por favor intente de nuevo.")