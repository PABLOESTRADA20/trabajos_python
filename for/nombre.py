nombre = input("¿Cuál es tu nombre? ")
letrs = 0
for i in nombre:
    if i in " aeiouAEIOU":
        letrs = letrs + 1
print(f"tu nombre tiene {letrs} vocales")