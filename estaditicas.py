import random

def media(x):
    return sum(x) / len(x)

if __name__ == "__main__":
    X = [random.randint(1,21) for i in range(20)]
    mu = media(X)

    print(X)
    print(mu)