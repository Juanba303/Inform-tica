# Se pide la temperatura en Celsius y se pasa a Fahrenheit
celsius = float(input("Temperatura en Celsius: "))
print(f"{celsius}°C equivalen a {celsius * 9/5 + 32:.2f}°F")

# Se pide la temperatura en Fahrenheit y se pasa a Celsius
fahrenheit = float(input("Temperatura en Fahrenheit: "))
print(f"{fahrenheit}°F equivalen a {(fahrenheit - 32) * 5/9:.2f}°C")