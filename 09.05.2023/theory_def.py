def count_above_threshold(numbers: list, threshold: int):
    count = 0
    for number in numbers:
        if number > threshold:
            count += 1
    return count


temperatures = [20, 25, 27, 30, 30, 28, 24]
temperatures1 = [20, 25, 27, 30, 30, 28, 24]
temperatures2 = [20, 25, 27, 30, 30, 28, 24]
temperatures3 = [20, 25, 27, 30, 30, 28, 24]
threshold = 25
result = count_above_threshold(temperatures, threshold)
print(f"Количество элементов выше порога ({threshold}):", result)  # Output: Количество элементов выше порога (25): 3
