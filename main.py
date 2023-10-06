while True:
    def display_even_numbers():
        try:
            start = int(input("Введіть початкове число: "))
            end = int(input("Введіть кінцеве число: "))

            print(f"Парні числа між {start} і {end}:")

            # Перевірка, яке число є меншим і більшим
            if start < end:
                for num in range(start, end + 1):
                    if num % 2 == 0:
                        print(num)
            else:
                for num in range(end, start + 1):
                    if num % 2 == 0:
                        print(num)
        except ValueError:
            print("Будь ласка, введіть правильні числа.")


    display_even_numbers()

    продовжити = input('чи бажаєте ввести інші числа? (так/ні)')
    if продовжити.lower() != 'так':
        break
