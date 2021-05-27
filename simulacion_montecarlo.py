import random
import collections

TIPOS_CARTAS = ["Espadas", "Corazones", "Rombos", "Treboles"]
VALORES = ["AS", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]

def crear_mazo():
    mazo = []
    for tipo in TIPOS_CARTAS:
        for valor in VALORES:
            mazo.append((tipo, valor))

    return mazo


def obtener_mano(mazo, tamano_mano):
    return random.sample(mazo, tamano_mano)

def simulacion_montecarlo():
    tamano_mano = 5
    iteraciones = 1000
    mazo = crear_mazo()
    manos = []

    for _ in range(iteraciones):
        manos.append(obtener_mano(mazo, tamano_mano))

    pares = 0
    tercias = 0
    for mano in manos:
        valores = []
        for carta in mano:
            valores.append(carta[1])

        counter = dict(collections.Counter(valores))
        for val in counter.values():
            if val == 2:
                pares += 1
                break
        for val in counter.values():
            if val == 3:
                tercias += 1
                break

    probabilidad_par = pares / iteraciones
    probabilidad_tercia = tercias / iteraciones

    print(f"Probabilidad de par en una mano de {tamano_mano} es del: {probabilidad_par * 100} por ciento")
    print(f"Probabilidad de tercia en una mano de {tamano_mano} es del: {probabilidad_tercia * 100} por ciento")


def main():
    simulacion_montecarlo()

if __name__ == "__main__":
   main()