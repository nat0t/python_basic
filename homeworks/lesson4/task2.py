source = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
result = [item for index, item in enumerate(source[1:]) if item > source[index]]
print(result)