reamur = float(input("Masukan suhu celcius: "))

celcius = 0.0
fahrenheit = 0.0
kelvin = 0.0

formulaCelcius = 5 / 4 * reamur
formulaFahrenheit = 9 / 4 * reamur + 32
formulaKelvin = 5 / 4 * reamur + 273.15

print("Suhu Reamur %.2f -> Suhu Celcius: %.2f" % (reamur, formulaCelcius) )
print("Suhu Reamur %.2f -> Suhu Fahrenheit: %.2f" % (reamur, formulaFahrenheit))
print("Suhu Reamur %.2f -> Suhu Kelvin: %.2f" % (reamur, formulaKelvin))
