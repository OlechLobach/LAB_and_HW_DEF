def is_prime(number):
    if number <= 1:
        return False
    if number <= 3:
        return True
    if number % 2 == 0 or number % 3 == 0:
        return False
    i = 5
    while i * i <= number:
        if number % i == 0 or number % (i + 2) == 0:
            return False
        i += 6


num = int(input('введіть число для перевірки'))
result = is_prime(num)
if result:
    print(f"{num} є простим числом.")
else:
    print(f"{num} не є простим числом.")