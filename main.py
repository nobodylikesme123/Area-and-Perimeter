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

if choice == 1:
    length = float(input("Enter length of rectangle: "))
    width = float(input("Enter width of rectangle: "))
    area = length * width
    print("The area of the rectangle is", area)
elif choice == 2:
    radius = float(input("Enter radius of circle: "))
    area = math.pi * radius ** 2
    print("The area of the circle is", area)
elif choice == 3:
    base = float(input("Enter base of triangle: "))
    height = float(input("Enter height of triangle: "))
    area = 0.5 * base * height
    print("The area of the triangle is", area)
elif choice == 4:
    base = float(input("Enter base of parallelogram: "))
    height = float(input("Enter height of parallelogram: "))
    area = base * height
    print("The area of the parallelogram is", area)
else:
    print("Invalid choice")

