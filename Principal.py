def calcular_precio_final(precio_base, descuento):
    """
    Calcula el precio final aplicando un porcentaje de descuento.
    El descuento debe estar entre 0 y 100.
    """
    if not isinstance(precio_base, (int, float)) or not isinstance(descuento, (int, float)):
        raise ValueError("Ambos argumentos deben ser numéricos")

    if descuento < 0 or descuento > 100:
        raise ValueError("El descuento debe estar entre 0 y 100")

    reduccion = precio_base * (descuento / 100)
    return precio_base - reduccion


def formatear_nombre_producto(nombre):
    """
    Limpia espacios y pone en mayúsculas el nombre de un producto.
    """
    if not nombre:
        return ""
    return nombre.strip().upper()


if __name__ == "__main__":
    # Ejemplo de uso rápido
    p_final = calcular_precio_final(100, 15)
    print(f"Precio con descuento: {p_final}")