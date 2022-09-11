"""
imc = Peso / (altura al cuadrado)

imc < 18:
bajo peso

18 <= imc < 26:
peso normal

imc >= 26:
sobrepeso

"""

nombre = input("Ingrese nombre del paciente: ")

peso = input("Ingrese peso en kilogramos del paciente: ")
peso = float(peso)

altura = input("Ingrese altura en metros del paciente: ")
altura = float(altura)

imc = peso / (altura**2)

print(nombre,"tiene un imc de",imc)

if imc < 18:
    print("Bajo peso")
elif imc < 26:
    print("Peso normal")
else:
    print("Sobre peso")