'''
Zavier Philpot
Area and Perimeter

'''
import math

print("Choose a shape to calculate its area:")
print("1. Rectangle")
print("2. Circle")
print("3. Triangle")
print("4. Parallelogram")

choice = int(input("Enter choice (1-4): "))

shape = ""
length = 0
width = 0
radius = 0
base = 0
height = 0

if choice == 1:
    shape = "rectangle"
    length = float(input("Enter length of rectangle: "))
    width = float(input("Enter width of rectangle: "))
    area = length * width
elif choice == 2:
    shape = "circle"
    radius = float(input("Enter radius of circle: "))
    area = math.pi * radius ** 2
elif choice == 3:
    shape = "triangle"
    base = float(input("Enter base of triangle: "))
    height = float(input("Enter height of triangle: "))
    area = 0.5 * base * height
elif choice == 4:
    shape = "parallelogram"
    base = float(input("Enter base of parallelogram: "))
    height = float(input("Enter height of parallelogram: "))
    area = base * height
else:
    print("Invalid choice")
    exit()

print(f"The area of the {shape} is {area}")

# Store the user's input in a dictionary
user_input = {"shape": shape, "length": length, "width": width, "radius": radius, "base": base, "height": height}

# Display the user's input
print("You entered:")
for key, value in user_input.items():
    if value != 0:
        print(f"{key.capitalize()}: {value}")
