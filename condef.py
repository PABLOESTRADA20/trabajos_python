def contar_letras(nombre):
    letras = 0
    letrs = 0
    num_consonantes = 0
    for i in nombre:
        letras = letras + 1
        if i in " aeiouAEIOU":
            letrs = letrs + 1
        elif i in " bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ": 
                num_consonantes = num_consonantes + 1
    print(f"tu nombre tiene {letrs} vocales , tiene  {num_consonantes} consonantes y {letras} letras en total")
nombre = input("ingrese su nombre: ")
contar_letras(nombre)