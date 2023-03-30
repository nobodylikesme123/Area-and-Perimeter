'''
Zavier Philpot
Area and Perimeter

'''
import math

class ShapeCalculator:
    def __init__(self):
        self.shape = ""

    def get_shape(self):
        self.shape = input("Enter a shape (rectangle, circle, triangle, parallelogram): ")

    def calculate_area(self):
        if self.shape == "rectangle":
            length = float(input("Enter length: "))
            width = float(input("Enter width: "))
            area = length * width
            print(f"The area of the rectangle is: {area}")
        elif self.shape == "circle":
            radius = float(input("Enter radius: "))
            area = math.pi * radius**2
            print(f"The area of the circle is: {area}")
        elif self.shape == "triangle":
            base = float(input("Enter base: "))
            height = float(input("Enter height: "))
            area = 0.5 * base * height
            print(f"The area of the triangle is: {area}")
        elif self.shape == "parallelogram":
            base = float(input("Enter base: "))
            height = float(input("Enter height: "))
            area = base * height
            print(f"The area of the parallelogram is: {area}")
        else:
            print("Invalid shape entered.")

    def calculate_perimeter(self):
        if self.shape == "rectangle":
            length = float(input("Enter length: "))
            width = float(input("Enter width: "))
            perimeter = 2 * (length + width)
            print(f"The perimeter of the rectangle is: {perimeter}")
        elif self.shape == "circle":
            radius = float(input("Enter radius: "))
            perimeter = 2 * math.pi * radius
            print(f"The perimeter of the circle is: {perimeter}")
        elif self.shape == "triangle":
            side1 = float(input("Enter side 1: "))
            side2 = float(input("Enter side 2: "))
            side3 = float(input("Enter side 3: "))
            perimeter = side1 + side2 + side3
            print(f"The perimeter of the triangle is: {perimeter}")
        elif self.shape == "parallelogram":
            side1 = float(input("Enter side 1: "))
            side2 = float(input("Enter side 2: "))
            perimeter = 2 * (side1 + side2)
            print(f"The perimeter of the parallelogram is: {perimeter}")
        else:
            print("Invalid shape entered.")


calculator = ShapeCalculator()
while True:
    calculator.get_shape()
    calculator.calculate_area()
    calculator.calculate_perimeter()
    repeat = input("Do you want to calculate another shape? (Y/N)").lower()
    if repeat != "y":
        break