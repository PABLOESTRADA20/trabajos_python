op = 0
total = 0
while op !=4:
    print("1. pc $500.000")
    print("2. LGTV 55 Pylgadas $380.000")
    print("3. Microondas hamsa $100.000")
    print("4. Salir")
op = int(input("Ingrese una opcion: "))
match op:
    case 1:
        print("El precio de la pc es: ",500.000*1.19)
        total = 500.000*1.19
    case 2:
        print("El precio de la LGTV es: ",380.000*1.19)
        total = 380.000*1.19
    case 3:
        print("El precio del Microondas es: ",100.000*1.19)
        total = 100.000*1.19
    case 4:
        print("Saliendo del programa.")
    case _:
        print("Opcion no valida.")