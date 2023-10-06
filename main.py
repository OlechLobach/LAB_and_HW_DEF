def is_prime(number):
    if number <= 1:
        return False
    for i in range(2, int(number**0.5) + 1):
        if number % i == 0:
            return False
    return True
number = int(input("Введіть число: "))
result = is_prime(number)

if result:
    print(f"{number} є простим числом.")
else:
    print(f"{number} не є простим числом.")
