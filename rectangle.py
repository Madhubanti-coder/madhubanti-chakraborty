def area_of_rectangle(length, width):
    return length * width

def area_of_square(side):
    return side**2

# Menu-driven program
print("1. Area of Rectangle")
print("2. Area of Square")
choice = int(input("Enter your choice: "))
if choice == 1:
    length = float(input("Enter the length: "))
    width = float(input("Enter the width: "))
    print(f"Area of the rectangle is {area_of_rectangle(length, width)}")
elif choice == 2:
    side = float(input("Enter the side length: "))
    print(f"Area of the square is {area_of_square(side)}")
else:
    print("Invalid choice!")