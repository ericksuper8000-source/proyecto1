from Principal import suma, division, es_par


def test_suma():
    assert suma(2, 3) == 5


def test_division():
    assert division(10, 2) == 5.0


def test_es_par_true():
    assert es_par(4) is True


def test_es_par_false():
    assert es_par(5) is False
