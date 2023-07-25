# для неотрицательных чисел фибоначчи
def fibonacci(count):
    num1 = 0
    num2 = 1
    for i in range(count):
        result = num1
        num1, num2 = num2, num1+num2
        yield result


count = int(input('Количество чисел: \n'))
print(*fibonacci(count))