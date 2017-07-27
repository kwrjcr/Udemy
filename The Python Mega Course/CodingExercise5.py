temperatures = [10, -20, -289, 100]


def celsiusToFahrenheit(celsius):
    if float(celsius) < -273.15:
        return ''
    else:
        fahrenheit = float(celsius) * (9.0/5.0) + 32
        return str(fahrenheit) + '\n'


with open('temperatures.txt', 'w') as file:
    for temp in temperatures:
        file.write(celsiusToFahrenheit(temp))
        