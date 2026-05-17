const sumar = (a, b) => a + b;
const restar = (a, b) => a - b;
const multiplicar = (a, b) => a * b;

describe('Pruebas Unitarias - Matematicas de la App', () => {
  
  test('QA-1: Debería sumar dos números enteros correctamente', () => {
    expect(sumar(10, 5)).toBe(15);
  });

  test('QA-2: Debería restar dos números enteros correctamente', () => {
    expect(restar(10, 5)).toBe(5);
  });

  test('QA-3: Debería multiplicar dos números enteros correctamente', () => {
    expect(multiplicar(10, 5)).toBe(50);
  });

});
