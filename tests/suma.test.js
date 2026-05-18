const sumar = (a, b) => a + b;
const restar = (a, b) => a - b;
const multiplicar = (a, b) => a * b;
const dividir = (a, b) => b === 0 ? null : a / b;

describe('Pruebas Unitarias - Matematicas de la App V2', () => {
  
  // Estos tests ya existen en tu Jira con las claves SCRUM-5, SCRUM-6 y SCRUM-7.
  // Al poner la clave exacta al inicio, Xray sabrá que debe actualizar esas tareas existentes.
  
  test('SCRUM-5: Debería sumar dos números enteros correctamente', () => {
    expect(sumar(10, 5)).toBe(15);
  });

  test('SCRUM-6: Debería restar dos números enteros correctamente', () => {
    expect(restar(10, 5)).toBe(5);
  });

  test('SCRUM-7: Debería multiplicar dos números enteros correctamente', () => {
    expect(multiplicar(10, 5)).toBe(50);
  });

  // Este es un test NUEVO. Como no tiene clave de Jira, Xray creará una nueva actividad automáticamente (SCRUM-8)
  test('QA-4: Debería dividir dos números enteros correctamente', () => {
    expect(dividir(10, 2)).toBe(5);
  });

});
