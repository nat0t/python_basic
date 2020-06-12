while True:
    a = input('Enter the distance you ran at the first day (in kilometers): ')
    b = input('Enter the distance you want to run (in kilometers): ')
    # Without float values
    if not a.isdigit() or not b.isdigit():
        print('Entered values are incorrect.')
        continue
    days = 0
    a = int(a)
    b = int(b)
    while a < b:
        a *= 1.1
        days += 1
    print(f"You'll run {b} kilometers in {days} days.")
    break