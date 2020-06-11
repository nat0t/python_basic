while True:
    n = input('Please input natural number n: ')
    if not n.isdigit():
        print('You entered not a natural number.')
        continue
    sum = int(n) + int(n+n) + int(n+n+n)
    print(f'{n}+{n}{n}+{n}{n}{n}={sum}')
    break