reamur = float(input("Masukan suhu celcius: "))

celcius = 0.0
fahrenheit = 0.0
kelvin = 0.0

rumusCelcius = 5 / 4 * reamur
rumusFahrenheit = 9 / 4 * reamur + 32
rumusKelvin = 5 / 4 * reamur + 273.15

print("Suhu Reamur %.2f -> Suhu Celcius: %.2f" % (reamur, rumusCelcius))
print("Suhu Reamur %.2f -> Suhu Fahrenheit: %.2f" % (reamur, rumusFahrenheit))
print("Suhu Reamur %.2f -> Suhu Kelvin: %.2f" % (reamur, rumusKelvin))
