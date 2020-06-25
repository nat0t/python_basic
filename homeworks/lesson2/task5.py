rating = [7, 5, 3, 3, 2]
print(f'Source rating:\n{rating}')

number = None
while True:
    number = input('Enter natural number (if you want to finish typing, enter "!q"): ')
    if number == '!q':
        break
    elif not number.isdigit() or int(number) == 0:
        print('Entered number is not natural.')
        continue
    number = int(number)
    for item in rating[:]:
        if number > item:
            rating.insert(rating.index(item), number)
            break
    else:
        rating.append(number)
print(f'New rating:\n{rating}')