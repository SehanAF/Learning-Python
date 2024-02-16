reamur = float(input("Masukan suhu celcius: "))

formulaCelcius = 5 / 4 * reamur
formulaFahrenheit = 9 / 4 * reamur + 32
formulaKelvin = 5 / 4 * reamur + 273.15

print(f"Suhu Reamur {reamur:.2f} -> Suhu Celcius: {formulaCelcius:.2f} Derajat Celcius" )
print(f"Suhu Reamur {reamur:.2f} -> Suhu Fahrenheit: {formulaFahrenheit:.2f} Derajat Fahrenheit")
print(f"Suhu Reamur {reamur:.2f} -> Suhu Kelvin: {formulaKelvin:.2f} Derajat Kelvin ")
