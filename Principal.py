import sys


def calcular_descuento(precio: float, porcentaje: float) -> float:
    """
    Calcula el precio final tras aplicar un descuento.
    """
    if not (0 <= porcentaje <= 100):
        raise ValueError("El porcentaje debe estar entre 0 y 100")

    descuento = precio * (porcentaje / 100)
    return precio - descuento


def main():
    print("--- Sistema de Gestión de Cupones ---")

    try:
        precio_inicial = 150.0
        tasa_descuento = 15.0

        resultado = calcular_descuento(precio_inicial, tasa_descuento)

        print(f"Precio original: ${precio_inicial}")
        print(f"Descuento aplicado: {tasa_descuento}%")
        print(f"Precio final: ${resultado}")

    except ValueError as e:
        print(f"Error en los datos: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()