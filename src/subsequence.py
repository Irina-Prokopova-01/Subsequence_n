def generate_subsequence(n):
    result = []
    number = 1
    while len(result) < n:
        result.extend([number] * number)
        number += 1
    return result[:n]


n = int(input("Введите количество элементов последовательности: "))
subsequence = generate_subsequence(n)
print(subsequence)
