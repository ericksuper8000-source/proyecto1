import time


def suma(a, b):
    return a + b


def division(a, b):
    return a / b


def es_par(n):
    return n % 2 == 0


if __name__ == "__main__":
    while True:
        print("Suma:", suma(2, 3))
        print("División:", division(10, 2))
        print("¿Es par?:", es_par(4))
        print("---- ejecutándose ----\n")

        time.sleep(5)
        
# Este es mi primer comentario