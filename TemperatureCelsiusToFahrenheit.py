def temperature(celsius):
    return (celsius * 9 / 5) + 32
temp = float(input("Enter the temperature in  Celsius: "))
fahrenheit = temperature(temp)
print(f"The temperature in Fahrenheit is {fahrenheit:.2f} F")