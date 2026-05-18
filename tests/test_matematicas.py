import unittest

# Funciones a probar
def sumar(a, b):
    return a + b

def restar(a, b):
    return a - b

def multiplicar(a, b):
    return a * b

# Clase de pruebas unitarias en Python
class TestMatematicasPython(unittest.TestCase):

    # Xray de Jira leerá el nombre de cada método de test.
    # Al igual que en JS, si pones un código identificador (como QA-5, QA-6) al inicio del nombre del método,
    # Xray creará la tarea de test automáticamente.
    
    def test_QA_5_deberia_sumar_correctamente(self):
        self.assertEqual(sumar(10, 5), 15)

    def test_QA_6_deberia_restar_correctamente(self):
        self.assertEqual(restar(10, 5), 5)

    def test_QA_7_deberia_multiplicar_correctamente(self):
        self.assertEqual(multiplicar(10, 5), 50)

if __name__ == '__main__':
    unittest.main()
