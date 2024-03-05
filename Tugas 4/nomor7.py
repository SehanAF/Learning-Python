# Program untuk mengonversi suhu dari Celsius ke Fahrenheit atau sebaliknya, sesuai dengan input pengguna.

celcius = float(input("Masukan suhu celcius: "))
fahrenheit = float(input("Masukan suhu celcius: "))

formula_celcius = 5 / 4 * fahrenheit
formula_fahrenheit = 9 / 4 * celcius + 32

print(f"Suhu Celcius {celcius:.2f} -> Suhu Fahrenheit: {formula_fahrenheit:.2f} Derajat Fahreinheit" )
print(f"Suhu Fahrenheit {fahrenheit:.2f} -> Suhu Celcius: {formula_celcius:.2f} Derajat Fahrenheit")