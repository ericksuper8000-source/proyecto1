from Principal import sumar, dividir, es_par
import pytest


def test_sumar():
    assert sumar(2, 3) == 5


def test_dividir():
    assert dividir(10, 2) == 5


def test_dividir_cero():
    with pytest.raises(ValueError):
        dividir(10, 0)


def test_es_par():
    assert es_par(4) is True
    assert es_par(5) is False
