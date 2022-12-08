
def func(arr, n):
    table = [0 for _ in range(100)]

    for element in arr:
        table[element] += 1

    for element in arr:
        if element == 50:
            continue
        elif table[100-element] != 0:
            return 1
    return 0

print(func([1, 52, 48], 3))
print(func([50, 42], 2))
print(func([4, 13, 63, 87], 4))