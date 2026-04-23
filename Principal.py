def sumar(a, b):
    return a + b


def dividir(a, b):
    if b == 0:
        raise ValueError("No se puede dividir entre cero")
    return a / b


def es_par(numero):
    return numero % 2 == 0


if __name__ == "__main__":
    print("Suma:", sumar(2, 3))
    print("División:", dividir(10, 2))
    print("¿Es par?:", es_par(4))
