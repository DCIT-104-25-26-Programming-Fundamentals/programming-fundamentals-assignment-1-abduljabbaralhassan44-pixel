# =============================================================================
# PROGRAMMING FUNDAMENTALS — Assignment 4
# Topic: Multi-dimensional Arrays (2D Lists), Nested Loops, and Functions
# =============================================================================
#
# TASK: Matrix Operations
#
# Write a Python program that performs three operations on matrices (2D lists),
# each implemented in its own function.
#
# -----------------------------------------------------------------------------
# PART A — Transpose a Matrix
# -----------------------------------------------------------------------------
# - Read an M x N matrix from the user.
# - Compute and display its transpose (rows become columns, columns become rows).
#
# Example (2 x 3 input):
#
#   Original Matrix:      Transposed Matrix:
#   1  2  3               1  4
#   4  5  6               2  5
#                         3  6
#
# -----------------------------------------------------------------------------
# PART B — Add Two Matrices
# -----------------------------------------------------------------------------
# - Read two matrices of exactly the same size (M x N).
# - Compute their element-wise sum and display the result.
#   (Each position in the result = the sum of the values at that position
#    in both matrices.)
#
# -----------------------------------------------------------------------------
# PART C — Multiply Two Matrices
# -----------------------------------------------------------------------------
# - Read matrix A of size M x N and matrix B of size N x P.
#   (The number of COLUMNS in A must equal the number of ROWS in B.)
# - Compute and display the matrix product A × B (result is M x P).
#
# -----------------------------------------------------------------------------
# EXPECTED INPUT FORMAT
# -----------------------------------------------------------------------------
# When entering a row, the user types all values on one line separated by spaces:
#
#   Enter number of rows: 2
#   Enter number of columns: 3
#   Enter row 1: 1 2 3
#   Enter row 2: 4 5 6
#
# -----------------------------------------------------------------------------
# REQUIREMENTS
# -----------------------------------------------------------------------------
# - Use nested loops for all operations (no NumPy or other libraries).
# - Each operation must be in its own function (see scaffold below).
# - Display each matrix in a neat, aligned grid format.
# - Tip: Complete Part A first, then Parts B and C.
#

#
# =============================================================================
# YOUR CODE BELOW — remove the # symbols from the scaffold and fill it in
# =============================================================================

def print_matrix(matrix):
    """Helper function to print a 2D list in a clean grid format."""
    for row in matrix:
        print(" ".join(f"{val:>4}" for val in row))

def transpose_matrix(matrix):
    """Compute the transpose of an M x N matrix."""
    rows = len(matrix)
    cols = len(matrix[0])

    # Create empty N x M result matrix
    transposed = []
    for c in range(cols):
        new_row = []
        for r in range(rows):
            new_row.append(matrix[r][c])
        transposed.append(new_row)
    return transposed

def add_matrices(matrix_a, matrix_b):
    """Adds two matrices of the same dimensions element-wise."""
    rows = len(matrix_a)
    cols = len(matrix_a[0])

    result = []
    for r in range(rows):
        new_row = []
        for c in range(cols):
            new_row.append(matrix_a[r][c] + matrix_b[r][c])
        result.append(new_row)
    return result

def multiply_matrices(matrix_a, matrix_b):
    """Multiplies two matrices A (M x N) and B (N x P)."""
    rows_a = len(matrix_a)
    cols_a = len(matrix_a[0])
    cols_b = len(matrix_b[0])

    # Result size will be rows_A x cols_B
    for i in range(rows_a):
        new_row = []
        for j in range (cols_b):
            # Calculate the dot product of row i from A and column j from B
            dot_product = 0
            for k in range(cols_a):
                dot_product += matrix_a[i][k] * matrix_b[k][j]
            new_row.append(dot_product)
        result.append(new_row)
    return result

def read_matrix(rows, label=""):
    """Reads a matrix row by row from user input."""
    matrix = []
    if label:
        print(f"--- Entering {label} ---")
    for i in range(1, rows + 1):
        row_vals = list(map(int, input(f"Enter row {i}: ").split()))
        matrix.append(row_vals)
    return matrix

if __name__ == "__main__":
    print("=== Part A: Transpose a Matrix ===")
    m = int(input("Enter number of rows: "))
    n = int(input("Enter number of columns: "))
    matrix = read_matrix(m, n)

    print("\nOriginal Matrix:")
    print_matrix(matrix)

    print("\nTransposed Matrix:")
    print_matrix(transpose_matrix(matrix))

    print("\n=== Part B: Matrix Addition ===")
    print("Enter Matrix B (same dimensions M x N):")
    matrix_b = read_matrix(m, "Matrix B")

    print("\nMatrix A + Matrix B:")
    print_matrix(add_matrices(matrix_a, matrix_b))

    print("\n=== Part C: Matrix Multiplication ===")
    p = int(input("Enter number of columns for Matrix C (Matrix B is {n} x P) "))
    matrix_c = read_matrix(n, "Matrix C")

    print("\nMatrix A x Matrix C:")
    print_matrix(multiply_matrices(matrix_a, matrix_c))