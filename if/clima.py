tiempo = "clima actual" 
temperatura = 18.6
diadelmes = 16
mes = 4
llueve = False

print(f"{tiempo}")
print(f"Fecha de hoy: {diadelmes} de {mes}")
print(f"Temperatura: {temperatura}°C")

if llueve == False:
    print("Saco el paraguas.")
else:
    print("No saco el paraguas.")