#Camila López y Ana Amezquita

import random

def numeroInt(valor):
    try:
        int(valor)
        return True
    except ValueError:
        return False
    
def adivinar():
    while True:
        rangoMax = input("Ingrese un número para su rango máximo: ")
        if numeroInt(rangoMax):
            rangoMax = int(rangoMax)
            if rangoMax >=1:
                break
            else:
                print("Introduzca un número mayor a 0")
        else:
            print("No es un número válido")

    intentos = max(1, rangoMax // 20)
    
    numeroAdivinar = random.randint(1, rangoMax)

    lista = ["Falló"] * rangoMax
    lista[numeroAdivinar -1] = "Acertó"

    intento = 0
    aciertos = False

    while intento < intentos and not aciertos:
        numeroUsuario = input(f"Intento {intento+1}; introduce un número entre 1 y {rangoMax}: ")
        if numeroInt(numeroUsuario):
            numero = int(numeroUsuario)
            intento +=1

            if numero < 1 or numero > rangoMax:
                print(f"Debe ingresar un número entre 1 y {rangoMax}")
                continue
            if numero == numeroAdivinar:
                print(f"¡Haz adivinado el número!. Lo hiciste en {intento} intentos")
                aciertos = True
            elif numero < numeroAdivinar:
                print("El número a adivinar es mayor")
            else:
                print("El número a adivinar es menor")
        else:
            print("No es un número válido")
            intento += 1
    if not aciertos:
        print(f"Se acabaron los intentos y no lograste adivinar el número. El número a adivinar era {numeroAdivinar}")

    print(f"Lista de intentos {lista}")
adivinar()