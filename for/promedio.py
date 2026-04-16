print("promedio de notas")
num1= int(input("ingrese su cantidad de notas : "))

suma = 0

for i in range(num1):
    num2 = float(input(f"ingrese su nota {i+1}: "))
    suma = suma + num2

    prom = suma /num1
print ("su promedio es ", prom)

if prom >= 4:
    print("aprobo")
else:
    print("reprobo")