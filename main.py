def display_square(side_length, symbol, filled):
    if filled:
        for _ in range(side_length):
            print(symbol * side_length)
    else:
        print(symbol * side_length)
        for _ in range(side_length - 2):
            print(symbol + " " * (side_length - 2) + symbol)
        print(symbol * side_length)
side_length = int(input("Введіть довжину сторони квадрата: "))
symbol = input("Введіть символ для відображення: ")
filled = input("Заповнений квадрат (True) чи порожній (False)? (True/False): ").lower() == "true"

display_square(side_length, symbol, filled)
