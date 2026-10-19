"""
Matrix Row Sums — With Column Sums and Row Averages
Suggested time: 15–20 minutes

Problem

Given a matrix (a list containing rows of numbers), calculate and display the total of each row, the total of each column, and the average of each row.
Examples
Starting matrix: matrix = [[2, 4, 6], [1, 3, 5], [10, 20, 30]]
Row 1 total: 12 | Row 1 average: 4.0
Row 2 total: 9 | Row 2 average: 3.0
Row 3 total: 60 | Row 3 average: 20.0
Column 1 total: 13
Column 2 total: 27
Column 3 total: 41
Constraints
Use nested loops.
Do not use sum() or import libraries.
You may use len() for the averages.
Your solution should work for a matrix with a different number of rows and a different number of columns.
Do not hardcode the answer.
Calculate column totals using a separate nested loop (or a single pass with a list of accumulators — your choice).
What This Tests: Nested lists, nested loops, accumulators, indexing, and handling rectangular grids generically.
"""

def mat_row_sum(matrix):
    
    row_sums = {}
    for i in range(len(matrix)):
        row_total = 0
        count = 0
        for item in matrix[i]:
            row_total += item
            count += 1
        average = round(row_total/count, 2)
        row_sums[i+1] = (row_total, average)
    return row_sums

matrix = [[2, 4, 6], [1, 3, 5], [10, 20, 30]]
row_sums = mat_row_sum(matrix)

for row, data in row_sums.items():
    print(
        f"Row {row} total: {data[0]} | Row {row} average: {data[1]}"
    )

def mat_col_sum(matrix):
    col_sums = []

    max_mat = len(matrix[0])
    for mat in matrix[1:]:
        if len(mat) > max_mat:
            max_mat = len(mat)

    for i in range(max_mat):
        col_total = 0
        for j in range(len(matrix)):
            try:
                col_total += matrix[j][i]
            except IndexError:
                continue
        col_sums.append(col_total)
    return col_sums
    
print("\n")

col_sums = mat_col_sum(matrix)
for i in range(len(col_sums)):
    print(f"Column {i+1} total: {col_sums[i]}")
