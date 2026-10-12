def list_analyser(numbers):
    if not numbers:
        return "List is empty"
        

    smallest = numbers[0]
    largest = numbers[0]
    total = numbers[0]

    if len(numbers) > 1:
        for num in numbers[1:]:
            if num > largest:
                largest = num
            elif num < smallest:
                smallest = num
            total += num

    average = round(total/len(numbers), 2)

    return(f"smallest: {smallest}\n"
        f"largest: {largest}\n"
        f"Total: {total}\n"
        f"Average: {average}")

numbers = [12, 5, 27, 8, 14]
print(list_analyser(numbers))
