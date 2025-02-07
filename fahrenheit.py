def fahrenheit_to_celsius(f):
    return (f - 32) * 5/9

def celsius_to_fahrenheit(c):
    return (c * 9/5) + 32

# Menu-driven program
print("1. Fahrenheit to Celsius")
print("2. Celsius to Fahrenheit")
choice = int(input("Enter your choice: "))
if choice == 1:
    f = float(input("Enter temperature in Fahrenheit: "))
    print(f"{f}°F is {fahrenheit_to_celsius(f):.2f}°C")
elif choice == 2:
    c = float(input("Enter temperature in Celsius: "))
    print(f"{c}°C is {celsius_to_fahrenheit(c):.2f}°F")
else:
    print("Invalid choice!")