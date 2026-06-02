const { add, subtract, multiply, divide } = require('../src/calculator');

test('add returns sum', () => {
  expect(add(2, 3)).toBe(5);
});

test('subtract returns difference', () => {
  expect(subtract(5, 2)).toBe(3);
});

test('multiply returns product', () => {
  expect(multiply(3, 4)).toBe(12);
});

test('divide returns quotient', () => {
  expect(divide(10, 2)).toBe(5);
});

test('divide by zero throws', () => {
  expect(() => divide(1, 0)).toThrow('Cannot divide by zero!');
});
