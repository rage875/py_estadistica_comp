import sys
from pathlib import Path
file = Path(__file__).resolve()
package_root_directory = file.parents[1]
sys.path.append(str(package_root_directory))

import random
from bokeh.models.annotations import Title
from bokeh.plotting import figure, show
from estadisticas import desviacion_estandar, media, varianza

def mostrar_circulo(puntos_fuera, puntos_dentro):
    grafica = figure(title = "Circulo de puntos aleatorios")
    grafica.circle(puntos_fuera[0], puntos_fuera[1], color="red")
    grafica.circle(puntos_dentro[0], puntos_dentro[1], color="blue")

    show(grafica)

def sim_calculo_de_pi(numero_de_puntos):
    dentro_circulo = 0
    puntos_dentro_circulo = ([], [])
    puntos_afuera_circulo = ([], [])

    # Generar puntos y checar si estan dentro del circulo
    for _ in range(numero_de_puntos):
        # Obtener puntos de forma aleatoria en coord (x,y)
        x = random.random() * random.choice([-1, 1])
        y = random.random() * random.choice([-1, 1])
        # Teorema de pitagoras
        distancia_desde_el_centro = (x ** 2 + y ** 2) ** 0.5

        if distancia_desde_el_centro <= 1:
            dentro_circulo += 1
            puntos_dentro_circulo[0].append(x)
            puntos_dentro_circulo[1].append(y)
        else:
            puntos_afuera_circulo[0].append(x)
            puntos_afuera_circulo[1].append(y)

    # Mostrar circulo
    #mostrar_circulo(puntos_afuera_circulo, puntos_dentro_circulo)

    return (4 * dentro_circulo) /  numero_de_puntos

def estimacion(numero_de_puntos, iteraciones):
    estimados = []

    for _ in range(iteraciones):
        estimados.append(sim_calculo_de_pi(numero_de_puntos))

    print(f"Arreglo de datos: {estimados}")
    print(f"Media: {media(estimados)}")
    print(f"Varianza: {varianza(estimados)}")
    print(f"Desviacion estandar: {desviacion_estandar(estimados)}")

def main():
    numero_de_puntos = 10000
    iteraciones = 100
    #print(sim_calculo_de_pi())
    estimacion(numero_de_puntos, iteraciones)

if __name__ == "__main__":
    main()