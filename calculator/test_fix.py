from pkg.calculator import Calculator

calc = Calculator()
result = calc.evaluate("3 + 7 * 2")
print(f"3 + 7 * 2 = {result}")  # Expected: 17.0

result2 = calc.evaluate("3 * 7 + 2")
print(f"3 * 7 + 2 = {result2}")  # Expected: 23.0

result3 = calc.evaluate("2 + 3 * 4")
print(f"2 + 3 * 4 = {result3}")  # Expected: 14.0
