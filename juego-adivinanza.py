

import random


numero_secreto = random.randint(0,10)
adivinado=False

print("Bienvenido al juego de adivinar el numero secreto!")

while not adivinado:
    entrada = input("Introduce un numero del 1 al 99: ")
    numero=int(entrada)

    if numero == numero_secreto:
        print("Felicitaciones has adivinado el numero secreto")
        adivinado=True

    elif numero < numero_secreto:
         print("El numero es mayor al ingresado")

    else:
         print("El numero es menor al ingresado")

