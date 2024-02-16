reamur = float(input("Masukan suhu celcius: "))

formula_celcius = 5 / 4 * reamur
formula_fahrenheit = 9 / 4 * reamur + 32
formula_kelvin = 5 / 4 * reamur + 273.15

print(f"Suhu Reamur {reamur:.2f} -> Suhu Celcius: {formula_celcius:.2f} Derajat Celcius" )
print(f"Suhu Reamur {reamur:.2f} -> Suhu Fahrenheit: {formula_fahrenheit:.2f} Derajat Fahrenheit")
print(f"Suhu Reamur {reamur:.2f} -> Suhu Kelvin: {formula_kelvin:.2f} Derajat Kelvin ")
