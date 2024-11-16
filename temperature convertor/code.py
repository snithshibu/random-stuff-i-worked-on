#functions for conversion to minimize lines of code
def c_to_k(c): #Celsius to Kelvin
    return c + 273.15
def k_to_c(k): #Kelvin to Celsius
    return k - 273.15
def f_to_c(f): #Fahrenheit to Celsius
    return (f-32)*(5/9)
def c_to_f(c): #Celsius to Fahrenheit
    return c*(9/5) + 32
def f_to_k(f): #Fahrenheit to Kelvin
    return (f-32)*(5/9) + 273.15
def k_to_f(k): #Kelvin to Fahrenheit
    return (k-273.15)*(9/5) + 32

#Welcoming statement
print(f"Welcome to Temperature convertor. \nHere, you can convert temperature between Celsius, Fahrenheit and Kelvin.")
temp=int(input("Enter the value of temperature: "))
unit=input("Enter the unit (C/F/K): ").upper()

if unit == "C": #if user input celsius, output is in fahrenheit and kelvin
    print("In Kelvin,", c_to_k(temp))
    print("In Fahrenheit,", c_to_f(temp))

elif unit == "F": #if user input fahrenheit, output is in celsius and kelvin
    print("In Celsius,", f_to_c(temp))
    print("In Kelvin,", f_to_k(temp))

elif unit == "K": #if user input kelvin, output is in celsius and fahrenheit
    print("In Celsius,", k_to_c(temp))
    print("In Fahrenheit,", k_to_f(temp))

else:
    print("Enter valid unit of temperature, try again!")
