def CtoF(C):
    fahrenheit = C * (9.0/5.0) + 32
    return fahrenheit

celcius = input("What celcius value would you like to convert:")
print(CtoF(celcius))