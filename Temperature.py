def temperature(fahrenheit):
    return(fahrenheit - 32) * 5 / 9
temp = float(input("Enter temperature in fahrenheit: "))
celsius = (temperature(temp))
print(f"The temperature in celsius is {celsius:.2f} C")
