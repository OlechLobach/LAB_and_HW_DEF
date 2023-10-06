def display_line(length, direction, symbol):
    if direction == "horizontal":
        print(symbol * length)
    elif direction == "vertical":
        for _ in range(length):
            print(symbol)
    else:
        print("Неправильний напрямок. Виберіть 'horizontal' або 'vertical'.")

length_h = int(input("Введіть горизонтальну довжину: "))
symbol_h = input("Введіть символ для горизонтальної лінії: ")
length_v = int(input("Введіть вертикальну довжину: "))
symbol_v = input("Введіть символ для вертикальної лінії: ")
direction_h = "horizontal"
display_line(length_h, direction_h, symbol_h)


direction_v = "vertical"
display_line(length_v, direction_v, symbol_v)
