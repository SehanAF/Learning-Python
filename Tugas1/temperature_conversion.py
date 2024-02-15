reamur = float(input("Masukan suhu celcius: "))

formulaCelcius = 5 / 4 * reamur
formulaFahrenheit = 9 / 4 * reamur + 32
formulaKelvin = 5 / 4 * reamur + 273.15

print("Suhu Reamur %.2f -> Suhu Celcius: %.2f Derajat Celcius" % (reamur, formulaCelcius) )
print("Suhu Reamur %.2f -> Suhu Fahrenheit: %.2f Derajat Fahrenheit" % (reamur, formulaFahrenheit))
print("Suhu Reamur %.2f -> Suhu Kelvin: %.2f Derajat Kelvin" % (reamur, formulaKelvin))
