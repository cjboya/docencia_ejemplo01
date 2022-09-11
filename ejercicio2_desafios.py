a = input("Ingrese año para calcular: ")
a = int(a)

if a % 400 == 0:
    print("Es BISIESTO")
else:
    if a % 4 == 0 and a % 100 != 0:
        print("Es bisiesto")
    else:
        print("No es bisiesto")