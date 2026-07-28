# =============================================================================
# PROGRAMMING FUNDAMENTALS — Assignment 3
# Topic: Lists (Arrays), Loops, and Functions
# =============================================================================
#
# TASK: Array Statistics Calculator
#
# Write a Python program that reads a collection of numbers from the user
# and computes key statistical values using separate functions.
#
# -----------------------------------------------------------------------------
# EXPECTED INPUT / OUTPUT EXAMPLE
# -----------------------------------------------------------------------------
#
#   How many numbers? 5
#   Enter number 1: 4
#   Enter number 2: 7
#   Enter number 3: 2
#   Enter number 4: 9
#   Enter number 5: 1
#
#   Results:
#   Sum:     23
#   Average: 4.6
#   Maximum: 9
#   Minimum: 1
#
# -----------------------------------------------------------------------------
# REQUIREMENTS
# -----------------------------------------------------------------------------
# - You MUST implement each calculation in its own function (see scaffold).
# - You may NOT use Python's built-in sum(), max(), or min() functions.
#   Implement the logic yourself using loops inside each function.
# - N must be a positive integer. If the user enters 0 or a negative
#   number, print an error message and stop.
#

# =============================================================================
# YOUR CODE BELOW — remove the # symbols from the scaffold and fill it in
# =============================================================================

def calculate_sum(numbers):
    """Calculates the sum of a list of numbers using a loop."""
    total = 0
    for num in numbers:
        total += num
    return total


def calculate_average(numbers):
    """Calculates the average of a list of numbers."""
    if len(numbers) == 0:
        return 0
    total = calculate_sum(numbers)
    average = total / len(numbers)
    return average

def find_maximum(numbers):
    """Finds the maximum value in a list of numbers using a loop."""
    max_val = numbers[0]
    for num in numbers:
        if num > max_val:
            max_val = num
    return max_val

def find_minimum(numbers):
    """Finds the minimum value in a list using a loop."""
    min_val = numbers[0]
    for num in numbers:
        if num < min_val:
            min_val = num
    return min_val

if __name__ == "__main__":
    count = int(input("How many numbers? "))

    if count <= 0:
        print("Error: Number of elements must be a positive integer")
    else:
        numbers = []
        for i in range(1, count + 1):
            val = float(input(f"Enter number{i}: "))
            numbers.append(val)

        print("\nResults:")
        print(f"Sum:    {calculate_sum(numbers)}")
        print(f"Average:    {calculate_average(numbers)}")
        print(f"Maximum:    {find_maximum(numbers)}")
        print(f"Minimum:    {find_minimum(numbers)}")