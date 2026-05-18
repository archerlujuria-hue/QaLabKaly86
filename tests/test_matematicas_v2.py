import unittest

# Funciones a probar
def sumar(a, b):
    return a + b

def restar(a, b):
    return a - b

def multiplicar(a, b):
    return a * b

# Clase de pruebas unitarias en Python (Versión 2)
class TestMatematicasPythonV2(unittest.TestCase):

    # ⚠️ REGLA DE ORO DE PYTHON:
    # En Python, los nombres de funciones NO pueden llevar guiones medios (-) porque Python piensa que es una resta.
    # Por ejemplo, escribir "def test_SCRUM-8_suma" dará un error de sintaxis.
    
    # 💡 SOLUCIÓN XRAY:
    # En Python, reemplazamos el guion medio (-) por un guion bajo (_). 
    # Xray es súper inteligente y detectará automáticamente que "SCRUM_8" corresponde a la tarea "SCRUM-8" en Jira!

    # Estos tests ya existirán en tu Jira después de la primera ejecución (ej. creados como SCRUM_8, SCRUM_9, SCRUM_10)
    
    def test_SCRUM_8_deberia_sumar_correctamente(self):
        self.assertEqual(sumar(10, 5), 15)

    def test_SCRUM_9_deberia_restar_correctamente(self):
        self.assertEqual(restar(10, 5), 5)

    def test_SCRUM_10_deberia_multiplicar_correctamente(self):
        self.assertEqual(multiplicar(10, 5), 50)

    # ⚠️ TEST QUE FALLA A PROPÓSITO EN PYTHON:
    # Este test está diseñado para fallar y así poder comprobar el detalle del error en Jira y en tu reporte HTML de Python.
    def test_QA_8_deberia_fallar_a_proposito_para_verificar_reporte(self):
        valor_esperado = 100
        valor_obtenido = 50 + 40 # Esto dará 90
        self.assertEqual(valor_obtenido, valor_esperado) # Fallará porque 90 != 100

