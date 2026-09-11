# Program Konversi Suhu Celsius

KELVIN_OFFSET = 273.15

celsius = float(input("Masukkan suhu Celsius: "))

fahrenheit = (9 / 5) * celsius + 32
kelvin = celsius + KELVIN_OFFSET

print("Suhu Celsius   :", celsius, "°C")
print("Suhu Fahrenheit:", fahrenheit, "°F")
print("Suhu Kelvin    :", kelvin, "K")
