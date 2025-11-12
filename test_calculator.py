"""
Unit tests for calculator modules.
Ensures both the before and after versions produce identical results.
"""

import unittest
import sys
from io import StringIO

# Import both versions
import calculator_before
import calculator_after


class TestCalculatorConsistency(unittest.TestCase):
    """Test that both versions produce the same results."""
    
    def test_rectangle_area(self):
        """Test rectangle area calculation."""
        # Suppress print output for tests
        old_stdout = sys.stdout
        sys.stdout = StringIO()
        
        result_before = calculator_before.calculate_rectangle_area(5, 3)
        result_after = calculator_after.calculate_rectangle_area(5, 3)
        
        sys.stdout = old_stdout
        
        self.assertEqual(result_before, result_after)
        self.assertEqual(result_before, 15)
    
    def test_rectangle_perimeter(self):
        """Test rectangle perimeter calculation."""
        old_stdout = sys.stdout
        sys.stdout = StringIO()
        
        result_before = calculator_before.calculate_rectangle_perimeter(5, 3)
        result_after = calculator_after.calculate_rectangle_perimeter(5, 3)
        
        sys.stdout = old_stdout
        
        self.assertEqual(result_before, result_after)
        self.assertEqual(result_before, 16)
    
    def test_circle_area(self):
        """Test circle area calculation."""
        old_stdout = sys.stdout
        sys.stdout = StringIO()
        
        result_before = calculator_before.calculate_circle_area(4)
        result_after = calculator_after.calculate_circle_area(4)
        
        sys.stdout = old_stdout
        
        self.assertEqual(result_before, result_after)
        self.assertAlmostEqual(result_before, 50.26544, places=5)
    
    def test_circle_circumference(self):
        """Test circle circumference calculation."""
        old_stdout = sys.stdout
        sys.stdout = StringIO()
        
        result_before = calculator_before.calculate_circle_circumference(4)
        result_after = calculator_after.calculate_circle_circumference(4)
        
        sys.stdout = old_stdout
        
        self.assertEqual(result_before, result_after)
        self.assertAlmostEqual(result_before, 25.13272, places=5)
    
    def test_triangle_area(self):
        """Test triangle area calculation."""
        old_stdout = sys.stdout
        sys.stdout = StringIO()
        
        result_before = calculator_before.calculate_triangle_area(6, 4)
        result_after = calculator_after.calculate_triangle_area(6, 4)
        
        sys.stdout = old_stdout
        
        self.assertEqual(result_before, result_after)
        self.assertEqual(result_before, 12.0)
    
    def test_square_area(self):
        """Test square area calculation."""
        old_stdout = sys.stdout
        sys.stdout = StringIO()
        
        result_before = calculator_before.calculate_square_area(5)
        result_after = calculator_after.calculate_square_area(5)
        
        sys.stdout = old_stdout
        
        self.assertEqual(result_before, result_after)
        self.assertEqual(result_before, 25)
    
    def test_square_perimeter(self):
        """Test square perimeter calculation."""
        old_stdout = sys.stdout
        sys.stdout = StringIO()
        
        result_before = calculator_before.calculate_square_perimeter(5)
        result_after = calculator_after.calculate_square_perimeter(5)
        
        sys.stdout = old_stdout
        
        self.assertEqual(result_before, result_after)
        self.assertEqual(result_before, 20)
    
    def test_negative_input_rectangle(self):
        """Test that negative inputs are rejected."""
        old_stdout = sys.stdout
        sys.stdout = StringIO()
        
        result_before = calculator_before.calculate_rectangle_area(-5, 3)
        result_after = calculator_after.calculate_rectangle_area(-5, 3)
        
        sys.stdout = old_stdout
        
        self.assertIsNone(result_before)
        self.assertIsNone(result_after)
    
    def test_zero_input_circle(self):
        """Test that zero inputs are rejected."""
        old_stdout = sys.stdout
        sys.stdout = StringIO()
        
        result_before = calculator_before.calculate_circle_area(0)
        result_after = calculator_after.calculate_circle_area(0)
        
        sys.stdout = old_stdout
        
        self.assertIsNone(result_before)
        self.assertIsNone(result_after)


class TestRefactoredFeatures(unittest.TestCase):
    """Test new features in the refactored version."""
    
    def test_shape_classes(self):
        """Test that shape classes work correctly."""
        old_stdout = sys.stdout
        sys.stdout = StringIO()
        
        rect = calculator_after.Rectangle(10, 5)
        circle = calculator_after.Circle(3)
        square = calculator_after.Square(4)
        triangle = calculator_after.Triangle(8, 5)
        
        sys.stdout = old_stdout
        
        self.assertEqual(rect.area(), 50)
        self.assertEqual(rect.perimeter(), 30)
        self.assertAlmostEqual(circle.area(), 28.27431, places=5)
        self.assertAlmostEqual(circle.perimeter(), 18.84954, places=5)
        self.assertEqual(square.area(), 16)
        self.assertEqual(square.perimeter(), 16)
        self.assertEqual(triangle.area(), 20.0)
    
    def test_validation_function(self):
        """Test the extracted validation function."""
        self.assertIsNone(calculator_after.validate_positive(1, 2, 3))
        self.assertIsNotNone(calculator_after.validate_positive(1, -2, 3))
        self.assertIsNotNone(calculator_after.validate_positive(0))
    
    def test_pi_constant(self):
        """Test that PI constant is defined correctly."""
        self.assertEqual(calculator_after.PI, 3.14159)


if __name__ == "__main__":
    # Run tests
    unittest.main(verbosity=2)
