while True:
    def count_digits(number):
        num_str = str(number)
        digit_count = len(num_str)
        return digit_count
    num = int(input("Введіть число: "))
    result = count_digits(num)
    print(f"Кількість цифр у числі {num}: {result}")
    продовжити = input("Чи бажаєте підоахувати кількість цифр в іншому числі?(так/ні):")
    if продовжити.lower() !='так':
        break