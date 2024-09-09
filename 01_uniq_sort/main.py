import random


def get_result(items):
    return list(set(items))


input = [random.randint(0, 5) for _ in range(7)]
print('\nВходной массив:', ', '.join(map(str, input)))

result = get_result(input)
print('\nРезультат:', ', '.join(map(str, result)))
