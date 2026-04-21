import unittest
from Principal import calcular_precio_final, formatear_nombre_producto

class TestPrincipal(unittest.TestCase):

    def test_descuento_valido(self):
        self.assertEqual(calcular_precio_final(100, 20), 80.0)
        self.assertEqual(calcular_precio_final(50, 0), 50.0)

    def test_descuento_invalido(self):
        with self.assertRaises(ValueError):
            calcular_precio_final(100, 150)
        with self.assertRaises(ValueError):
            calcular_precio_final(100, -5)

    def test_formatear_nombre(self):
        self.assertEqual(formatear_nombre_producto("  laptop  "), "LAPTOP")
        self.assertEqual(formatear_nombre_producto("mouse"), "MOUSE")

if __name__ == "__main__":
    unittest.main()
