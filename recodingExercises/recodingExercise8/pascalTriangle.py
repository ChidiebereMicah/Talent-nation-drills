def pascal_rows(n):
    triangle = [[1], [1,1]]
    for i in range(n-2):
        row = []
        prev_row = triangle[-1]
        for j in range(len(prev_row)):
            if j == 0:
                row.append(prev_row[0])
                row.append(prev_row[0] + prev_row[1])
            elif j == len(prev_row) - 1:
                row.append(prev_row[j])
            else:
                row.append(prev_row[j] + prev_row[j+1])

        triangle.append(row)

    return triangle

pascal_triangle = pascal_rows(10)

count = len(pascal_triangle) - 1
for row in pascal_triangle:
    print(" "*count, end="")
    for num in row:
        print(num, end=" ")
    print("\r")
    count -= 1
    


