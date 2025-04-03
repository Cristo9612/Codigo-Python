from random import *

intentos = 0
estimado = 0
numero_aleatorio = randint(1,100)

nombre = input("\nCual es tu nombre: ")
print(f'\nBueno, {nombre}, he pensado un número entre 1 a 100, tienes 8 intentos para adivinar.')

while intentos < 8:
    estimado = int(input("\nCuál es el número? "))
    intentos += 1

    if estimado not in range(1,100):
        print("Ha elegido un número que no está permitido. Debe de estar dentro del rango 1 a 100")
    elif estimado < numero_aleatorio:
        print("Respuesta es incorrecta, ha elegido un número menor al número secreto.")
    elif estimado >  numero_aleatorio:
        print("Respuesta es incorrecta, ha elegido un número mayor al número secreto.")
    else:
        print(f'"Felicidades", acertó el número secreto le ha tomado {intentos} intentos.')
        break
if estimado != numero_aleatorio:
    print(f"\nHas perido, excediste el numero de intentos el número secresto es: {numero_aleatorio}")
