"""
Matrix Multiplication
Suggested time: 20–25 minutes
Problem
Given two matrices, A and B, calculate their product matrix. Matrix multiplication is possible only if the number of columns in A equals the number of rows in B.
Examples
Matrix A: [[1, 2], [3, 4]]
Matrix B: [[5, 6], [7, 8]]
Product Matrix:
[19, 22]
[43, 50]
(Explanation: 1×5 + 2×7 = 19; 1×6 + 2×8 = 22, etc.)
Constraints
Use nested loops (three levels of loops are needed).
Do not import libraries such as numpy.
Do not use list comprehensions.
Dynamically build the result matrix based on the dimensions of A and B.
Do not hardcode the answer.
What This Tests: Advanced nested loops, matrix dimensions, indexing, and accumulators.

"""

def mat_multiplication(matA, matB):
    if len(matA[0]) != len(matB):
        return "Matrix multiplication cannot work for this pair in the given order"

    product = []
    for i in range(len(matA)):
        product_row = []
        for j in range(len(matB[0])):
            product_row.append(matA[i][j] * matB[j][i])
    return product_row


matA = [[1, 2], [3, 4]]
matB = [[5, 6], [7, 8]]

print(mat_multiplication(matA, matB))
