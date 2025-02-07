import math

def area_of_circle(radius):
    return math.pi * radius**2

# Menu-driven program
print("1. Calculate Area of Circle")
choice = int(input("Enter your choice: "))
if choice == 1:
    radius = float(input("Enter the radius of the circle: "))
    print(f"Area of the circle is {area_of_circle(radius):.2f}")
else:
    print("Invalid choice!")