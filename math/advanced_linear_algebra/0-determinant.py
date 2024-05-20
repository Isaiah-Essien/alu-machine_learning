def determinant(matrix):
    """
    Calculate the determinant of a square matrix.

    Args:
        matrix (list of lists): The matrix whose determinant should be calculated.

    Returns:
        float: The determinant of the matrix.

    Raises:
        TypeError: If matrix is not a list of lists.
        ValueError: If matrix is not square.

    """
    # Check if matrix is a list of lists
    if not isinstance(matrix, list) or not all(isinstance(row, list) for row in matrix):
        raise TypeError("matrix must be a list of lists")

    # Check if matrix is square
    if len(matrix) != len(matrix[0]):
        raise ValueError("matrix must be a square matrix")

    # Base case for 0x0 matrix
    if len(matrix) == 0:
        return 1

    # Base case for 1x1 matrix
    if len(matrix) == 1:
        return matrix[0][0]

    det = 0
    for i in range(len(matrix)):
        # Calculate the cofactor
        cofactor = (-1) ** i * matrix[0][i] * determinant(minor(matrix, 0, i))
        det += cofactor

    return det

def minor(matrix, i, j):
    """
    Calculate the minor of a matrix by removing row i and column j.

    Args:
        matrix (list of lists): The matrix from which the minor should be calculated.
        i (int): The row index to remove.
        j (int): The column index to remove.

    Returns:
        list of lists: The minor of the matrix.

    """
    return [row[:j] + row[j+1:] for row in (matrix[:i] + matrix[i+1:])]
