import random

def tirar_dado():
    return random.choice([1, 2, 3, 4, 5, 6])

def simulacion_dado(num_tiros):
    resultado_tiros = []

    for _ in range(num_tiros):
        resultado_tiros.append(tirar_dado())

    return resultado_tiros

def main():
    num_tiros = 10
    num_iteraciones = 10000
    resultado_tiro_iteracion = []

    for _ in range(num_iteraciones):
        resultado_tiro_iteracion.append(simulacion_dado(num_tiros))

    # Calcular prob de tiros con 1
    resultado_cara_1 = 0
    resultado_no_cara_1 = 0

    for resultado in resultado_tiro_iteracion:
        if 1 in resultado:
            resultado_cara_1 +=1

    for resultado in resultado_tiro_iteracion:
        if 1 not in resultado:
            resultado_no_cara_1 +=1

    prob_cara_1 = resultado_cara_1 / num_iteraciones
    prob_no_cara_1 = resultado_no_cara_1 / num_iteraciones

    # 1 - P(De no 1) = (5/6) ^ (num_tiros)
    print(f"Probabilidad de obtener la cara 1 en {num_tiros} tiros: {prob_cara_1}")
    print(f"Probabilidad de no obtener la cara 1 en {num_tiros} tiros: {prob_no_cara_1}")

if __name__ == "__main__":
    main()