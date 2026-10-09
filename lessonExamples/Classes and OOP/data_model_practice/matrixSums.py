# def matrix_sums(matrix):
#     rows = [sum(row) for row in matrix]

#     col = [ for row in zip(matrix)]


matrix = [[1, 2], 
          [3, 4]]
mat_sum = []
for i in range(len(matrix)):
    total = 0
    for j in range(len(matrix)):
        total += matrix[j][i]
    mat_sum.append(total)
# print(list(zip(matrix)))

print(mat_sum)