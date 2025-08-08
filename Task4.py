def perform_operations(a, b):
    addition = a + b
    subtraction = a - b
    multiplication = a * b
    if b != 0:
        division = a / b
    else:
        division = None  # Avoid division by zero
    return addition, subtraction, multiplication, division

# Example usage:
result = perform_operations(10, 5)
print("Addition:", result[0])
print("Subtraction:", result[1])
print("Multiplication:", result[2])
print("Division:", result[3])