# 9_7 Декораторы
def is_prime(func):
    def wrapper(a, b, c):
        sum = func(a, b, c)
        if sum < 2:
            return False
        for i in range(2, int(sum ** 0.5) + 1):
            if sum % i == 0:
                print('Составное число')
            else:
                print('Простое число')
            return sum
    return wrapper

@is_prime
def sum_three(a, b, c):
    return a + b + c

result = sum_three(2, 3, 6)
print(result)
