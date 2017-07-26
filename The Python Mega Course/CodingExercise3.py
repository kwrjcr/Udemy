def CtoF(C):
    
    if float(C) < -273.15:
        message = "That is below the possible tempertures physical matter can take"
        return message
    else:
        fahrenheit = C * (9.0/5.0) + 32
        return fahrenheit

#celcius = input("What celcius value would you like to convert:")
#print(CtoF(celcius))