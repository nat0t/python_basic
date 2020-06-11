while True:
    number = input('Please input natural number: ')
    temp = number
    if not number.isdigit():
        print('You entered not a natural number.')
        continue
    number = int(number)
    number, max_digit = divmod(number, 10)
    while number > 0:
        number, last_digit = divmod(number, 10)
        if max_digit < last_digit:
            max_digit = last_digit
    print(f'Max digit in {temp} is {max_digit}')
    break