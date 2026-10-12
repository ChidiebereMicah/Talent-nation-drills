def mat_row_sums(matrix):
    row_sum = 0
    # mat_sum = [row_sum += element for row in matrix for element in row]

    mat_sum = []
    for row in matrix:
        row_sum = 0
        for element in row:
            row_sum += element
        mat_sum.append(row_sum)
    return mat_sum


matrix = [[2, 4, 6], [1, 3, 5], [10, 20, 30]]
mat_sum = mat_row_sums(matrix)

for i in range(len(mat_sum)):
    print(f"Row {i} total: {mat_sum[i]}")