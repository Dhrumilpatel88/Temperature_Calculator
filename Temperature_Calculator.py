# Constants 
C_TO_F = 9/5
C_TO_K = 273.15
F_TO_C = 5/9
F_TO_K = 273.15
K_TO_C = -273.15
K_TO_F = 9/5

input_temperature = float(input("Enter the tempreture : "))
selected_temperature = input("Enter Celsius ,Fahrenheit or Kelvin : ").lower()
    
if selected_temperature == 'Celsius':
        Celsius = input_temperature
        print("Temperature in Celsius : ",Celsius)
        Fahrenheit = Celsius * C_TO_F + 32
        print("Temperature in Fahrenheit : ",Fahrenheit)
        Kelvin = Celsius + C_TO_K
        print("Temperature in Celsius : ",Kelvin)
elif selected_temperature == 'Fahrenheit':
        Fahrenheit = input_temperature
        print("Temperature in Fahrenheit : ",Fahrenheit)
        Celsius = (Fahrenheit - 32) * F_TO_C
        print("Temperature in Celsius : ",Celsius)
        Kelvin = (Fahrenheit - 32) * F_TO_C + C_TO_K
        print("Temperature in Kelvin : ",Kelvin)
else:
        Kelvin = input_temperature
        print("Temperature in Kelvin : ",Kelvin)
        Celsius = Kelvin + K_TO_C
        print("Temperature in Celsius : ",Celsius)
        Fahrenheit = Kelvin * K_TO_F + 32
        print("Temperature in Fahrenheit : ",Fahrenheit)
    
   