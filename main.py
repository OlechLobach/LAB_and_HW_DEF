def is_happy_number(number):
    num_str = str(number)
    if len(num_str) != 6:
        return False
    first_half = num_str[:3]
    second_half = num_str[3:]
    sum_first_half = sum(map(int, first_half))
    sum_second_half = sum(map(int, second_half))
    return sum_first_half == sum_second_half

num = int(input('Введіть число: '))
result = is_happy_number(num)

if result:
    print(f"{num} - щасливе число.")
else:
    print(f"{num} - не щасливе число.")
