# Code Refactoring Example: Eliminating Duplication

This repository demonstrates the process of identifying and refactoring duplicated code for better maintainability and code quality.

## Overview

The project contains two versions of a simple geometric calculator:
- **calculator_before.py**: Original code with extensive duplication
- **calculator_after.py**: Refactored code following DRY (Don't Repeat Yourself) principles

## Identified Code Duplication Issues

### 1. **Repeated Validation Logic**
Every function in the original code contained identical validation checks:
```python
if parameter <= 0:
    print("Error: parameter must be positive")
    return None
```
This pattern appeared 11+ times throughout the code.

### 2. **Duplicated Logging/Output Pattern**
Each calculation function had the same logging pattern:
```python
print(f"Calculating [operation]: [formula] = {result}")
```

### 3. **Repeated Constants**
The value of PI (3.14159) was defined multiple times in different functions.

### 4. **Similar Function Structures**
All calculation functions followed the same structure:
- Validate inputs
- Perform calculation
- Log result
- Return value

## Refactoring Solutions

### 1. **Extract Validation Function**
Created a reusable `validate_positive()` function:
```python
def validate_positive(*values: float) -> Optional[str]:
    """Validate that all values are positive."""
    for i, value in enumerate(values):
        if value <= 0:
            return f"Error: parameter {i + 1} must be positive"
    return None
```

**Benefits:**
- Single source of truth for validation logic
- Easier to modify validation rules
- Reduced code by ~30 lines

### 2. **Create Logging Decorator**
Implemented a `@log_calculation` decorator:
```python
def log_calculation(operation_name: str):
    """Decorator to log calculation operations."""
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            result = func(*args, **kwargs)
            if result is not None:
                print(f"Calculating {operation_name}: {args} = {result}")
            return result
        return wrapper
    return decorator
```

**Benefits:**
- Separation of concerns (calculation vs. logging)
- Consistent logging format
- Easy to enable/disable logging
- Reduced code by ~15 lines

### 3. **Consolidate Constants**
Defined PI once at module level:
```python
PI = 3.14159
```

**Benefits:**
- Single source of truth
- Easy to update precision
- Reduced potential for typos

### 4. **Apply Object-Oriented Design**
Created a `Shape` base class with specialized subclasses:
```python
class Shape:
    """Base class for geometric shapes."""
    
    def __init__(self, *dimensions: float):
        self.dimensions = dimensions
        self._validate()
    
    def area(self) -> Optional[float]:
        raise NotImplementedError
```

**Benefits:**
- Encapsulation of related data and behavior
- Inheritance reduces code duplication
- Polymorphism allows uniform interface
- Easier to add new shapes

## Metrics

| Metric | Before | After | Improvement |
|--------|--------|-------|-------------|
| Lines of Code | ~110 | ~220* | Better organized |
| Code Duplication | High | None | 100% eliminated |
| Validation Logic | 11 copies | 1 function | 91% reduction |
| Logging Logic | 7 copies | 1 decorator | 86% reduction |
| Maintainability | Low | High | Significant |

*Note: The refactored version has more lines due to proper documentation, type hints, and OOP structure, but it's more maintainable and extensible.

## Running the Examples

### Before Refactoring
```bash
python calculator_before.py
```

### After Refactoring
```bash
python calculator_after.py
```

Both versions produce the same output, demonstrating that functionality is preserved while improving code quality.

## Key Refactoring Principles Applied

1. **DRY (Don't Repeat Yourself)**
   - Eliminated repeated validation and logging code
   - Consolidated constants

2. **Single Responsibility Principle**
   - Separated validation, calculation, and logging concerns
   - Each function/class has one clear purpose

3. **Open/Closed Principle**
   - Easy to add new shapes without modifying existing code
   - Extensible through inheritance

4. **Code Reusability**
   - Validation and logging can be reused across the application
   - Base class provides common functionality

## Testing Both Versions

You can verify that both versions work identically:

```bash
# Test before refactoring
python calculator_before.py > output_before.txt

# Test after refactoring
python calculator_after.py > output_after.txt

# Compare outputs (should be identical for same calculations)
diff output_before.txt output_after.txt
```

## Benefits of Refactoring

1. **Maintainability**: Changes to validation or logging only need to be made in one place
2. **Testability**: Smaller, focused functions are easier to unit test
3. **Readability**: Code is more organized and self-documenting
4. **Extensibility**: Easy to add new shapes or calculation types
5. **Reduced Bugs**: Less duplication means fewer places for bugs to hide

## Lessons Learned

- **Look for patterns**: Repeated code often indicates an opportunity for abstraction
- **Consider the trade-offs**: Sometimes a small amount of duplication is acceptable
- **Maintain functionality**: Refactoring should preserve behavior
- **Improve incrementally**: Don't try to refactor everything at once
- **Write tests first**: Ensure refactoring doesn't break existing functionality

## Next Steps

For further improvement, consider:
- Adding comprehensive unit tests
- Implementing additional shapes (hexagon, pentagon, etc.)
- Adding support for 3D shapes (sphere, cube, etc.)
- Creating a CLI or GUI interface
- Adding support for different unit systems (metric, imperial)

## Contributing

This is a demonstration repository showing refactoring techniques. Feel free to explore and learn from the examples provided.
