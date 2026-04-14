from Principal import calcular_descuento
import pytest

def test_descuento_valido():
    # Caso normal: 10% de 100 es 10, resultado 90
    assert calcular_descuento(100, 10) == 90.0
    # Caso límite: 0% de descuento
    assert calcular_descuento(50, 0) == 50.0

def test_descuento_invalido():
    # Verificamos que lance error si el porcentaje es mayor a 100
    with pytest.raises(ValueError):
        calcular_descuento(100, 110)
