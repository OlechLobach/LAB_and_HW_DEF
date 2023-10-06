def calculate_product_in_range(start, end):
    if start > end:
        start, end = end, start
    product = 1
    for num in range(start, end + 1):
        product *= num
    return product
start_range = int(input("Введіть початок діапазону: "))
end_range = int(input("Введіть кінець діапазону: "))

result = calculate_product_in_range(start_range, end_range)
print(f"Добуток чисел у діапазоні від {start_range} до {end_range}: {result}")
