repeat_ = 'y'
characteristics = ('name', 'price', 'quantity', 'measure')
count = 0

goods = []
while True:
    repeat_ = input('Do you want to add new product? (y/n) ')
    if not repeat_ in ('y', 'n'):
        continue
    elif repeat_ == 'n':
        break
    id = input('Enter number of product: ')
    goods.append((id, {}))
    for characteristic in characteristics:
        goods[count][1][characteristic] = \
            input(f'Enter {characteristic} of product: ')
    count += 1
print('Goods:')
for item in goods:
    print(item)

# goods = [
# (1, {'name': 'компьютер', 'price': 20000, 'quantity': 5, 'measure': 'шт.'}),
# (2, {'name': 'принтер', 'price': 6000, 'quantity': 2, 'measure': 'шт.'}),
# (3, {'name': 'сканер', 'price': 2000, 'quantity': 7, 'measure': 'шт.'})
#     ]

analytics = {}
for characteristic in characteristics:
    analytics[characteristic] = [product[1][characteristic] for product in goods]
print('Analytics:')
for key, value in analytics.items():
    print(key, value)