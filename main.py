def find_max():
    try:
        num1 = float(input("Введіть перше число: "))
        num2 = float(input("Введіть друге число: "))
        num3 = float(input("Введіть третє число: "))
        num4 = float(input("Введіть четверте число: "))
        max_value = max(num1, num2, num3, num4)
        return max_value
    except ValueError:
        print("Будь ласка, введіть правильні числа.")
max_number = find_max()
if max_number is not None:
    print(f"Максимальне число: {max_number}")