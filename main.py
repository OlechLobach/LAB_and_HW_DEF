def find_min():
    try:
        num1 = float(input("Введіть перше число: "))
        num2 = float(input("Введіть друге число: "))
        num3 = float(input("Введіть третє число: "))
        num4 = float(input("Введіть четверте число: "))
        min_value = min(num1, num2, num3, num4)
        return min_value
    except ValueError:
        print("Будь ласка, введіть правильні числа.")

min_number = find_min()

if min_number is not None:
    print(f"Мінімальне число: {min_number}")
