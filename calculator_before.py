"""
Calculator module - BEFORE refactoring
This file contains duplicated code that needs to be refactored.
"""


def calculate_rectangle_area(length, width):
    """Calculate the area of a rectangle."""
    if length <= 0:
        print("Error: length must be positive")
        return None
    if width <= 0:
        print("Error: width must be positive")
        return None
    
    area = length * width
    print(f"Calculating rectangle area: {length} x {width} = {area}")
    return area


def calculate_circle_area(radius):
    """Calculate the area of a circle."""
    if radius <= 0:
        print("Error: radius must be positive")
        return None
    
    pi = 3.14159
    area = pi * radius * radius
    print(f"Calculating circle area: π x {radius}² = {area}")
    return area


def calculate_triangle_area(base, height):
    """Calculate the area of a triangle."""
    if base <= 0:
        print("Error: base must be positive")
        return None
    if height <= 0:
        print("Error: height must be positive")
        return None
    
    area = 0.5 * base * height
    print(f"Calculating triangle area: 0.5 x {base} x {height} = {area}")
    return area


def calculate_rectangle_perimeter(length, width):
    """Calculate the perimeter of a rectangle."""
    if length <= 0:
        print("Error: length must be positive")
        return None
    if width <= 0:
        print("Error: width must be positive")
        return None
    
    perimeter = 2 * (length + width)
    print(f"Calculating rectangle perimeter: 2 x ({length} + {width}) = {perimeter}")
    return perimeter


def calculate_circle_circumference(radius):
    """Calculate the circumference of a circle."""
    if radius <= 0:
        print("Error: radius must be positive")
        return None
    
    pi = 3.14159
    circumference = 2 * pi * radius
    print(f"Calculating circle circumference: 2 x π x {radius} = {circumference}")
    return circumference


def calculate_square_area(side):
    """Calculate the area of a square."""
    if side <= 0:
        print("Error: side must be positive")
        return None
    
    area = side * side
    print(f"Calculating square area: {side} x {side} = {area}")
    return area


def calculate_square_perimeter(side):
    """Calculate the perimeter of a square."""
    if side <= 0:
        print("Error: side must be positive")
        return None
    
    perimeter = 4 * side
    print(f"Calculating square perimeter: 4 x {side} = {perimeter}")
    return perimeter


# Example usage
if __name__ == "__main__":
    print("=== Rectangle ===")
    calculate_rectangle_area(5, 3)
    calculate_rectangle_perimeter(5, 3)
    
    print("\n=== Circle ===")
    calculate_circle_area(4)
    calculate_circle_circumference(4)
    
    print("\n=== Triangle ===")
    calculate_triangle_area(6, 4)
    
    print("\n=== Square ===")
    calculate_square_area(5)
    calculate_square_perimeter(5)
    
    print("\n=== Error Cases ===")
    calculate_rectangle_area(-5, 3)
    calculate_circle_area(0)
