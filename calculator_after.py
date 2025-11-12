"""
Calculator module - AFTER refactoring
This file demonstrates how duplicated code has been refactored into reusable components.

Key improvements:
1. Extracted validation logic into a reusable function
2. Extracted logging/output logic into a decorator
3. Consolidated constants (PI) into a single location
4. Created a base class structure for better organization
"""

import functools
from typing import List, Optional


# Constants
PI = 3.14159


def validate_positive(*values: float) -> Optional[str]:
    """
    Validate that all values are positive.
    
    Args:
        *values: Variable number of values to validate
    
    Returns:
        Error message if validation fails, None otherwise
    """
    for i, value in enumerate(values):
        if value <= 0:
            param_name = f"parameter {i + 1}"
            return f"Error: {param_name} must be positive"
    return None


def log_calculation(operation_name: str):
    """
    Decorator to log calculation operations.
    
    Args:
        operation_name: Name of the operation being performed
    """
    def decorator(func):
        @functools.wraps(func)
        def wrapper(self, *args, **kwargs):
            result = func(self, *args, **kwargs)
            if result is not None:
                # Format dimensions for display
                dims_str = ", ".join(str(dim) for dim in self.dimensions)
                print(f"Calculating {operation_name}: {dims_str} = {result:.5f}")
            return result
        return wrapper
    return decorator


class Shape:
    """Base class for geometric shapes."""
    
    def __init__(self, *dimensions: float):
        """
        Initialize shape with dimensions.
        
        Args:
            *dimensions: Variable number of dimension values
        """
        self.dimensions = dimensions
        self.is_valid = self._validate()
    
    def _validate(self) -> bool:
        """Validate shape dimensions."""
        error = validate_positive(*self.dimensions)
        if error:
            print(error)
            return False
        return True
    
    def area(self) -> Optional[float]:
        """Calculate area. To be implemented by subclasses."""
        raise NotImplementedError
    
    def perimeter(self) -> Optional[float]:
        """Calculate perimeter. To be implemented by subclasses."""
        raise NotImplementedError


class Rectangle(Shape):
    """Rectangle shape."""
    
    def __init__(self, length: float, width: float):
        super().__init__(length, width)
        self.length = length
        self.width = width
    
    @log_calculation("rectangle area")
    def area(self) -> Optional[float]:
        """Calculate rectangle area."""
        if not self.is_valid:
            return None
        return self.length * self.width
    
    @log_calculation("rectangle perimeter")
    def perimeter(self) -> Optional[float]:
        """Calculate rectangle perimeter."""
        if not self.is_valid:
            return None
        return 2 * (self.length + self.width)


class Circle(Shape):
    """Circle shape."""
    
    def __init__(self, radius: float):
        super().__init__(radius)
        self.radius = radius
    
    @log_calculation("circle area")
    def area(self) -> Optional[float]:
        """Calculate circle area."""
        if not self.is_valid:
            return None
        return PI * self.radius * self.radius
    
    @log_calculation("circle circumference")
    def perimeter(self) -> Optional[float]:
        """Calculate circle circumference."""
        if not self.is_valid:
            return None
        return 2 * PI * self.radius


class Triangle(Shape):
    """Triangle shape."""
    
    def __init__(self, base: float, height: float):
        super().__init__(base, height)
        self.base = base
        self.height = height
    
    @log_calculation("triangle area")
    def area(self) -> Optional[float]:
        """Calculate triangle area."""
        if not self.is_valid:
            return None
        return 0.5 * self.base * self.height
    
    def perimeter(self) -> Optional[float]:
        """Not implemented for this simple triangle."""
        raise NotImplementedError("Perimeter calculation requires all side lengths")


class Square(Shape):
    """Square shape."""
    
    def __init__(self, side: float):
        super().__init__(side)
        self.side = side
    
    @log_calculation("square area")
    def area(self) -> Optional[float]:
        """Calculate square area."""
        if not self.is_valid:
            return None
        return self.side * self.side
    
    @log_calculation("square perimeter")
    def perimeter(self) -> Optional[float]:
        """Calculate square perimeter."""
        if not self.is_valid:
            return None
        return 4 * self.side


# Convenience functions for backward compatibility
def calculate_rectangle_area(length: float, width: float) -> Optional[float]:
    """Calculate rectangle area."""
    rect = Rectangle(length, width)
    return rect.area()


def calculate_rectangle_perimeter(length: float, width: float) -> Optional[float]:
    """Calculate rectangle perimeter."""
    rect = Rectangle(length, width)
    return rect.perimeter()


def calculate_circle_area(radius: float) -> Optional[float]:
    """Calculate circle area."""
    circle = Circle(radius)
    return circle.area()


def calculate_circle_circumference(radius: float) -> Optional[float]:
    """Calculate circle circumference."""
    circle = Circle(radius)
    return circle.perimeter()


def calculate_triangle_area(base: float, height: float) -> Optional[float]:
    """Calculate triangle area."""
    triangle = Triangle(base, height)
    return triangle.area()


def calculate_square_area(side: float) -> Optional[float]:
    """Calculate square area."""
    square = Square(side)
    return square.area()


def calculate_square_perimeter(side: float) -> Optional[float]:
    """Calculate square perimeter."""
    square = Square(side)
    return square.perimeter()


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
    
    print("\n=== Using Object-Oriented Approach ===")
    rect = Rectangle(10, 5)
    print(f"Rectangle area: {rect.area()}")
    print(f"Rectangle perimeter: {rect.perimeter()}")
