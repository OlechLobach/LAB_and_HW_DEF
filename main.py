def is_palindrome(number):
    num_str = str(number)
    return num_str == num_str[::-1]
num = int(input("Введіть число: "))
result = is_palindrome(num)
if result:
    print(f"{num} - це паліндром.")
else:
    print(f"{num} - не паліндром.")
