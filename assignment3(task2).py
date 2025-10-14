import math
try:
    num_str = input("Please enter a number: ")
    num = float(num_str)
    if num >= 0:
        square_root = math.sqrt(num)
        print(f"The square root of {num} is: {square_root}")
    else:
        print(f"Cannot calculate the square root of a negative number ({num}) using math.sqrt().")
    if num > 0:
        natural_log = math.log(num)
        print(f"The natural logarithm (log base e) of {num} is: {natural_log}")
    else:
        print(f"Cannot calculate the natural logarithm of a non-positive number ({num}).")
    sine_value = math.sin(num)
    print(f"The sine of {num} (in radians) is: {sine_value}")

except ValueError:
    print("Invalid input. Please enter a valid number.")