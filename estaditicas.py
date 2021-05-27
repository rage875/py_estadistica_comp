import random

def media(X):
    # Promedio de los datos
    return sum(X) / len(X)

def varianza(X):
    # (1/n)(sum(X(i)-mu)^2)
    mu = media(X)

    res = 0
    for x in X:
        res += (x - mu) ** 2

    return res / len(X)

def desviacion_estandar(X):
    # Raiz cuadrada de la varianza
    return varianza(X) ** 0.5


if __name__ == "__main__":
    # X - Se refiere a un arreglo de datos
    # mu - Media
    X = [random.randint(1,21) for i in range(20)]
    mu = media(X)
    var = varianza(X)
    sigma = desviacion_estandar(X) # Que tanta variabilidad habra entre los datos

    print(f"Arreglo de datos: {X}")
    print(f"Media: {mu}")
    print(f"Varianza: {var}")
    print(f"Desviacion estandar: {sigma}")
